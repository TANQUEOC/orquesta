# Flujo técnico · Control operativo y reporting → Operaciones v1

## Objetivo
Definir cómo se implementa técnicamente el handoff con el stack pragmático actual de ORQUESTA.

## Stack
- Google Sheets
- Gmail
- n8n

## Modelo mínimo recomendado
### Áreas o pestañas principales
- `clientes_activos`
- `incidencias`
- `bloqueos`
- `seguimiento`
- `operaciones_activas`
- `tareas`
- `dependencias`
- `bloqueos_operativos`
- `seguimiento_operativo`

## Secuencia técnica recomendada
1. Control registra y actualiza el caso en `clientes_activos`
2. el caso cambia a `listo_para_operar`
3. n8n detecta ese cambio de estado
4. n8n valida que no exista operación activa duplicada
5. n8n crea o actualiza la fila en `operaciones_activas`
6. n8n genera una o varias tareas base en `tareas`
7. n8n copia prioridad, bloqueos e incidencias relevantes
8. n8n registra el evento en `seguimiento_operativo`
9. n8n avisa internamente al responsable si aplica

## Trigger recomendado en n8n
### Evento base
- cambio o lectura periódica de filas en `clientes_activos`
- filtro por `status = listo_para_operar`

### Condiciones mínimas antes de crear o activar operación
- client_id o identificador equivalente disponible
- responsable interno u operativo definido o marcado como pendiente
- no existir ya operación abierta duplicada
- contexto mínimo de ejecución presente

## Acciones mínimas del flujo
- crear o actualizar fila en `operaciones_activas`
- asignar `operacion_abierta`
- generar tarea inicial
- guardar referencia cruzada con control
- registrar evento en `seguimiento_operativo`
- generar aviso interno si hay bloqueo o prioridad alta

## Protección anti-duplicado
Debe existir una de estas protecciones:
- campo `operation_created = yes`
- validación por `client_id`
- validación por referencia cruzada control-operaciones
- tabla o pestaña de logs de activación operativa

## Supervisión humana
Aunque el handoff sea automático, debe haber revisión humana al menos en:
- calidad del contexto transferido
- prioridades altas o casos sensibles
- definición de responsable operativo
- bloqueos que impiden arrancar

## Resultado esperado
Cuando un caso ya está listo para operar, no debe quedarse en observación.
Debe entrar automáticamente en operaciones con una unidad de ejecución visible y trazable.
