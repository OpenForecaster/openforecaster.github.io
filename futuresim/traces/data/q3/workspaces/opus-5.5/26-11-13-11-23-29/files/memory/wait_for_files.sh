#!/bin/bash
# usage: wait_for_files.sh <max_seconds> ; waits until all 19 batch forecasts json exist or timeout
max=${1:-540}
start=$(date +%s)
while true; do
  n=$(ls /agent/workspace/memory/batches/batch_*_forecasts.json 2>/dev/null | wc -l)
  now=$(date +%s)
  if [ "$n" -ge 19 ]; then echo "ALL DONE ($n files) after $((now-start))s"; break; fi
  if [ $((now-start)) -ge $max ]; then echo "TIMEOUT: $n files after $((now-start))s"; ls /agent/workspace/memory/batches/ | grep forecasts; break; fi
  sleep 15
done
