#!/usr/bin/env bash
# Serve MiniCPM5-2B-Math with llama.cpp (Apple Silicon, CPU, or GPU).
# Needs llama.cpp b9833 or newer (b9354 added the MiniCPM5 tokenizer, b9833 its chat parser); tested with b10964.
#
# -np sets parallel slots (agents decoding at once); -kvu lets them share one KV cache of -c tokens.
# Measured on an Apple M5 (16 GB) with Q8_0: about 46 tok/s for one stream, about 125 tok/s total with 4 slots.
set -euo pipefail
REPO="${REPO:-Caldalis/MiniCPM5-2B-Math-GGUF}"
QUANT="${QUANT:-Q8_0}"          # Q4_K_M | Q8_0 | BF16
PORT="${PORT:-8000}"
exec llama-server -hf "$REPO:$QUANT" -a MiniCPM5-2B-Math \
  --jinja -ngl 99 \
  -c "${CTX:-98304}" -np "${SLOTS:-4}" -kvu \
  --port "$PORT" "$@"
