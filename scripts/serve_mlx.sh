#!/usr/bin/env bash
# Serve MiniCPM5-2B-Math with MLX-LM on Apple Silicon (pip install mlx-lm; tested with mlx-lm 0.32.0 on an M5).
# For several agents at once, llama.cpp with parallel slots (serve_llamacpp.sh) is usually faster on a laptop.
set -euo pipefail
MODEL="${MODEL:-Caldalis/MiniCPM5-2B-Math}"
PORT="${PORT:-8000}"
exec mlx_lm.server --model "$MODEL" --port "$PORT" "$@"
