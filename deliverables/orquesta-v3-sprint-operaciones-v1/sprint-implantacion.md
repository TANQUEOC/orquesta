# ORQUESTA v3 · Sprint de implantación real · Operaciones v1

## Propósito
Este sprint existe para convertir el pilar de Operaciones en una capacidad operativa real de ORQUESTA.

No se trata de seguir describiendo procesos en abstracto.
Se trata de dejar una primera mecánica de ejecución funcionando con tareas, responsables, dependencias, handoffs y cierre.

## Duración
5 días.

## Objetivo del sprint
Al terminar el sprint, la capa de operaciones debe poder:

- recibir trabajo desde control operativo
- convertir casos activos en trabajo ejecutable
- asignar responsables
- ordenar tareas y dependencias
- detectar bloqueos operativos
- registrar avance y cierre
- dejar trazabilidad mínima de ejecución
- preparar handoffs internos cuando corresponda

## Stack reutilizado
Se reutiliza la misma lógica y familia de herramientas que en Captación, Onboarding y Control:
- Google Sheets
- Gmail
- n8n
- soporte documental en Drive si hace falta

## Alcance del sprint por días

### Día 1 · Cierre del modelo operativo
#### Objetivo
Definir cómo se traduce un caso activo en trabajo real.

#### Trabajo
- definir tipos de tarea o unidad operativa
- definir responsables posibles
- definir estados operativos de ejecución
- definir dependencias típicas
- definir criterio de cierre y bloqueo

#### Entregable
- modelo operativo definido
- estados base definidos
- lógica de responsables y dependencias cerrada

### Día 2 · Montaje de la base operativa de ejecución
#### Objetivo
Dejar creada la base donde vive el trabajo operativo.

#### Trabajo
- crear hoja maestra o estructura base de operaciones
- montar pestañas recomendadas
- definir columnas y relaciones mínimas
- definir campos de estado, responsable, prioridad, fecha y dependencia

#### Tabs recomendadas
- `operaciones_activas`
- `tareas`
- `dependencias`
- `bloqueos_operativos`
- `seguimiento_operativo`
- `catalogos`

#### Entregable
- base operativa creada
- estructura mínima usable cerrada

### Día 3 · Automatización de entrada y handoffs
#### Objetivo
Dejar automatizada la entrada de trabajo desde control y los primeros handoffs internos.

#### Trabajo
- configurar workflows n8n para activar trabajo desde control
- crear tareas base a partir de casos activos
- registrar handoffs internos
- detectar bloqueos iniciales
- enviar avisos internos cuando haga falta

#### Entregable
- workflow base de operaciones
- entrada automática de trabajo funcionando
- trazabilidad inicial de handoffs activa

### Día 4 · Seguimiento de ejecución y cierre
#### Objetivo
Tener visibilidad mínima sobre el trabajo operativo real.

#### Trabajo
- crear vista de operaciones activas
- crear vista de tareas abiertas
- crear vista de bloqueos
- crear vista de responsables y cargas mínimas
- definir indicadores básicos de avance y cierre

#### Indicadores mínimos sugeridos
- operaciones activas
- tareas abiertas
- tareas bloqueadas
- cierres recientes
- handoffs pendientes

#### Entregable
- cuadro de seguimiento operativo base
- visibilidad mínima de ejecución

### Día 5 · Prueba real y cierre operativo
#### Objetivo
Validar la mecánica de operaciones con casos reales o simulados.

#### Trabajo
- probar activación de trabajo desde control
- probar creación de tareas
- probar cambio de estado y bloqueo
- probar cierre de tarea u operación
- revisar claridad del sistema
- corregir fallos
- documentar uso mínimo y backlog v2

#### Entregable
- capa de operaciones v1 validada
- incidencias corregidas
- criterio operativo documentado

## Definición de éxito
El sprint se considera bien cerrado cuando se puede:

- transformar un caso activo en trabajo real
- saber quién hace qué
- ver el estado de ejecución
- detectar bloqueos operativos
- registrar avances y cierres
- dejar continuidad entre control y operación

## Definición de no terminado
No debe considerarse implantado de verdad si:

- solo existe una lista de tareas sin flujo
- no hay responsables claros
- no hay prueba real o simulada
- no se distinguen tareas abiertas, bloqueadas y cerradas
- el trabajo sigue dependiendo de perseguirlo todo manualmente
