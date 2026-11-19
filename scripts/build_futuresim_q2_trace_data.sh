#!/usr/bin/env bash
set -euo pipefail

repo=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
q2_runs=${FSIM_Q2_RUNS:-/is/cluster/fast/sgoel/forecasting/current_sim/Q2results}
out="$repo/futuresim/traces/data/q2"
start_date=2026-03-25
args=()

find_source() {
  local run_dir="$1" source_name="$2"
  find "$run_dir/agents" -maxdepth 2 -type f -name "$source_name" -print -quit 2>/dev/null
}

add_run() {
  local agent="$1" slug="$2" model="$3" harness="$4" seed="$5" run_dir="$6" source_name="$7"
  local source
  source=$(find_source "$run_dir" "$source_name")
  if [[ -z "$source" ]]; then
    echo "missing $source_name in $run_dir" >&2
    exit 1
  fi
  args+=(--run "$agent|$slug|$model|$harness|$seed|$source@$start_date")
}

mkdir -p "$out"
rm -rf "$out/runs" "$out/workspaces" "$out/archive" "$out/manifest.json"

add_run "GPT 5.6 Sol" gpt-5.6-sol gpt-56-sol Codex r00 "$q2_runs/codex_aljazeera2026Q2v38_gpt56sol_max_r00/26-08-01-03-53-08" codex_stdout.jsonl
add_run "GPT 5.6 Sol" gpt-5.6-sol gpt-56-sol Codex r01 "$q2_runs/codex_aljazeera2026Q2v38_gpt56sol_max_r01/26-08-01-15-41-52" codex_stdout.jsonl
add_run "GPT 5.6 Sol" gpt-5.6-sol gpt-56-sol Codex r02 "$q2_runs/codex_aljazeera2026Q2v38_gpt56sol_max_r02/26-08-02-01-32-58" codex_stdout.jsonl

add_run "GPT 5.5" gpt-5.5 gpt-55 Codex r00 "$q2_runs/codex_aljazeera2026Q2v38_gpt55_xhigh_r00/26-08-01-12-55-55" codex_stdout.jsonl
add_run "GPT 5.5" gpt-5.5 gpt-55 Codex r01 "$q2_runs/codex_aljazeera2026Q2v38_gpt55_xhigh_r01/26-08-01-15-41-57" codex_stdout.jsonl
add_run "GPT 5.5" gpt-5.5 gpt-55 Codex r02 "$q2_runs/codex_aljazeera2026Q2v38_gpt55_xhigh_r02/26-08-02-02-43-28" codex_stdout.jsonl

add_run "Opus 5 v1" opus-5-v1 claude-opus-5 "Claude Code" r00 "$q2_runs/claude_code_aljazeera2026Q2v38_opus5_v1_r00/26-08-03-00-40-27" claude_code_stdout.jsonl
add_run "Opus 5 v1" opus-5-v1 claude-opus-5 "Claude Code" r01 "$q2_runs/claude_code_aljazeera2026Q2v38_opus5_v1_r01/26-08-03-08-07-58" claude_code_stdout.jsonl

add_run "Fable 5 v1" fable-5-v1 claude-fable-5 "Claude Code" r00 "$q2_runs/claude_code_aljazeera2026Q2v38_fable5_cont01_r00_restart/26-08-01-12-55-55" claude_code_stdout.jsonl
add_run "Fable 5 v1" fable-5-v1 claude-fable-5 "Claude Code" r01 "$q2_runs/claude_code_aljazeera2026Q2v38_fable5_retry_r01/26-08-01-20-40-56" claude_code_stdout.jsonl
add_run "Fable 5 v1" fable-5-v1 claude-fable-5 "Claude Code" r02 "$q2_runs/claude_code_aljazeera2026Q2v38_fable5_r02/26-08-02-01-32-30" claude_code_stdout.jsonl

add_run "GLM 5.2" glm-5.2 glm-52 "Claude Code" r00 "$q2_runs/claude_code_aljazeera2026Q2v38_glm52_r00/26-08-01-03-51-35" claude_code_stdout.jsonl
add_run "GLM 5.2" glm-5.2 glm-52 "Claude Code" r01 "$q2_runs/claude_code_aljazeera2026Q2v38_glm52_r01/26-08-01-12-55-35" claude_code_stdout.jsonl
add_run "GLM 5.2" glm-5.2 glm-52 "Claude Code" r02 "$q2_runs/claude_code_aljazeera2026Q2v38_glm52_r02/26-08-01-15-36-43" claude_code_stdout.jsonl
add_run "GLM 5.2" glm-5.2 glm-52 "Claude Code" r03 "$q2_runs/claude_code_aljazeera2026Q2v38_glm52_r03/26-08-01-20-40-51" claude_code_stdout.jsonl
add_run "GLM 5.2" glm-5.2 glm-52 "Claude Code" r04 "$q2_runs/claude_code_aljazeera2026Q2v38_glm52_r04/26-08-02-02-43-54" claude_code_stdout.jsonl

add_run "DeepSeek V4 Flash 0731" deepseek-v4-flash-0731 deepseek-v4-flash-0731 "Claude Code" r01 "$q2_runs/claude_code_aljazeera2026Q2v38_deepseek_v4flash0731_v3_openrouter_r01/26-08-01-15-41-53" claude_code_stdout.jsonl
add_run "DeepSeek V4 Flash 0731" deepseek-v4-flash-0731 deepseek-v4-flash-0731 "Claude Code" r02 "$q2_runs/claude_code_aljazeera2026Q2v38_deepseek_v4flash0731_v3_openrouter_r02/26-08-01-20-41-09" claude_code_stdout.jsonl
add_run "DeepSeek V4 Flash 0731" deepseek-v4-flash-0731 deepseek-v4-flash-0731 "Claude Code" r03 "$q2_runs/claude_code_aljazeera2026Q2v38_deepseek_v4flash0731_v3_openrouter_r03/26-08-02-01-32-56" claude_code_stdout.jsonl

python "$repo/scripts/build_futuresim_trace_viewer_data.py" --output "$out" --max-string-chars 10000 --gzip "${args[@]}"
python "$repo/scripts/build_futuresim_workspace_data.py" --data-dir "$out" --workspace-root "$q2_runs"
