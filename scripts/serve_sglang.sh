#!/usr/bin/env bash
# Serve MiniCPM5-2B-Math with SGLang (>= 0.5.16) on an NVIDIA GPU.
set -euo pipefail
MODEL="${MODEL:-Caldalis/MiniCPM5-2B-Math}"
PORT="${PORT:-8000}"
exec python -m sglang.launch_server \
  --model-path "$MODEL" \
  --served-model-name MiniCPM5-2B-Math \
  --context-length 131072 \
  --port "$PORT" "$@"
