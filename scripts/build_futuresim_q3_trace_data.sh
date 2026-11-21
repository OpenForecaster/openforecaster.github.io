#!/usr/bin/env bash
# Build the trace viewer's 2026 Q3 data (futuresim/traces/data/q3) from the 20 leaderboard runs.
#
# Claude Code runs are read from their stdout transcript. Codex, Muse and Antigravity runs are read
# from their session logs, because stdout does not have their sub-agents, who make many of the
# forecasts.
#
# GitHub Pages allows a site of 1 GB, so the data is kept small in three ways:
#   - the day shards are gzip-compressed, as Q1's and Q2's are (the viewer decompresses them);
#   - a text field is cut at 10,000 characters, as in Q2;
#   - a run whose memory/ folder holds more than 10 MB of files other than Markdown notes (search
#     dumps, article scans) gets only the notes, which is new in Q3. The workspace manifest
#     records how many files were left out, and the viewer says so.
#
# The agents ran in a sandbox on a shared cluster, so a cluster path in their tool output belongs
# to someone else's job. Lines that name one are left out (--hide-host-paths), on top of what every
# build leaves out (futuresim_trace_masks.py); the trace says how many lines were left out at each spot.
#
#   FSIM_Q3_RUNS   where the runs are      (default: the clean_runs_Q3v8 folder)
#   FSIM_Q3_OUT    where to write the data (default: futuresim/traces/data/q3)
#
# The day summaries get their segments, counts and forecasts from build_futuresim_trace_summaries.py
# (rule-based, as for Q1) and their day titles and segment labels from scripts/futuresim_q3_summary_text/,
# which a language model wrote from a digest of each day (futuresim_trace_summary_text.py). That
# text is only put on a run whose segments are still the ones it was written for. If the traces
# change, the last step says which runs kept their rule-based text, and the text is to be redone.
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

add_run "Gemini 4 Carbon" gemini-4-carbon gemini-4-carbon-high Antigravity r00 "$q3_runs/agy_aljazeera2026Q3v8_gemini4carbon_high_exa_r00/26-11-16-02-42-54" agy_conversations
add_run "Gemini 4 Carbon" gemini-4-carbon gemini-4-carbon-high Antigravity r01 "$q3_runs/agy_aljazeera2026Q3v8_gemini4carbon_high_exa_r01/26-11-16-11-33-54" agy_conversations

add_run "Gemini 4 Neon" gemini-4-neon gemini-4-neon-xhigh Antigravity r00 "$q3_runs/agy_aljazeera2026Q3v8_gemini4neon_xhigh_exa_r00/26-11-19-16-15-28" agy_conversations
add_run "Gemini 4 Neon" gemini-4-neon gemini-4-neon-xhigh Antigravity r01 "$q3_runs/agy_aljazeera2026Q3v8_gemini4neon_xhigh_exa_r01/26-11-19-16-15-30" agy_conversations

# Both runs were started in the same second, so their folders have the same name; the trace builder
# tells them apart by adding the seed to the run id.
add_run "Inkling 2 Small" inkling-2-small inkling-2-small "Claude Code" r00 "$q3_runs/claude_code_aljazeera2026Q3v8_inkling2small_tinker_exa_r00/26-11-16-16-51-30" claude_code_stdout.jsonl
add_run "Inkling 2 Small" inkling-2-small inkling-2-small "Claude Code" r01 "$q3_runs/claude_code_aljazeera2026Q3v8_inkling2small_tinker_exa_r01/26-11-16-16-51-30" claude_code_stdout.jsonl

python3 "$repo/scripts/build_futuresim_trace_viewer_data.py" --output "$out" --max-string-chars 10000 --gzip --hide-host-paths "${args[@]}"
python3 "$repo/scripts/build_futuresim_workspace_data.py" --data-dir "$out" --workspace-root "$q3_runs" --root-first --max-data-bytes 10000000
# Each run's tokens (in total and per day) and wall-clock time, from the harnesses' session logs.
python3 "$repo/scripts/build_futuresim_run_usage.py" --data-dir "$out" --runs-root "$q3_runs"
# Every run has the same market.csv (question titles and resolved answers).
python3 "$repo/scripts/build_futuresim_trace_summaries.py" --data-dir "$out" --overwrite --join-short \
  --market-csv "$q3_runs/muse_aljazeera2026Q3v8_wonderfull_max_exa_r00/26-11-14-15-31-51/market.csv"
python3 "$repo/scripts/futuresim_trace_summary_text.py" apply --data-dir "$out" --text "$repo/scripts/futuresim_q3_summary_text"
