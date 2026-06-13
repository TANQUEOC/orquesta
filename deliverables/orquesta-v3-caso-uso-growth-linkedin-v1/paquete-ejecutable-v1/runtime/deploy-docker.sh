#!/usr/bin/env bash
set -euo pipefail

cd "$(dirname "$0")"

if [ ! -f .env ]; then
  cp .env.example .env
  echo "Se ha creado .env desde .env.example. Rellena SUPABASE_SERVICE_ROLE_KEY antes del despliegue."
fi

docker compose up -d --build

echo "Runtime desplegado en http://127.0.0.1:8010"
