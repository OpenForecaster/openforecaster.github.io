#!/usr/bin/env python3
"""Apply the trace masks to day shards that are already published.

  mask_futuresim_trace_shards.py futuresim/traces/data futuresim/traces/data/q2 futuresim/traces/data/q3
  mask_futuresim_trace_shards.py --write futuresim/traces/data futuresim/traces/data/q2 futuresim/traces/data/q3

build_futuresim_trace_viewer_data.py applies futuresim_trace_masks.py to every event it writes.
This script applies the same masks to shards that were built before a mask existed, so a period
does not have to be rebuilt from its run folders. Without --write it only lists what would change.

A shard that changes is written the way the builder writes it, and the others are not touched.
The manifest and the summaries hold counts of events and tool calls, which the masks do not
change. Lines that name a path on the shared cluster are not looked for here: that is the
builder's --hide-host-paths, a choice made for each period when it is built.
"""
import argparse
import gzip
import json
import sys
from multiprocessing import Pool
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_futuresim_trace_viewer_data import preview_from_blocks, write_json  # noqa: E402
from futuresim_trace_masks import mask_blocks, without_home_names  # noqa: E402


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("data_dir", type=Path, nargs="+", help="A folder with a manifest.json and its runs/.")
    parser.add_argument("--write", action="store_true", help="Rewrite the shards that change.")
    args = parser.parse_args()
    jobs = []
    for data in args.data_dir:
        data = data.resolve()
        for run in json.loads((data / "manifest.json").read_bytes())["runs"]:
            jobs.append((data, [day["path"] for day in run["days"]], args.write))
    shards = events = 0
    with Pool() as pool:
        for changed in pool.imap(mask_run, jobs):
            for path, indexes in changed:
                print(f"{path}: events {', '.join(map(str, indexes))}")
                shards += 1
                events += len(indexes)
    print(f"{events} events in {shards} day shards {'rewritten' if args.write else 'would change'}")


def mask_run(job):
    """Mask one run's shards, in the order of its days. Returns each changed shard with its events' idx."""
    data, paths, write = job
    process_calls = {}
    changed = []
    for path in paths:
        shard = data / path
        payload = json.loads(gzip.decompress(shard.read_bytes()))
        indexes = []
        for event in payload["events"]:
            before = json.dumps(event["blocks"], ensure_ascii=False)
            # The builder adds earlier outcomes to a forecast call after it has written the preview.
            derived = event["preview"] == preview_from_blocks(event["blocks"])
            mask_blocks(event["blocks"], process_calls)
            if json.dumps(event["blocks"], ensure_ascii=False) == before:
                continue
            event["preview"] = preview_from_blocks(event["blocks"]) if derived else without_home_names(event["preview"])
            indexes.append(event["idx"])
        if not indexes:
            continue
        if write:
            write_json(shard, payload, gzipped=True)
            if json.loads(gzip.decompress(shard.read_bytes())) != payload:
                raise SystemExit(f"{shard} does not read back as written")
        changed.append((str(shard), indexes))
    return changed


if __name__ == "__main__":
    main()
