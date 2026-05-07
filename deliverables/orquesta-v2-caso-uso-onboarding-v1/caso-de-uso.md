# ORQUESTA v2 · Caso de uso formal · Onboarding v1

## Identificación
- **Pilar:** Onboarding
- **Nombre del caso:** Onboarding de nuevos clientes para Orquesta
- **Versión:** v1
- **Estado:** diseño operativo
- **Skill principal:** `orquesta-onboarding-clientes`
- **Skills de apoyo:** `orquesta-procesos-negocio`, `orquesta-control-operativo-reporting`, `orquesta-control-total`

## Objetivo de negocio
Diseñar un sistema de onboarding capaz de convertir una venta en una puesta en marcha limpia, rápida, trazable y controlada.

El objetivo no es solo dar la bienvenida, sino garantizar que el cliente entra bien, el equipo interno sabe qué hacer y el tiempo hasta primer valor se reduce.

## Problema que resuelve
Muchos negocios venden, pero luego pierden calidad en el arranque por:
- información incompleta
- accesos pedidos tarde
- tareas sin dueño
- clientes desorientados
- esperas entre comercial y operación
- poca visibilidad del estado
- incidencias repetidas en la primera semana

Este caso de uso ordena esa transición.

## Resultado esperado
Al terminar la implantación, Orquesta debería tener:
- trigger claro desde el cierre comercial
- expediente inicial del cliente
- checklist de datos y accesos
- mensaje de bienvenida
- kickoff bien definido
- tareas internas asignadas
- seguimiento inicial
- criterio claro de paso a operación normal
- métricas del onboarding

## Perfil de cliente ideal
Este caso encaja especialmente con:
- servicios consultivos o de implementación
- clientes que requieren acceso a herramientas o activos
- procesos donde la primera semana es crítica
- negocios con varias personas implicadas tras la venta

## Flujo del caso de uso

### 1. Cierre comercial
El onboarding comienza cuando se confirma que la venta está cerrada y hay luz verde operativa.

Trigger recomendado:
- cambio de estado en CRM
- firma
- pago inicial
- validación manual del comercial

### 2. Alta del expediente del cliente
Se crea un registro central con:
- nombre del cliente
- empresa
- contacto principal
- servicio contratado
- fecha de inicio
- responsable comercial
- responsable operativo
- estado del onboarding

### 3. Bienvenida
Se envía un mensaje inicial para:
- confirmar arranque
- explicar siguientes pasos
- pedir información necesaria
- marcar responsable y canal de comunicación

### 4. Recogida de datos y accesos
Checklist típica:
- datos de facturación si aplica
- accesos a cuentas
- materiales o activos previos
- contactos clave
- objetivos inmediatos
- restricciones o dependencias

### 5. Kickoff
Objetivos del kickoff:
- alinear expectativas
- confirmar alcance
- revisar tiempos
- validar prioridades
- resolver dudas iniciales

### 6. Configuración interna
Acciones típicas:
- crear carpeta o espacio de trabajo
- crear documento maestro del cliente
- asignar tareas
- preparar herramientas
- activar automatizaciones necesarias

### 7. Seguimiento de primera semana
Durante los primeros días se controla:
- si faltan accesos
- si el cliente respondió
- si hay bloqueo interno
- si se entregó el primer valor
- si el estado avanzó en plazo

### 8. Handoff a operación normal
El onboarding termina cuando se cumplen criterios objetivos, por ejemplo:
- kickoff hecho
- accesos recibidos
- entorno preparado
- primer hito ejecutado
- siguiente fase asignada

## Arquitectura mínima viable

### Opción simple
- CRM o tabla central
- Gmail
- Google Drive
- Google Docs
- checklist estructurada
- n8n o Make para avisos y tareas

### Opción objetivo
- CRM con pipeline de onboarding
- automatización de emails y recordatorios
- documento maestro por cliente
- dashboard de seguimiento
- alertas por bloqueo y SLA

## Automatizaciones prioritarias
1. Alta automática del cliente al cerrar venta
2. Email o mensaje de bienvenida
3. Creación de carpeta y documento base
4. Checklist inicial asignada
5. Aviso interno al responsable
6. Recordatorios por datos o accesos pendientes
7. Registro de tiempos clave del onboarding

## Estados recomendados
- nuevo
- pendiente de bienvenida
- pendiente de datos/accesos
- kickoff programado
- en configuración
- primer valor entregado
- onboarding completado
- bloqueado

## KPIs principales
- tiempo desde venta hasta bienvenida
- tiempo desde venta hasta kickoff
- tiempo hasta primer valor
- porcentaje de onboarding completado en plazo
- bloqueos por falta de accesos
- incidencias en primera semana
- tasa de clientes con arranque limpio

## Riesgos y controles

### Riesgos
- depender de memoria humana
- pedir demasiadas cosas a la vez al cliente
- no saber quién lleva el caso
- accesos que llegan tarde
- promesa comercial mal trasladada a operación
- falta de visibilidad de bloqueos

### Controles
- checklist mínima obligatoria
- un responsable operativo claro
- estados de onboarding definidos
- alertas por espera prolongada
- kickoff como punto de validación
- criterio explícito de cierre del onboarding

## Reparto humano vs automatización

### Automático
- creación del expediente
- aviso de inicio
- envío de bienvenida
- seguimiento de pendientes
- logs y timestamps

### Asistido
- resumen del caso
- propuesta de checklist
- clasificación de bloqueos
- borradores de comunicaciones

### Humano
- kickoff
- validación de alcance
- resolución de excepciones
- relación con el cliente
- decisión de paso a operación normal

## Roadmap de implantación

### Fase 1
- definir estados
- definir checklist mínima
- crear trigger desde cierre comercial
- enviar bienvenida automática

### Fase 2
- activar recordatorios
- crear carpeta y documento base
- registrar tiempos clave
- ordenar handoff comercial → operación

### Fase 3
- añadir dashboard
- medir cuellos de botella
- optimizar tiempos y mensajes
- estandarizar por tipo de servicio

## Documento operativo mínimo derivado de este caso
A partir de este caso conviene producir después:
- checklist detallada de onboarding
- plantilla de bienvenida
- plantilla de kickoff
- flujo n8n/Make
- documento maestro por cliente
- dashboard de onboarding

## Siguiente paso recomendado
Convertir este caso en un flujo de implantación real según un servicio concreto de Orquesta.

Sugerencia directa:
**`onboarding-cliente-servicio-orquesta-v1`**
