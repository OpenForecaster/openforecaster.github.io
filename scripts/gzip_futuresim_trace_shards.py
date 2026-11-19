#!/usr/bin/env python3
"""Compress the day shards of trace data that was built without --gzip.

  gzip_futuresim_trace_shards.py futuresim/traces/data futuresim/traces/data/q2

Each <date>.json that a manifest lists becomes <date>.json.gz, written the way
build_futuresim_trace_viewer_data.py --gzip writes it. The manifest's day paths and the summaries'
trace_path values get the new name; nothing else in those files changes. A folder whose shards
are already compressed is left as it is.

2026 Q1 and Q2 were published as plain JSON and compressed this way, to keep the site under GitHub
Pages' size limit. Their build scripts pass --gzip since then, so a rebuild writes the same kind
of file and this script is only needed for data built before that.
"""
import argparse
import gzip
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_futuresim_trace_viewer_data import write_json  # noqa: E402

SHARD_NAME = re.compile(r'"(runs/[^"\\]+\.json)"')


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("data_dir", type=Path, nargs="+", help="A folder with a manifest.json and its runs/.")
    for data in parser.parse_args().data_dir:
        compress(data.resolve())


def compress(data):
    manifest = data / "manifest.json"
    paths = [day["path"] for run in json.loads(manifest.read_bytes())["runs"] for day in run["days"]]
    plain = [path for path in paths if path.endswith(".json")]
    before = after = 0
    for path in plain:
        source = data / path
        target = data / f"{path}.gz"
        payload = json.loads(source.read_bytes())
        write_json(target, payload, gzipped=True)
        if json.loads(gzip.decompress(target.read_bytes())) != payload:
            raise SystemExit(f"{target} does not read back as {source}")
        before += source.stat().st_size
        after += target.stat().st_size

    # Only the shards' names are rewritten, as text, so the rest of each file stays as it was.
    renamed = set(plain)
    for file in [manifest, *sorted((data / "summaries").glob("*.json"))]:
        text = file.read_bytes().decode("utf-8")
        new = SHARD_NAME.sub(lambda name: f'"{name[1]}.gz"' if name[1] in renamed else name[0], text)
        if new != text:
            file.write_bytes(new.encode("utf-8"))
    for path in plain:
        (data / path).unlink()
    print(f"{data}: {len(plain)} of {len(paths)} day shards compressed, {before:,} -> {after:,} bytes")


if __name__ == "__main__":
    main()
