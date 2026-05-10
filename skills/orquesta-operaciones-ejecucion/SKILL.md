---
name: orquesta-operaciones-ejecucion
description: Diseña y mejora la capa real de operaciones de ORQUESTA: activación de trabajo desde control, tareas, responsables, dependencias, bloqueos operativos, handoffs internos, seguimiento de ejecución y cierre de operaciones o servicios.
---

# Orquesta Operaciones Ejecución

## Para qué existe
Esta skill convierte casos activos y priorizados en trabajo real ejecutable.

No sirve para hablar en abstracto de procesos.
Sirve para ordenar la ejecución diaria de un servicio, operación o flujo interno con responsables, tareas, dependencias, bloqueos y cierre.

## Cuándo usarla
Actívala cuando el usuario pida algo como:

- organizar la operación diaria
- convertir casos activos en trabajo real
- repartir tareas y responsables
- ordenar dependencias entre personas o equipos
- evitar trabajo perdido entre fases
- registrar avance, bloqueo y cierre
- crear una mecánica operativa mínima pero seria

## Qué resuelve
Diseña una capa de operaciones con estas piezas:

1. entrada de trabajo desde control
2. operaciones activas
3. tareas o unidades de ejecución
4. responsables
5. dependencias
6. bloqueos operativos
7. seguimiento de avance
8. cierre y validación

## Entradas mínimas
Si faltan, pide solo esto:

- qué tipo de trabajo entra en operaciones
- quién ejecuta o supervisa
- qué estados necesita la ejecución
- qué bloqueos son habituales
- qué significa “terminado” en ese contexto

## Método de trabajo

### 1. Define la unidad operativa
Aclara qué se mueve realmente en operaciones:
- tarea
- caso
- entrega
- servicio
- incidencia
- lote de trabajo

### 2. Mapea el flujo de ejecución
Ordena el recorrido real:
- trigger de entrada
- creación de operación
- asignación de responsable
- ejecución
- bloqueo si aplica
- validación
- cierre

### 3. Detecta fricciones
Busca especialmente:
- tareas sin dueño
- dependencias invisibles
- trabajo que entra sin contexto suficiente
- bloqueos no registrados
- cierres sin criterio claro
- handoffs internos confusos

### 4. Diseña el flujo objetivo
Cada paso debe incluir:
- trigger
- acción
- sistema
- responsable
- plazo o SLA si aplica
- criterio de completado

### 5. Define la capa de control mínima
Incluye siempre:
- estados operativos
- responsables
- prioridad
- dependencias
- bloqueos
- trazabilidad de avance
- criterio de cierre

## Salidas esperadas
Cuando uses esta skill, entrega normalmente:

1. definición de unidad operativa
2. flujo de ejecución propuesto
3. estados y responsables
4. automatizaciones prioritarias
5. estructura de seguimiento
6. bloqueos típicos y tratamiento
7. riesgos operativos
8. siguiente paso de implantación

## KPIs base
Usa los que encajen:

- operaciones activas
- tareas abiertas
- tareas bloqueadas
- tiempo hasta cierre
- handoffs pendientes
- operaciones cerradas por periodo
- bloqueos por tipo
- carga por responsable

## Cuándo leer referencias
- Lee `references/operaciones-v1-reference.md` cuando el trabajo deba apoyarse en el sprint de Operaciones ya paquetizado o en la cadena maestra de ORQUESTA.
- Lee `references/control-to-operaciones-handoff.md` cuando el caso esté justo en la unión entre Control y Operaciones.

## Reglas
- No confundas operaciones con control o reporting.
- No conviertas una operación en una simple lista de tareas sin flujo.
- No dejes responsables implícitos.
- Toda operación seria necesita criterio de cierre y trazabilidad.
- Si el trabajo entra desde control, no rehagas contexto desde cero: arrastra prioridad, bloqueos e incidencias relevantes.

## Formato de salida
Responde con mentalidad de operaciones reales.

Prioriza:
- flujo
- responsables
- estados
- bloqueos
- handoffs
- quick wins
- siguiente paso concreto
