#!/usr/bin/env bash
# Sandboxed checker runner: no network, read-only filesystem, resource-capped.
# Usage: ./run-checker.sh your_submission.json [IMAGE]
# IMAGE defaults to the digest-pinned image in the live task description.
set -euo pipefail
SUB="${1:?usage: run-checker.sh submission.json [image]}"
IMAGE="${2:-ghcr.io/math-market/no-isosceles-checker:latest}"
exec docker run --rm \
  --network none \
  --read-only \
  --memory 512m --cpus 1 --pids-limit 64 \
  --security-opt no-new-privileges \
  --cap-drop ALL \
  -v "$(cd "$(dirname "$SUB")" && pwd)/$(basename "$SUB"):/data/sub.json:ro" \
  "$IMAGE" /data/sub.json
