#!/usr/bin/env bash
# Sandboxed checker runner: no network, read-only filesystem, resource-capped.
# Usage: ./run-checker.sh your_submission.json [IMAGE]
# IMAGE defaults to the locally-built tag: docker build -t noiso-checker .
set -euo pipefail
SUB="${1:?usage: run-checker.sh submission.json [image]}"
IMAGE="${2:-noiso-checker}"
exec docker run --rm \
  --network none \
  --read-only \
  --memory 512m --cpus 1 --pids-limit 64 \
  --security-opt no-new-privileges \
  --cap-drop ALL \
  -v "$(cd "$(dirname "$SUB")" && pwd)/$(basename "$SUB"):/data/sub.json:ro" \
  "$IMAGE" /data/sub.json
