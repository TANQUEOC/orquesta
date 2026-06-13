#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Se ha creado .env desde .env.example. Revísalo antes de seguir."
fi

uvicorn app.main:app --host 0.0.0.0 --port 8010
