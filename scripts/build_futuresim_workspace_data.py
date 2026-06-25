#!/usr/bin/env python3
"""Export small workspace artifacts for the static FutureSim trace viewer."""

from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path
from typing import Any


WORKSPACE_RE = re.compile(r"(/[A-Za-z0-9_./-]+?/workspace)")
SECRET_RE = re.compile(
    r"(?i)(sk-[A-Za-z0-9_-]{20,}|[A-Za-z0-9_-]*(?:api|token|key)[A-Za-z0-9_-]*[=:][A-Za-z0-9_.-]{16,})"
)
DATE_RE = re.compile(r"(20\d{2}[-_]\d{2}[-_]\d{2})")
MAX_FILE_BYTES = 1_000_000


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--data-dir", type=Path, default=Path("futuresim/traces/data"))
    parser.add_argument(
        "--workspace-root",
        action="append",
        type=Path,
        default=[Path("/lustre/fast/fast/sgoel/forecasting/current_sim/final_runs_v37")],
    )
    args = parser.parse_args()

    manifest_path = args.data_dir / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    out_root = args.data_dir / "workspaces"
    if out_root.exists():
        shutil.rmtree(out_root)
    out_root.mkdir(parents=True)

    for run in manifest["runs"]:
        workspace = find_workspace(args.data_dir, run, args.workspace_root)
        if not workspace:
            run.pop("workspace", None)
            continue
        workspace_manifest = export_workspace(args.data_dir, out_root, run, workspace)
        run["workspace"] = {
            "manifest_path": workspace_manifest["path"],
            "file_count": workspace_manifest["file_count"],
            "memory_file_count": workspace_manifest["memory_file_count"],
            "prediction_file_count": workspace_manifest["prediction_file_count"],
        }

    manifest_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def find_workspace(data_dir: Path, run: dict[str, Any], roots: list[Path]) -> Path | None:
    for day in run.get("days", []):
        text = (data_dir / day["path"]).read_text(encoding="utf-8", errors="ignore")
        for match in WORKSPACE_RE.findall(text):
            path = Path(match)
            if path.exists():
                return path

    for root in roots:
        for path in root.glob(f"*/{run['run_id']}/agents/*/workspace"):
            if path.exists():
                return path
    return None


def export_workspace(data_dir: Path, out_root: Path, run: dict[str, Any], workspace: Path) -> dict[str, Any]:
    run_root = out_root / run["agent_slug"] / run["run_id"]
    files_root = run_root / "files"
    files = []
    for source in workspace_files(workspace):
        if source.stat().st_size > MAX_FILE_BYTES:
            continue
        rel = source.relative_to(workspace)
        target = files_root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        copy_redacted(source, target)
        files.append({
            "label": str(rel),
            "kind": file_kind(rel),
            "date": file_date(rel.name),
            "size": target.stat().st_size,
            "path": str(target.relative_to(data_dir)),
        })

    files.sort(key=lambda item: (item["kind"] != "memory", item["date"] or "9999-99-99", item["label"]))
    payload = {
        "agent_slug": run["agent_slug"],
        "agent_name": run["agent_name"],
        "run_id": run["run_id"],
        "seed_label": run.get("seed_label", ""),
        "workspace_source": str(workspace),
        "files": files,
    }
    path = run_root / "manifest.json"
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return {
        "path": str(path.relative_to(data_dir)),
        "file_count": len(files),
        "memory_file_count": sum(1 for item in files if item["kind"] == "memory"),
        "prediction_file_count": sum(1 for item in files if item["kind"] == "predictions"),
    }


def workspace_files(workspace: Path) -> list[Path]:
    files = []
    agents = workspace / "AGENTS.md"
    if agents.is_file():
        files.append(agents)
    for dirname in ["memory", "predictions"]:
        root = workspace / dirname
        if root.exists():
            files.extend(path for path in root.rglob("*") if path.is_file())
    return files


def copy_redacted(source: Path, target: Path) -> None:
    text = source.read_text(encoding="utf-8", errors="replace")
    target.write_text(SECRET_RE.sub("[redacted]", text), encoding="utf-8")


def file_kind(path: Path) -> str:
    first = path.parts[0] if path.parts else ""
    if first in {"memory", "predictions"}:
        return first
    return "workspace"


def file_date(name: str) -> str:
    match = DATE_RE.search(name)
    return match.group(1).replace("_", "-") if match else ""


if __name__ == "__main__":
    main()
