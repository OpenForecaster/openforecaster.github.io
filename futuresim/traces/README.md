# FutureSim Trace Viewer

Static viewer for official FutureSim leaderboard traces.

The deployed page defaults to 2026 Q3 and can switch between three static data
roots:

- 2026 Q3: `futuresim/traces/data/q3/`
- 2026 Q2: `futuresim/traces/data/q2/`
- 2026 Q1: `futuresim/traces/data/`

Each root contains a manifest, per-day raw trace shards, workspace history, and
summary overlays. The day shards are gzip-compressed
(`runs/<agent>/<run>/<date>.json.gz`) and the viewer decompresses them in the
browser. Q1 is generated from `official_runs_complete` with
`scripts/build_futuresim_official_trace_data.sh`. Q3 is generated from the 18
leaderboard runs in `clean_runs_Q3v8` with:

```bash
scripts/build_futuresim_q3_trace_data.sh
```

That one script writes the shards, the workspaces and the summaries. Q3 starts
on `2026-06-24` and caps raw text fields at 10,000 characters, as Q2 does. It
differs from Q1 and Q2 in seven ways:

- Codex, Muse and Antigravity runs are read from their session logs
  (`codex_sessions/`, `muse_sessions/`, `agy_conversations/`) by
  `scripts/futuresim_session_logs.py`, not from stdout. Their sub-agents make
  many of the forecasts and stdout does not have them. Each event from a
  sub-agent carries its name in `subagent`. Codex stores the text of messages
  between agents encrypted, so the viewer shows a placeholder for those.
  Antigravity (Gemini) calls are shown the way the other harnesses' are: a
  call to the forecast server as that tool, a shell command as Bash, and the
  result of a command that finished in the background with the call that
  started it.
- A run's id is the name of its timestamp folder. The two Inkling 2 Small runs
  were started in the same second, so their ids also carry the seed
  (`26-11-16-16-51-30-r00`). Each run's entry in the manifest records its
  folder as `source_run`, which is how the workspace export finds it.
- A run whose `memory/` folder holds more than 10 MB of files other than
  Markdown notes (search dumps, article scans) is exported with its notes and
  predictions only. Its workspace manifest records the count and size under
  `data_files_left_out`, and the viewer shows that next to the file count.
- Each run's entry in the manifest has `tokens`: the input, cached-input and
  output tokens of the run's own agent (`main`), of the agents it started
  (`subagents`) and of the model calls the harness made by itself (`other`,
  which is Muse's reminder sessions). Codex and Muse runs also have
  `reasoning_output`, the part of the output that was reasoning; the other
  harnesses do not log it. Each day of a run has `tokens` too, summed over the
  three, for the model calls made while that simulation day was open. The
  run's `model_calls` says how many requests to the model each of the three
  made, the ones that compact the context included. Claude Code logs such a
  request as a marker without its tokens and reports them only in the total a
  process prints when it exits. Three runs had compactions in a process that
  was stopped before that (Claude Opus 5.5 r00 and r01, Inkling 2 Small r00):
  their `tokens` leave those compactions out, and `uncounted_compactions` says
  how many they are and how many tokens of context they summarised.
  `scripts/build_futuresim_run_usage.py` reads all of it from the session logs
  (for Claude Code, `claude_config/projects/`) the way
  `analysis/src/q3_v8_output_tokens.py` in the simulator's repository counts
  output tokens, and its header says what each number includes. The viewer
  shows the totals and the model calls under Run Activity, a day's tokens in
  the day's header, and output tokens per day as a third metric of the
  trajectory chart. Q1 and Q2 have no token counts, because only stdout was
  kept for those runs: Codex's reports the usage of the first turn only, and
  Claude Code's carries the output count from the start of each message, not
  its end.
- Each run's entry also has `wall_clock`, from the same script: `seconds` is
  the time from the run's first log record to its last, without the gap before
  each restart. Five runs were interrupted and restarted in a new session (GPT
  6.1 Sol r00 and r01 twice, DeepSeek V4.1 Flash 1017 r00, r01 and r02 once).
  Their folders hold nothing between the last record before a restart and the
  restart's first record, when the run was stopped or doing work on a day that
  the restart redid, so that gap is not counted; `restarts` and
  `restart_wait_seconds` say how many there were and how long. No run is
  silent for more than seven minutes anywhere else.
- The agents ran in a sandbox (`/agent/workspace`) on a shared cluster, so a
  cluster path in their tool output belongs to someone else's job. The build
  passes `--hide-host-paths`: a line of tool output that names a cluster path
  (`/lustre/…`, `/fast/…`, `/is/cluster/…`, `/scratch/…`, `/home/<account>/…`)
  is replaced by a note saying how many lines were left out. Do not use this
  option for Q1 or Q2, whose agents worked directly in a cluster folder.
- The summaries get their segments, counts and sample forecasts from
  `scripts/build_futuresim_trace_summaries.py`, as for Q1, run with
  `--join-short`. A segment ends where the acting agent changes, a sub-agent's
  segments are labelled with its name, and a stretch of up to three entries
  with no research or forecasts (a hand-off to a sub-agent, a closing remark)
  is folded into its neighbour. The day titles and segment labels, which are
  what the viewer shows, were then written by a language model from a digest of
  each day. They are kept in `scripts/futuresim_q3_summary_text/`, one file per
  run, and the build script puts them on a run only if its segments are still
  the ones the text was written for.

To redo the Q3 titles and labels after the traces change:

```bash
python3 scripts/futuresim_trace_summary_text.py digest \
  --data-dir futuresim/traces/data/q3 --market-csv <run>/market.csv --out <digests>
# have a model write one JSONL line per day into <text>, as the script's header describes
python3 scripts/futuresim_trace_summary_text.py apply \
  --data-dir futuresim/traces/data/q3 --text <text> --keep scripts/futuresim_q3_summary_text
```

Q2 is generated from the 19 selected `Q2results` runs with:

```bash
scripts/build_futuresim_q2_trace_data.sh
```

Q2 starts on `2026-03-25`; keep that explicit start date when regenerating
Codex shards because those stdout records do not carry reliable day-transition
dates. Q2 raw text fields are capped at 10,000 characters so the published site
stays below GitHub Pages' 1 GB limit. After generating new summary overlays, place them in
`data/q2/summaries/`, align their dates and `trace_path` values with the Q2
manifest, and refresh `data/q2/summaries/index.json`.

With all three periods the built site is about 382 MB, of which the day shards
are 274 MB (Q1 60, Q2 116, Q3 98). GitHub Pages allows 1 GB, which its deploy
step counts as 1,073,741,824 bytes. Check the size of a Jekyll build before
adding more trace data.

Q1 and Q2 were first published with plain JSON shards (260 MB and 549 MB). They
were compressed in place with `scripts/gzip_futuresim_trace_shards.py`, which
renames each shard in the manifest and in the summaries' `trace_path` and
changes nothing else, and their build scripts pass `--gzip` since then. The
viewer tells a compressed shard by its first two bytes, not by its name, so it
also reads plain JSON from another data host.

Every build leaves four things out of the traces. The rules are in
`scripts/futuresim_trace_masks.py`:

- A listing of the job's environment variables (`env`, `printenv`) is left out
  whole.
- The rows of a process listing (`ps`, `pgrep`, `top`) are left out. On a
  shared node they are mostly other people's jobs, and the agent's own rows
  cannot be told apart from them, so those go too.
- A line of tool output that names the cluster's file server (its address, in
  `df` or `mount`) is left out.
- A home folder on someone's own computer loses the name: `/Users/<name>/…`
  becomes `/Users/[redacted]/…`, in commands and messages as well as in output.

A note such as `[18 lines left out: processes on the shared cluster]` stands
where lines were left out. The published shards were built before these rules
existed, and `scripts/mask_futuresim_trace_shards.py` applied them in place (20
events in 14 shards). Run it without `--write` to list what a new rule would
change in published data.

The "Download trace" button beside the run selector saves the selected run as
one zip (`futuresim-<period>-<agent>-<seed>.zip`): a `README.txt`, `run.json`
(the run's entry in the manifest, without `workspace`) and `days/<date>.json`
for every day. The viewer builds the zip in the browser from the day shards,
because a second copy of every run would not fit the size limit. A gzip shard's
deflate stream, CRC and length are what a zip entry stores, so each shard goes
in as it is and nothing is unpacked or recompressed. That relies on a shard
being a single gzip member, which is how the build scripts write them. The
largest run is 36 MB zipped (GPT 5.6 Sol r00 in Q2, 170 MB unpacked). The
workspace files are not in the zip.

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

This refreshes the trace shards/manifest, the `workspaces/` memory and
prediction exports, and the bootstrapped `leaderboard.json`. GitHub Pages is
static, so the deployed visualizer reads the JSON committed to this repo unless
`window.FSIM_TRACE_DATA_BASE` is explicitly changed to point at another static
host.

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
