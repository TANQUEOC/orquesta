# ORQUESTA · LinkedIn Growth Campaign

Runtime mínimo para la pieza **Campaña publicitaria automática de Growth LinkedIn**.

## Qué hace esta app
- recibe un prompt de campaña
- normaliza parámetros
- genera un lote editorial inicial
- calcula calendario básico
- persiste campañas y publicaciones en Supabase ORQUESTA
- deja preparada la frontera técnica para LinkedIn real

## Estado
Runtime desplegable de v1. Aún no publica en LinkedIn real porque faltan credenciales/permisos del canal.

## Endpoints
- `GET /`
- `GET /health`
- `GET /runtime/meta`
- `GET /linkedin/status`
- `POST /campaigns/preview`
- `POST /campaigns/launch`

## Arranque local simple
```bash
cd apps/linkedin-growth-campaign
cp .env.example .env
# rellena SUPABASE_SERVICE_ROLE_KEY
bash run-local.sh
```

## Despliegue con Docker
```bash
cd apps/linkedin-growth-campaign
cp .env.example .env
# rellena SUPABASE_SERVICE_ROLE_KEY
bash deploy-docker.sh
```

## Configuración importante
- `SUPABASE_URL=https://rxuknfjovwvqrlxzyxye.supabase.co`
- `SUPABASE_SERVICE_ROLE_KEY=...`
- `CORS_ORIGINS=["*"]` o lista cerrada si ya conoces el origen real
- `RUNTIME_PUBLIC_BASE_URL=http://127.0.0.1:8010`

## Relación con ORQUESTA
Esta app es el runtime de la pieza visual:
- `deliverables/orquesta-v3-campana-publicitaria-redes-sociales-v1.html`

Y usa como base funcional/documental:
- `deliverables/orquesta-v3-caso-uso-growth-linkedin-v1/`
