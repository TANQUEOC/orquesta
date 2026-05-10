# Referencia reusable · Handoff Control → Operaciones

## Trigger canónico
- `control.status = listo_para_operar`
  o
- `control.status = prioridad_alta` con criterio operativo válido

## Acción esperada
- crear o activar `operaciones.status = operacion_abierta`

## Datos mínimos que deben pasar
- `client_id`
- `lead_id` si existe
- cliente o empresa
- responsable interno actual
- prioridad
- bloqueos activos
- incidencias abiertas
- siguiente paso recomendado
- fecha de última actualización
- notas operativas relevantes

## Qué debe ocurrir después
- crear o actualizar `operaciones_activas`
- generar una tarea inicial
- registrar trazabilidad en `seguimiento_operativo`
- dejar visible responsable, bloqueo y prioridad

## Regla de continuidad
No debe existir un caso `listo_para_operar` sin una de estas dos cosas:
- operación abierta
- excepción humana registrada

## Fuente principal
- `projects/orquesta/deliverables/orquesta-v3-handoff-control-operaciones-v1/`
