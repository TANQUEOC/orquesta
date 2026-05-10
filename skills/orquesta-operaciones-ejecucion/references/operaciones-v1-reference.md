# Referencia reusable · Operaciones v1

## Qué ancla esta referencia
Resume la capa de Operaciones ya definida en ORQUESTA para que la skill no parta desde cero.

## Idea central
Operaciones convierte casos activos y priorizados en trabajo real ejecutable.

La secuencia base es:
- entrada desde control
- creación de operación activa
- generación de tareas
- asignación de responsables
- gestión de dependencias y bloqueos
- seguimiento
- cierre

## Estados útiles
- `operacion_abierta`
- `tarea_inicial_creada`
- `en_ejecucion`
- `bloqueada`
- `pendiente_validacion`
- `cerrada`

## Pestañas o áreas mínimas recomendadas
- `operaciones_activas`
- `tareas`
- `dependencias`
- `bloqueos_operativos`
- `seguimiento_operativo`
- `catalogos`

## Regla de diseño
Operaciones no debe quedarse en observación ni convertirse en una lista plana.
Debe convertir prioridad y contexto en ejecución trazable.

## Fuente principal
- `projects/orquesta/deliverables/orquesta-v3-sprint-operaciones-v1/`
- `projects/orquesta/deliverables/orquesta-v3-cadena-maestra-captacion-onboarding-control-operaciones-v1.md`
