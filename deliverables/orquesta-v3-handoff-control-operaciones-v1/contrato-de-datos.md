# Contrato de datos · Control operativo y reporting → Operaciones v1

## Objetivo
Definir qué datos pasan de Control a Operaciones y cuáles nacen ya dentro de la capa operativa.

## Datos mínimos que deben pasar desde Control
- client_id
- referencia a lead_id si existe
- nombre de cliente o empresa
- responsable interno actual
- estado actual del caso
- prioridad
- bloqueos activos
- incidencias abiertas
- siguiente paso recomendado
- fecha de última actualización
- notas operativas relevantes

## Datos que pueden pasar si existen
- fecha objetivo
- nivel de urgencia
- área o línea de servicio implicada
- dependencias ya detectadas
- handoff previo desde onboarding

## Datos que nacen en Operaciones
- operation_id
- tarea_id o tareas iniciales
- responsable operativo
- estado operativo
- fecha de inicio operativo
- dependencias internas de ejecución
- cierre parcial o cierre final
- log de avance operativo

## Regla de datos
- pasar suficiente contexto para ejecutar sin rehacer análisis
- no inundar Operaciones con ruido de seguimiento irrelevante
- sí trasladar bloqueos, prioridad y siguiente paso útil

## Identificador recomendado
Debe existir un identificador común o enlazable entre:
- registro de control
- registro de operaciones

Opciones mínimas viables:
- `client_id` como clave principal
- `client_id` + `operation_id` como relación operativa
- referencia cruzada control-operaciones como fallback visible

## Regla de calidad
Si un caso entra en operaciones sin contexto suficiente, debe marcarse como `contexto_incompleto` y requerir revisión humana antes de seguir automatizando.
