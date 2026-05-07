# ORQUESTA v2 · Caso de uso formal · Captación v1

## Identificación
- **Pilar:** Captación
- **Nombre del caso:** Captación de leads para Orquesta
- **Versión:** v1
- **Estado:** diseño operativo
- **Skill principal:** `orquesta-captacion-leads`
- **Skills de apoyo:** `orquesta-marketing-autonomo`, `orquesta-control-operativo-reporting`, `orquesta-control-total`

## Objetivo de negocio
Diseñar un sistema de captación capaz de generar leads cualificados para Orquesta de forma trazable, medible y escalable.

El objetivo no es solo recoger contactos, sino crear un proceso completo desde el interés inicial hasta el handoff comercial o la siguiente automatización.

## Problema que resuelve
Muchos negocios captan contactos, pero no tienen un flujo serio para:
- distinguir leads válidos de ruido
- responder rápido
- guardar bien los datos
- clasificar intención
- convertir el lead en conversación útil
- medir qué canal y mensaje funcionan mejor

Este caso de uso resuelve justo ese hueco.

## Resultado esperado
Al terminar la implantación, Orquesta debería tener:
- una oferta de entrada clara
- uno o varios puntos de captura conectados
- almacenamiento estructurado del lead
- respuesta automática inicial
- cualificación básica
- seguimiento inicial
- traspaso a comercial o siguiente fase
- métricas operativas y de negocio

## Perfil de lead ideal
Este caso está pensado para leads que encajan con al menos una de estas categorías:
- empresas pequeñas o medianas con cuellos de botella operativos
- negocios que quieren automatizar captación, onboarding, reporting o procesos internos
- equipos que necesitan más estructura sin inflar plantilla
- perfiles interesados en sistemas con IA aplicados a negocio real

## Flujo del caso de uso

### 1. Atracción
Canales posibles:
- contenido orgánico
- publicaciones en comunidades
- referral
- redes sociales
- lead magnet
- outreach selectivo
- tráfico de pago si más adelante compensa

### 2. Punto de captura
Opciones válidas:
- formulario web
- Google Form
- Typeform
- landing dedicada
- CTA hacia WhatsApp con preclasificación

Datos mínimos a capturar:
- nombre
- email o teléfono
- empresa
- rol
- necesidad principal
- urgencia
- origen del lead

### 3. Registro del lead
El lead entra en un sistema central, idealmente CRM o una tabla estructurada intermedia.

Campos mínimos recomendados:
- `created_at`
- `source`
- `campaign`
- `name`
- `company`
- `role`
- `email`
- `phone`
- `need_summary`
- `status`
- `lead_score`
- `owner`
- `first_response_at`
- `qualified_at`
- `notes`

### 4. Respuesta automática inicial
Objetivo:
- confirmar recepción
- bajar fricción
- marcar siguiente paso
- aumentar probabilidad de respuesta

Ejemplos:
- email automático de bienvenida
- mensaje con enlace para agendar
- mensaje con pregunta de cualificación breve

### 5. Cualificación
Reglas simples iniciales:
- **alto interés:** problema claro, empresa real, necesidad cercana
- **interés medio:** encaje parcial o necesidad no urgente
- **interés bajo:** curiosidad, perfil no encajado o datos pobres

El scoring inicial puede basarse en:
- tipo de empresa
- tamaño potencial
- problema declarado
- urgencia
- canal de origen

### 6. Handoff
Según score y comportamiento:
- a comercial
- a secuencia de nurturing
- a espera/revisión
- a descarte razonado

### 7. Seguimiento
Ventanas mínimas recomendadas:
- primera respuesta en menos de 10 minutos si el lead es caliente
- recordatorio o segunda acción antes de 24 horas
- cierre temporal o cambio de estado antes de 7 días

### 8. Reporting
La captación debe acabar medida con KPIs útiles.

## Arquitectura mínima viable

### Opción simple
- formulario web o Google Form
- Google Sheets o tabla tipo Airtable/Supabase
- Gmail
- n8n o Make
- Google Docs para documentación

### Opción objetivo
- landing dedicada
- CRM como fuente de verdad
- automatización con n8n o Make
- scoring inicial
- secuencia de respuesta
- dashboard de control

## Automatizaciones prioritarias
1. Alta automática del lead en el sistema
2. Email o mensaje de respuesta inicial
3. Asignación de estado inicial
4. Enriquecimiento básico si hay datos suficientes
5. Aviso al responsable cuando el lead supera umbral
6. Registro de tiempos de respuesta

## KPIs principales
- volumen de leads por semana
- tasa de conversión de visita a lead
- porcentaje de lead válido
- tiempo de primera respuesta
- ratio lead a reunión
- ratio reunión a oportunidad
- origen con mejor calidad
- coste por lead si hay inversión

## Riesgos y controles

### Riesgos
- demasiados datos en formulario y caída de conversión
- leads sin respuesta rápida
- CRM desordenado
- scoring arbitrario
- atribución pobre
- captación desconectada del cierre comercial

### Controles
- formulario mínimo viable
- estados obligatorios
- alertas por lead sin respuesta
- revisión semanal de calidad
- naming de campañas y origen consistente
- trazabilidad de handoff

## Reparto humano vs automatización

### Automático
- recogida del lead
- guardado estructurado
- respuesta inicial
- asignación de estado base
- avisos y logs

### Asistido
- scoring inicial mejorado
- resumen del problema
- propuesta de siguiente paso

### Humano
- validación comercial final
- conversación de venta
- excepción o casos sensibles
- redefinición de oferta o segmentación

## Roadmap de implantación

### Fase 1
- definir oferta de entrada
- definir campos mínimos
- crear formulario
- conectar almacenamiento
- activar respuesta inicial

### Fase 2
- añadir scoring
- añadir seguimiento automático
- ordenar estados del pipeline
- medir tiempos y conversiones

### Fase 3
- enriquecer lead
- separar segmentos
- optimizar mensajes por canal
- construir dashboard operativo

## Documento operativo mínimo derivado de este caso
A partir de este caso conviene producir después:
- checklist de implantación
- esquema de datos
- flujo n8n/Make
- plantillas de respuesta inicial
- dashboard de captación

## Siguiente paso recomendado
Convertir este caso en un caso de implantación real con nombre de proceso concreto, stack elegido y flujo ejecutable.

Sugerencia directa:
**`captacion-leads-comunidad-orquesta-v2`**
