#!/bin/bash
AUTH_FILE="$HOME/.local/share/opencode/auth.json"
TOKEN=$(jq -r '.anthropic.access // .claude.access // empty' "$AUTH_FILE" 2>/dev/null)

if [[ -z "$TOKEN" ]]; then
  echo "NO_TOKEN"
  exit 0
fi

curl -s "https://api.anthropic.com/api/oauth/usage" -H "Authorization: Bearer $TOKEN" 2>/dev/null || echo "OFFLINE"
