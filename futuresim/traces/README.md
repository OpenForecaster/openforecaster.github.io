# FutureSim Trace Viewer

Static viewer for official FutureSim leaderboard traces.

The deployed page currently loads `manifest.json`, then a single
`{agent}/{run}/{simulation_day}.json` shard from the static files checked into
`futuresim/traces/data/`. Those files are generated from
`/fast/sgoel/forecasting/current_sim/official_runs_complete` by
`scripts/build_futuresim_official_trace_data.sh`.

The raw legacy trajectory browser is linked from the page header through
`window.FSIM_RAW_TRACE_URL` in `config.js`.

The FutureSim landing page leaderboard reads `data/leaderboard.json`. This file
is precomputed by `scripts/build_futuresim_leaderboard_data.py` from the same
official runs, using daily per-question prediction snapshots and matcher cache
files to bootstrap over both seeds and question IDs. When adding or replacing a
model/run in the trace visualizer, rerun:

```bash
scripts/build_futuresim_official_trace_data.sh
```

This refreshes both the trace shards/manifest and the bootstrapped
`leaderboard.json`. GitHub Pages is static, so the deployed visualizer reads the
JSON committed to this repo unless `window.FSIM_TRACE_DATA_BASE` is explicitly
changed to point at another static host.

Example local sample generation:

```bash
python scripts/build_futuresim_trace_viewer_data.py \
  --output futuresim/traces/data \
  --max-days 1 \
  --max-events-per-day 160 \
  --run 'Fable 5|fable-5|claude-fable-5|Claude Code|r00|/fast/sgoel/forecasting/current_sim/final_runs_v37/claude_code_aljazeeraQ12026v37_fable5_activemem2_r00_restart/26-06-12-12-16-48/agents/minimalHarness_claude-fable-5_001/claude_code_stdout.jsonl'
```

For deployment, generate without `--max-days` / `--max-events-per-day`, upload
the output directory, and set `window.FSIM_TRACE_DATA_BASE` in `config.js`.
