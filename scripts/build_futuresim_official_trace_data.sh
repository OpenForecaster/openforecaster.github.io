#!/usr/bin/env bash
set -euo pipefail

repo=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
official_runs=${FSIM_OFFICIAL_RUNS:-/fast/sgoel/forecasting/current_sim/official_runs_complete}
out="$repo/futuresim/traces/data"

args=()

find_source() {
  local run_dir="$1" source_name="$2"
  find "$run_dir/agents" -type f -name "$source_name" | head -1
}

add_run() {
  local agent="$1" slug="$2" model="$3" harness="$4" seed="$5" run_dir="$6" source_name="$7"
  local source
  source=$(find_source "$run_dir" "$source_name")
  if [[ -z "$source" ]]; then
    echo "missing $source_name in $run_dir" >&2
    exit 1
  fi
  args+=(--run "$agent|$slug|$model|$harness|$seed|$source")
}

add_stitched_run() {
  local agent="$1" slug="$2" model="$3" harness="$4" seed="$5" spec="$6"
  args+=(--run "$agent|$slug|$model|$harness|$seed|$spec")
}

require_handholding_v3() {
  local run_dir="$1"
  python - "$run_dir/config.json" <<'PY'
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
config = json.loads(path.read_text(encoding="utf-8"))
defaults = config.get("defaults") if isinstance(config.get("defaults"), dict) else {}
version = config.get("handholding_version") or defaults.get("handholding_version")
if version != "v3":
    raise SystemExit(f"{path.parent} is not handholding v3; found {version!r}")
PY
}

rm -rf "$out"

add_run "DeepSeek V4 Pro" ds-v4-pro deepseek-v4-pro "Claude Code" r00 "$official_runs/ds-v4-pro/26-05-01-18-54-31" claude_code_stdout.jsonl
add_run "DeepSeek V4 Pro" ds-v4-pro deepseek-v4-pro "Claude Code" r01 "$official_runs/ds-v4-pro/26-05-02-00-01-06" claude_code_stdout.jsonl
add_run "DeepSeek V4 Pro" ds-v4-pro deepseek-v4-pro "Claude Code" r02 "$official_runs/ds-v4-pro/26-05-02-12-17-09" claude_code_stdout.jsonl

add_run "GLM 5.1" glm-5.1 glm-51 "Claude Code" r00 "$official_runs/glm-5.1/26-05-03-21-51-35" claude_code_stdout.jsonl
add_run "GLM 5.1" glm-5.1 glm-51 "Claude Code" r01 "$official_runs/glm-5.1/26-05-05-17-56-54" claude_code_stdout.jsonl
add_run "GLM 5.1" glm-5.1 glm-51 "Claude Code" r02 "$official_runs/glm-5.1/26-05-04-18-41-13" claude_code_stdout.jsonl

add_run "GPT 5.5" gpt-5.5 gpt-55 Codex r00 "$official_runs/gpt-5.5/26-05-04-02-00-26" codex_stdout.jsonl
add_run "GPT 5.5" gpt-5.5 gpt-55 Codex r01 "$official_runs/gpt-5.5/26-06-01-14-27-01" codex_stdout.jsonl

add_run "Opus 4.6" opus-4.6 claude-opus-4-6 "Claude Code" r00 "$official_runs/opus-4.6/26-05-03-16-45-45" claude_code_stdout.jsonl
opus46_stitched=$(
  printf "%s@2025-12-24;%s@2026-02-06;%s@2026-03-06;%s@2026-03-28" \
    "$(find_source "$official_runs/opus-4.6/26-05-12-15-42-37" claude_code_stdout.jsonl)" \
    "$(find_source "$official_runs/opus-4.6/26-05-13-12-58-20" claude_code_stdout.jsonl)" \
    "$(find_source "$official_runs/opus-4.6/26-05-13-17-50-45" claude_code_stdout.jsonl)" \
    "$(find_source "$official_runs/opus-4.6/26-05-13-19-45-35" claude_code_stdout.jsonl)"
)
add_stitched_run "Opus 4.6" opus-4.6 claude-opus-4-6 "Claude Code" r01 "$opus46_stitched"

add_run "Opus 4.7" opus-4.7 claude-opus-4-7 "Claude Code" r00 "$official_runs/opus-4.7/26-05-17-23-14-12" claude_code_stdout.jsonl
add_run "Opus 4.7" opus-4.7 claude-opus-4-7 "Claude Code" r01 "$official_runs/opus-4.7/26-05-18-14-59-05" claude_code_stdout.jsonl
add_run "Opus 4.7" opus-4.7 claude-opus-4-7 "Claude Code" r02 "$official_runs/opus-4.7/26-05-18-02-25-32" claude_code_stdout.jsonl

add_run "Qwen 3.6 Plus" qwen-3.6-plus qwen36-plus OpenCode r00 "$official_runs/qwen-3.6-plus/26-05-02-00-01-06" opencode_stdout.jsonl
add_run "Qwen 3.6 Plus" qwen-3.6-plus qwen36-plus OpenCode r01 "$official_runs/qwen-3.6-plus/26-05-02-05-32-23" opencode_stdout.jsonl
add_run "Qwen 3.6 Plus" qwen-3.6-plus qwen36-plus OpenCode r02 "$official_runs/qwen-3.6-plus/26-05-02-17-28-54" opencode_stdout.jsonl

add_run "Fable 5" fable-5 claude-fable-5 "Claude Code" r00 "$official_runs/fable-5/26-06-10-01-14-28" claude_code_stdout.jsonl
add_run "Fable 5" fable-5 claude-fable-5 "Claude Code" r01 "$official_runs/fable-5/26-06-10-11-14-42" claude_code_stdout.jsonl

glm52_r00="$official_runs/glm-5.2/26-06-14-02-57-24"
glm52_r01="$official_runs/glm-5.2/26-06-14-19-17-03"
glm52_r02="$official_runs/glm-5.2/26-06-15-01-56-56"
require_handholding_v3 "$glm52_r00"
require_handholding_v3 "$glm52_r01"
require_handholding_v3 "$glm52_r02"
add_run "GLM 5.2" glm-5.2 glm-52 "Claude Code" r00 "$glm52_r00" claude_code_stdout.jsonl
add_run "GLM 5.2" glm-5.2 glm-52 "Claude Code" r01 "$glm52_r01" claude_code_stdout.jsonl
add_run "GLM 5.2" glm-5.2 glm-52 "Claude Code" r02 "$glm52_r02" claude_code_stdout.jsonl

add_run "Opus 4.8" opus-4.8 claude-opus-4-8 "Claude Code" r00 "$official_runs/opus-4.8/26-05-29-00-44-11" claude_code_stdout.jsonl
add_run "Opus 4.8" opus-4.8 claude-opus-4-8 "Claude Code" r01 "$official_runs/opus-4.8/26-06-05-02-36-11" claude_code_stdout.jsonl
add_run "Opus 4.8" opus-4.8 claude-opus-4-8 "Claude Code" r02 "$official_runs/opus-4.8/26-06-05-11-17-13" claude_code_stdout.jsonl

python "$repo/scripts/build_futuresim_trace_viewer_data.py" --output "$out" "${args[@]}"
python "$repo/scripts/build_futuresim_workspace_data.py" --data-dir "$out"
python "$repo/scripts/build_futuresim_leaderboard_data.py"
