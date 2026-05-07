# ORQUESTA v2 · Captación · Análisis técnico

## Identificación
- **Pilar:** Captación
- **Proceso:** `captacion-leads-comunidad-orquesta-v2`
- **Estado:** análisis técnico
- **Objetivo:** diseñar una implementación mínima seria para captar leads, responder rápido y medir el rendimiento

## Resultado que se quiere conseguir
Crear un sistema sencillo pero trazable para:
- captar leads desde formulario
- guardarlos con estructura
- responder automáticamente por Gmail
- notificar internamente
- medir tiempos, calidad y conversiones
- dejar una base clara para escalar a CRM o Supabase más adelante

## Stack propuesto
### Captura
- Google Form o landing con formulario

### Registro
- Google Sheets como base operativa inicial

### Automatización
- n8n como motor principal

### Comunicación
- Gmail para respuesta inicial y avisos internos

### Documentación
- Google Docs + repo Orquesta

### Reporting
- Looker Studio simple conectado a Google Sheets

## Arquitectura mínima implementable

### Flujo principal
1. El lead rellena un formulario
2. Google Forms escribe una fila en Google Sheets
3. n8n detecta nueva fila o nueva entrada
4. n8n normaliza datos y asigna estado inicial
5. n8n envía email de respuesta inicial por Gmail
6. n8n envía aviso interno al responsable
7. n8n actualiza la fila con timestamps y seguimiento
8. Looker Studio lee la hoja y muestra KPIs

## Componentes

### 1. Google Form
Función:
- punto de captura inicial

Campos recomendados:
- nombre
- email
- teléfono
- empresa
- rol
- necesidad principal
- urgencia
- consentimiento
- origen si aplica

### 2. Google Sheet base
Función:
- tabla operativa mínima y fuente inicial de reporting

Pestañas recomendadas:
- `leads`
- `catalogos`
- `seguimiento`
- `dashboard_base`

### 3. n8n
Función:
- automatización central

Responsabilidades:
- leer nuevas entradas
- normalizar datos
- deduplicar básico
- asignar estado inicial
- enviar email
- alertar al responsable
- registrar tiempos

### 4. Gmail
Función:
- respuesta al lead
- aviso interno

### 5. Looker Studio
Función:
- vista de métricas sin complicar la base

## Modelo de datos recomendado

### Hoja `leads`
Campos mínimos:
- `lead_id`
- `created_at`
- `source`
- `campaign`
- `name`
- `email`
- `phone`
- `company`
- `role`
- `need_summary`
- `urgency`
- `consent`
- `status`
- `lead_score`
- `owner`
- `first_response_at`
- `meeting_booked_at`
- `qualified_at`
- `last_contact_at`
- `duplicate_of`
- `notes`

### Hoja `catalogos`
Contenido sugerido:
- estados válidos
- urgencias válidas
- owners
- fuentes

### Hoja `seguimiento`
Contenido sugerido:
- `event_id`
- `lead_id`
- `event_type`
- `event_at`
- `actor`
- `detail`

## Estados propuestos
- nuevo
- respondido
- pendiente-respuesta-lead
- cualificado
- no-cualificado
- reunion-agendada
- oportunidad
- cerrado
- duplicado

## Lead scoring inicial simple
Regla práctica inicial:
- +3 si el problema está claro
- +2 si empresa o rol encajan
- +2 si la urgencia es alta
- +1 si deja teléfono además de email
- -2 si la respuesta es demasiado vaga

Traducción operativa:
- 0 a 2: bajo
- 3 a 5: medio
- 6+: alto

## Automatizaciones mínimas

### Flujo 1. Captura y alta
Trigger:
- nueva fila o nuevo registro

Acciones:
- generar `lead_id`
- normalizar strings
- poner `status = nuevo`
- guardar `created_at`
- calcular score inicial

### Flujo 2. Respuesta inicial por Gmail
Trigger:
- lead nuevo con email válido

Acciones:
- enviar email automático
- registrar `first_response_at`
- cambiar estado a `respondido`

### Flujo 3. Aviso interno
Trigger:
- lead score medio o alto

Acciones:
- enviar aviso interno por Gmail
- asignar owner inicial si aplica

### Flujo 4. Seguimiento y control
Trigger:
- revisión periódica desde n8n

Acciones:
- detectar leads sin respuesta posterior
- detectar leads nuevos sin owner
- detectar leads estancados más de X días
- registrar incidencias operativas

## Gmail: mensajes base
### Email al lead
Objetivo:
- confirmar recepción
- dar siguiente paso
- reducir fricción

### Email interno
Objetivo:
- avisar de lead valioso
- resumir datos clave
- pedir acción rápida

## Reporting simple en Looker Studio

### Fuente
- Google Sheet `leads`

### KPIs mínimos
- leads totales
- leads por fuente
- leads por estado
- tiempo de primera respuesta
- leads cualificados
- ratio cualificado / total
- reuniones agendadas

### Gráficos mínimos
- serie temporal de leads por día o semana
- tabla por fuente
- pastel o barras por estado
- score medio por fuente
- lista de leads sin mover

## Riesgos técnicos
- duplicados manuales
- validaciones pobres del formulario
- Gmail con plantillas poco afinadas
- n8n mal sincronizado con cambios en la hoja
- Looker Studio con campos inconsistentes

## Controles recomendados
- estados cerrados y validados
- hoja `catalogos`
- naming consistente de origen y campaña
- columna `duplicate_of`
- revisión semanal del dashboard

## Fases de implantación
### Fase 1. Base funcional
- crear formulario
- crear sheet
- crear workflow n8n
- activar Gmail
- tener dashboard mínimo

### Fase 2. Mejora operativa
- scoring más fino
- reglas de seguimiento
- mejor clasificación de necesidad
- mejor segmentación por origen

### Fase 3. Escalado
- migración a CRM o Supabase si compensa
- más trazabilidad
- reporting ejecutivo
- atribución más seria

## Decisiones abiertas
Todavía habría que decidir:
- si la captura arranca con Google Form o landing propia
- si el aviso interno va a una sola persona o a varias
- qué SLA concreto tendrá la primera respuesta
- cuándo pasamos de Google Sheets a CRM o base más robusta

## Recomendación clara
Para empezar bien y sin barro innecesario:
- Google Form
- Google Sheet
- n8n
- Gmail
- Looker Studio

Es una base razonable para aprender rápido y luego escalar con criterio.
