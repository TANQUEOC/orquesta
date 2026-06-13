# 04 · Modelo de datos lógico

## Objetivo
Definir la estructura mínima de datos para que el caso de uso del agente LinkedIn funcione como sistema gobernable y no solo como generador de texto.

## Principios
- separar publicación, estado, lotes y assets cuando aporte claridad
- dejar trazabilidad de cambios
- no acoplar toda la información al texto generado
- permitir aprobación humana y errores sin romper el flujo
- dejar preparada la futura integración real con LinkedIn

---

## Entidades principales

### 1. `linkedin_prompt_runs`
Representa la instrucción original del usuario y el lote editorial derivado.

Sirve para:
- guardar el prompt origen
- persistir parámetros extraídos
- relacionar varias publicaciones con una misma instrucción
- medir reutilización y calidad del input

### 2. `linkedin_publications`
Entidad central del sistema.

Representa cada publicación individual planificada o generada para LinkedIn.

Sirve para:
- almacenar copy, CTA, hashtags y metadatos editoriales
- guardar fechas
- registrar estado actual
- conectar con imagen, aprobaciones e integración remota

### 3. `linkedin_publication_status_history`
Historial de cambios de estado por publicación.

Sirve para:
- auditar el ciclo de vida
- saber quién o qué cambió el estado
- detectar errores, reprogramaciones y cancelaciones

### 4. `linkedin_publication_assets`
Tabla opcional pero útil para desacoplar la parte visual.

Sirve para:
- registrar imagen generada
- distinguir asset pendiente, aprobado o fallido
- permitir variantes visuales futuras

### 5. `linkedin_approval_events`
Registra revisiones y decisiones humanas.

Sirve para:
- guardar aprobación, rechazo o petición de cambios
- sostener el approval gate del MVP

### 6. `linkedin_delivery_events`
Tabla para interacción con LinkedIn o con la capa de integración.

Sirve para:
- registrar intentos de programación/publicación
- guardar IDs remotos
- capturar errores técnicos y respuestas del canal

---

## Relaciones

### Relación 1
`linkedin_prompt_runs` 1 → N `linkedin_publications`

Un prompt puede generar muchas publicaciones.

### Relación 2
`linkedin_publications` 1 → N `linkedin_publication_status_history`

Una publicación pasa por varios estados.

### Relación 3
`linkedin_publications` 1 → N `linkedin_publication_assets`

Una publicación puede tener uno o más assets asociados.

### Relación 4
`linkedin_publications` 1 → N `linkedin_approval_events`

Una publicación puede revisarse varias veces.

### Relación 5
`linkedin_publications` 1 → N `linkedin_delivery_events`

Puede haber varios intentos de programación/publicación.

---

## Estado mínimo del sistema

### Nivel lote / prompt
- `received`
- `parsed`
- `failed`
- `completed`

### Nivel publicación
- `draft`
- `pending_approval`
- `approved`
- `scheduled`
- `published`
- `publication_error`
- `cancelled`
- `rescheduled` (opcional desde v1)

### Nivel asset
- `pending`
- `generated`
- `selected`
- `error`

### Nivel delivery
- `pending`
- `scheduled`
- `published`
- `error`
- `cancelled`

---

## Decisiones de diseño para la v1

### Decisión 1
Guardar el prompt completo y también los parámetros extraídos en JSON.

### Decisión 2
Separar historial de estados para no perder trazabilidad.

### Decisión 3
Separar delivery remoto de la publicación principal para soportar reintentos y errores sin ensuciar la tabla base.

### Decisión 4
Mantener la tabla de assets aunque al principio solo use placeholder o una sola imagen.

### Decisión 5
Usar identificadores UUID y timestamps con zona horaria.

---

## Resultado esperado
Con este modelo, la pieza Growth de LinkedIn puede:
- recibir un prompt
- generar un lote
- planificar publicaciones
- guardar cada una con su metadata
- revisar y aprobar
- programar en LinkedIn
- registrar errores y auditoría
- escalar más adelante sin rehacer la base
