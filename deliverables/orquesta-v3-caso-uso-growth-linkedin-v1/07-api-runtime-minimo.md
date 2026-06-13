# 07 · API runtime mínimo

## Objetivo
Cerrar la pieza LinkedIn como sistema ejecutable mínimo, no solo como documentación o pantalla.

## Runtime creado
- `apps/linkedin-growth-campaign/`

## Endpoints
### `GET /health`
Valida que el servicio está vivo.

### `POST /campaigns/preview`
Recibe el payload de campaña y devuelve:
- prompt normalizado
- resumen
- publicaciones propuestas
- fechas calculadas

### `POST /campaigns/launch`
Hace lo mismo que preview y además intenta persistencia.

## Comportamiento actual
- genera lote editorial inicial
- calcula calendario básico
- marca estados iniciales
- deja preparada la capa de persistencia
- todavía no escribe en Supabase por falta de credencial activa

## Siguiente salto técnico
Implementar persistencia real en `persist_campaign()` contra el proyecto Supabase ORQUESTA:
- `https://rxuknfjovwvqrlxzyxye.supabase.co`
