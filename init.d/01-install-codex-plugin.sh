#!/usr/bin/env bash
if [ -n "$CODEX_HOME" ]; then
  mkdir -p "$CODEX_HOME"
fi
codex plugin marketplace add https://github.com/openai/plugins
codex plugin add build-web-data-visualization@openai-curated
