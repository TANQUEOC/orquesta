# ORQUESTA v2 · Caso de uso formal · Control operativo y reporting v1

## Identificación
- **Pilar:** Reporting y control
- **Nombre del caso:** Control operativo y reporting para Orquesta
- **Versión:** v1
- **Estado:** diseño operativo
- **Skill principal:** `orquesta-control-operativo-reporting`
- **Skills de apoyo:** `orquesta-control-total`, `orquesta-procesos-negocio`

## Objetivo de negocio
Diseñar un sistema de control operativo y reporting capaz de dar visibilidad real sobre lo que ocurre en la operación, detectar desvíos a tiempo y facilitar decisiones con datos útiles.

El objetivo no es tener dashboards decorativos, sino una capa de control que permita gobernar procesos, automatizaciones y handoffs con criterio.

## Problema que resuelve
Muchos negocios tienen actividad, pero no una visión clara de:
- qué procesos van bien o mal
- dónde se atascan las tareas
- qué SLAs se incumplen
- qué incidencias se repiten
- qué automatizaciones fallan
- qué requiere intervención humana
- qué necesita ver dirección frente a operaciones

Este caso ordena esa capa de visibilidad.

## Resultado esperado
Al terminar la implantación, Orquesta debería tener:
- inventario básico de procesos controlados
- estados operativos claros
- eventos y métricas clave registrados
- alertas mínimas
- dashboard operativo
- vista ejecutiva resumida
- criterio de escalado humano
- rutina de revisión

## Ámbito de control
Este caso está pensado para controlar procesos como:
- captación de leads
- onboarding de clientes
- seguimiento de tareas operativas
- incidencias
- automatizaciones críticas
- reporting semanal del negocio

## Flujo del caso de uso

### 1. Inventario de procesos
Primero se decide qué procesos entran en control.

Mínimo recomendable:
- captación
- onboarding
- operación semanal
- incidencias
- automatizaciones críticas

### 2. Definición de estados
Cada proceso debe tener estados claros.

Ejemplo:
- nuevo
- en curso
- pendiente de tercero
- bloqueado
- completado
- error
- escalado

### 3. Registro de eventos
Se deben guardar eventos que permitan entender qué pasó.

Ejemplos:
- lead creado
- primera respuesta enviada
- kickoff realizado
- tarea bloqueada
- SLA incumplido
- automatización fallida
- incidencia cerrada

### 4. Métricas operativas
Se seleccionan métricas que muevan decisiones.

Ejemplos:
- volumen por proceso
- tiempo por etapa
- backlog por estado
- porcentaje de SLA cumplido
- incidencias abiertas
- errores por automatización
- tiempo medio de resolución

### 5. Alertas
Se define cuándo saltar aviso y a quién.

Ejemplos:
- lead caliente sin respuesta
- onboarding parado más de 48h
- automatización fallida
- incidencia crítica sin dueño
- SLA incumplido

### 6. Dashboard operativo
Vista pensada para quien gestiona el día a día.

Debe responder rápido a:
- qué está atascado
- qué va tarde
- qué proceso falla más
- dónde actuar hoy

### 7. Vista ejecutiva
Resumen para dirección.

Debe responder a:
- cómo va la operación
- dónde se pierde rendimiento
- qué riesgos crecen
- qué palancas conviene priorizar

### 8. Cadencia de revisión
La capa de control solo sirve si se revisa.

Cadencias recomendadas:
- diaria para incidencias y bloqueos
- semanal para operación y SLA
- mensual para tendencias y mejoras estructurales

## Arquitectura mínima viable

### Opción simple
- tabla central o Google Sheets
- automatización con n8n o Make
- Gmail o Telegram para alertas
- Google Docs para documentación
- dashboard básico en Looker Studio, Sheets o similar

### Opción objetivo
- eventos desde CRM, automatizaciones y operaciones
- base estructurada de estados e incidencias
- dashboard operativo
- dashboard ejecutivo
- alertas automáticas
- histórico para análisis

## Automatizaciones prioritarias
1. Registro de eventos clave
2. Cálculo automático de tiempos y SLAs
3. Alertas por bloqueo o error
4. Resumen semanal automático
5. Detección de procesos sin movimiento
6. Escalado a responsable cuando toque

## Vistas recomendadas

### Vista operativa
- tareas o casos abiertos
- backlog por estado
- bloqueados
- retrasados
- errores activos
- próximas acciones

### Vista ejecutiva
- procesos activos
- SLA global
- incidencias críticas
- tiempo medio de resolución
- evolución semanal
- foco prioritario

## KPIs principales
- SLA cumplido vs incumplido
- tiempo medio por etapa
- tiempo medio de resolución
- incidencias abiertas por criticidad
- backlog por proceso
- ratio de automatizaciones exitosas
- número de bloqueos activos
- porcentaje de casos sin responsable

## Riesgos y controles

### Riesgos
- exceso de métricas inútiles
- datos no fiables
- estados mal definidos
- alertas que nadie atiende
- mezcla de vista ejecutiva y operativa en un caos único
- reporting sin vínculo con decisiones reales

### Controles
- pocos KPIs, bien definidos
- estados obligatorios
- dueño por proceso o incidencia
- umbrales de alerta claros
- revisión periódica
- trazabilidad de cambios y escalados

## Reparto humano vs automatización

### Automático
- captura de eventos
- cálculo de métricas
- alertas
- resúmenes periódicos
- detección de inactividad o error

### Asistido
- clasificación de incidencias
- resumen de estado
- priorización sugerida
- explicación de desviaciones

### Humano
- decisión ante bloqueos relevantes
- reasignación de prioridades
- resolución de excepciones
- cierre de incidencias críticas
- lectura ejecutiva del reporting

## Roadmap de implantación

### Fase 1
- definir procesos bajo control
- definir estados
- definir métricas mínimas
- activar alertas esenciales

### Fase 2
- unificar eventos
- construir dashboard operativo
- crear resumen semanal
- ordenar responsables y escalado

### Fase 3
- crear vista ejecutiva
- detectar patrones de fallo
- comparar rendimiento por periodo
- mejorar gobierno de automatizaciones

## Documento operativo mínimo derivado de este caso
A partir de este caso conviene producir después:
- catálogo de procesos controlados
- diccionario de estados
- matriz de alertas
- plantilla de dashboard
- flujo n8n/Make de resúmenes y alertas
- protocolo de revisión semanal

## Siguiente paso recomendado
Convertir este caso en un sistema operativo real conectado a captación y onboarding, con reporting semanal accionable.

Sugerencia directa:
**`dashboard-operativo-orquesta-v1`**
