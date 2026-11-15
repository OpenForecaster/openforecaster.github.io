#!/usr/bin/env bash
# Build the trace viewer's 2026 Q3 data (futuresim/traces/data/q3) from the 14 leaderboard runs.
#
# Claude Code runs are read from their stdout transcript. Codex and Muse runs are read from their
# session logs, because their sub-agents make most of the forecasts and stdout does not have them.
#
# The site is close to GitHub Pages' 1 GB limit, so two things differ from Q1 and Q2:
#   - the day shards are gzip-compressed (the viewer decompresses them), which keeps the same
#     10,000-character limit per text field as Q2 at about a third of the size;
#   - a run whose memory/ folder holds more than 5 MB of files other than Markdown notes (search
#     dumps, article scans) gets only the notes. The workspace manifest records how many files
#     were left out, and the viewer says so.
#
# The agents ran in a sandbox on a shared cluster. When one lists processes (ps, pgrep) the output
# shows other people's jobs, so lines of tool output that name a cluster path are left out
# (--hide-host-paths); the trace says how many lines were left out at that spot.
#
#   FSIM_Q3_RUNS   where the runs are      (default: the clean_runs_Q3v8 folder)
#   FSIM_Q3_OUT    where to write the data (default: futuresim/traces/data/q3)
#
# The day summaries are written by build_futuresim_trace_summaries.py (rule-based, as for Q1).
set -euo pipefail

repo=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
q3_runs=${FSIM_Q3_RUNS:-/is/cluster/fast/sgoel/forecasting/current_sim/clean_runs_Q3v8}
out=${FSIM_Q3_OUT:-$repo/futuresim/traces/data/q3}
start_date=2026-06-24
args=()

find_source() {
  local run_dir="$1" source_name="$2"
  find "$run_dir/agents" -maxdepth 2 -name "$source_name" -print -quit 2>/dev/null
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
rm -rf "$out/runs" "$out/workspaces" "$out/archive" "$out/summaries" "$out/manifest.json"

add_run "GPT 6.1 Sol" gpt-6.1-sol gpt-61-sol Codex r00 "$q3_runs/codex_aljazeera2026Q3v8_gpt61sol_max_exa_r00/26-11-14-01-06-59" codex_sessions
add_run "GPT 6.1 Sol" gpt-6.1-sol gpt-61-sol Codex r01 "$q3_runs/codex_aljazeera2026Q3v8_gpt61sol_max_exa_r01/26-11-14-01-07-04" codex_sessions

add_run "Opus 5.5" opus-5.5 claude-opus-5-5 "Claude Code" r00 "$q3_runs/claude_code_aljazeera2026Q3v8_opus55_exa_r00/26-11-13-00-42-18" claude_code_stdout.jsonl
add_run "Opus 5.5" opus-5.5 claude-opus-5-5 "Claude Code" r01 "$q3_runs/claude_code_aljazeera2026Q3v8_opus55_exa_r01/26-11-13-11-23-29" claude_code_stdout.jsonl

add_run "DeepSeek V4.1 Flash 1017" deepseek-v4.1-flash-1017 deepseek-v41-flash-1017 "Claude Code" r00 "$q3_runs/claude_code_aljazeera2026Q3v8_deepseek_v41flash1017_openrouter_exa_r00/26-11-13-03-50-34" claude_code_stdout.jsonl
add_run "DeepSeek V4.1 Flash 1017" deepseek-v4.1-flash-1017 deepseek-v41-flash-1017 "Claude Code" r01 "$q3_runs/claude_code_aljazeera2026Q3v8_deepseek_v41flash1017_openrouter_exa_r01/26-11-13-13-46-36" claude_code_stdout.jsonl
add_run "DeepSeek V4.1 Flash 1017" deepseek-v4.1-flash-1017 deepseek-v41-flash-1017 "Claude Code" r02 "$q3_runs/claude_code_aljazeera2026Q3v8_deepseek_v41flash1017_openrouter_exa_r02/26-11-13-17-42-17" claude_code_stdout.jsonl

add_run "GLM 5.3 Flash" glm-5.3-flash glm-53-flash "Claude Code" r00 "$q3_runs/claude_code_aljazeera2026Q3v8_glm53flash_exa_r00/26-11-12-23-58-37" claude_code_stdout.jsonl
add_run "GLM 5.3 Flash" glm-5.3-flash glm-53-flash "Claude Code" r01 "$q3_runs/claude_code_aljazeera2026Q3v8_glm53flash_exa_r01/26-11-13-01-50-54" claude_code_stdout.jsonl
add_run "GLM 5.3 Flash" glm-5.3-flash glm-53-flash "Claude Code" r02 "$q3_runs/claude_code_aljazeera2026Q3v8_glm53flash_exa_r02/26-11-13-03-35-25" claude_code_stdout.jsonl
add_run "GLM 5.3 Flash" glm-5.3-flash glm-53-flash "Claude Code" r03 "$q3_runs/claude_code_aljazeera2026Q3v8_glm53flash_exa_r03/26-11-13-11-49-09" claude_code_stdout.jsonl
add_run "GLM 5.3 Flash" glm-5.3-flash glm-53-flash "Claude Code" r05 "$q3_runs/claude_code_aljazeera2026Q3v8_glm53flash_exa_r05/26-11-13-14-56-48" claude_code_stdout.jsonl

add_run "Muse Wonder Full 1.0" muse-wonder-full-1.0 muse-wonder-full-10 Muse r00 "$q3_runs/muse_aljazeera2026Q3v8_wonderfull_max_exa_r00/26-11-14-15-31-51" muse_sessions
add_run "Muse Wonder Full 1.0" muse-wonder-full-1.0 muse-wonder-full-10 Muse r01 "$q3_runs/muse_aljazeera2026Q3v8_wonderfull_max_exa_r01/26-11-14-16-00-01" muse_sessions

python3 "$repo/scripts/build_futuresim_trace_viewer_data.py" --output "$out" --max-string-chars 10000 --gzip --hide-host-paths "${args[@]}"
python3 "$repo/scripts/build_futuresim_workspace_data.py" --data-dir "$out" --workspace-root "$q3_runs" --root-first --max-data-bytes 5000000
# Every run has the same market.csv (question titles and resolved answers).
python3 "$repo/scripts/build_futuresim_trace_summaries.py" --data-dir "$out" --overwrite \
  --market-csv "$q3_runs/muse_aljazeera2026Q3v8_wonderfull_max_exa_r00/26-11-14-15-31-51/market.csv"
