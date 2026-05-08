# ORQUESTA v3 · Sprint de implantación real · Onboarding v1

## Propósito
Este sprint existe para convertir el pilar de Onboarding en una capacidad operativa real de ORQUESTA.

No se trata de seguir diseñando el sistema.
Se trata de dejarlo funcionando de extremo a extremo con datos, automatización, seguimiento y control mínimo.

## Duración
5 días.

## Objetivo del sprint
Al terminar el sprint, el onboarding debe poder:

- recoger datos reales del nuevo cliente
- solicitar accesos y materiales necesarios
- generar una checklist de arranque
- preparar el kickoff
- dejar el estado del onboarding visible
- avisar cuando haya bloqueos
- registrar seguimiento
- dejar listo el handoff a operación

## Stack reutilizado
Se reutiliza la misma lógica y la misma familia de herramientas que en Captación:
- Google Form
- Google Sheets
- Gmail
- n8n

## Alcance del sprint por días

### Día 1 · Cierre de la entrada real del onboarding
#### Objetivo
Dejar definida y conectada la entrada del proceso.

#### Trabajo
- definir el formulario de onboarding o ficha de arranque
- decidir campos obligatorios del cliente
- conectar el formulario con su hoja real de respuestas
- revisar estructura de datos y estados base
- definir qué documentos o accesos son obligatorios

#### Entregable
- entrada de onboarding conectada
- hoja real identificada
- estructura inicial de datos cerrada

### Día 2 · Cierre del workflow de onboarding
#### Objetivo
Dejar configurado el flujo real de arranque.

#### Trabajo
- montar el workflow de onboarding en n8n
- recoger respuestas del formulario o ficha
- generar checklist inicial
- disparar email de solicitud o bienvenida
- registrar el onboarding en la base maestra
- preparar aviso interno o tarea de kickoff

#### Entregable
- workflow cargado
- automatización base operativa
- estructura de onboarding registrada

### Día 3 · Estados, bloqueos y control mínimo
#### Objetivo
Evitar caos y falta de visibilidad en el arranque.

#### Trabajo
- definir estados del onboarding
- definir criterio de bloqueo
- definir avisos internos por falta de accesos o materiales
- dejar trazabilidad del estado
- dejar preparado criterio de handoff a operación

#### Entregable
- estados de onboarding activos
- control mínimo de bloqueos
- base de trazabilidad operativa

### Día 4 · Prueba real extremo a extremo
#### Objetivo
Validar el sistema completo con un onboarding real o simulado.

#### Trabajo
- lanzar 1 o 2 onboardings de prueba
- comprobar que se recogen los datos
- comprobar que salen los emails adecuados
- comprobar que la checklist se genera
- comprobar que el estado cambia correctamente
- comprobar que el aviso interno funciona
- detectar y corregir fallos

#### Entregable
- test E2E completado
- incidencias corregidas
- flujo validado en condiciones reales

### Día 5 · Cierre operativo
#### Objetivo
Dejar Onboarding v1 listo para uso estable.

#### Trabajo
- revisar tiempos y esperas típicas
- revisar mensajes y solicitudes al cliente
- documentar funcionamiento
- documentar puntos de revisión humana
- documentar qué queda fuera del alcance
- definir siguiente mejora prioritaria

#### Entregable
- Onboarding v1 operativo
- checklist de operación
- backlog de mejora v2

## Definición de éxito
El sprint se considera correctamente cerrado cuando ocurre esto:

- entra un nuevo cliente
- se recogen datos y accesos necesarios
- se genera checklist
- se dispara la comunicación correcta
- el equipo ve el estado del onboarding
- los bloqueos se identifican
- el handoff a operación queda claro

## Definición de no terminado
No debe considerarse implantado de verdad si:

- solo existe documentación
- el flujo no fue probado de punta a punta
- el estado del onboarding no queda visible
- las tareas dependen de perseguirlo todo a mano
- el handoff a operación sigue siendo confuso
