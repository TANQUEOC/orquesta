#!/usr/bin/env bash
curl -sS http://127.0.0.1:8010/campaigns/launch \
  -H 'Content-Type: application/json' \
  -d @examples/sample_campaign_payload.json
