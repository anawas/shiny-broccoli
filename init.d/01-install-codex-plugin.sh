#!/usr/bin/env bash
codex plugin marketplace add https://github.com/openai/plugins
if [ -n "$CODEX_HOME" ]; then
  mkdir -p "$CODEX_HOME"
fi
codex plugin add build-web-data-visualization@openai-curated
