# Integración de la pantalla `Campaña publicitaria en redes sociales`

## Pantalla fuente
- `deliverables/orquesta-v3-campana-publicitaria-redes-sociales-v1.html`

## Runtime mínimo asociado
- `apps/linkedin-growth-campaign/`

## Acción del botón `Lanzar ejecución`
Debe hacer `POST` a:
- `/campaigns/launch`

## Acción del botón `Previsualizar lote`
Debe hacer `POST` a:
- `/campaigns/preview`

## Mapeo de campos UI -> payload
- `prompt` -> `prompt`
- `periodicidad` -> `periodicity`
- `cantidad` -> `publication_count`
- `inicio` -> `start_date`
- `hora` -> `preferred_time`
- `canal` -> `channel`
- `tono` -> `tone`
- `modo de imagen` -> `image_mode`
- `instrucciones adicionales` -> `extra_instructions`
- `approval gate` -> `require_approval`

## Payload esperado mínimo
```json
{
  "prompt": "Quiero una campaña...",
  "periodicity": "2_per_week",
  "publication_count": 8,
  "channel": "linkedin",
  "language_code": "es",
  "tone": "profesional cercano",
  "style": "claro y útil",
  "start_date": "2026-06-16",
  "preferred_time": "09:00",
  "image_mode": "auto",
  "require_approval": true,
  "extra_instructions": "CTA a diagnóstico",
  "creator": "luis"
}
```

## Respuesta esperada del launch
- resumen de campaña
- publicaciones generadas
- número de piezas creadas
- si hubo o no persistencia real en Supabase

## Bloqueo actual
Sin `SUPABASE_SERVICE_ROLE_KEY`, el runtime genera preview pero no persiste aún en la base ORQUESTA.
