---
name: orquesta-router
description: Skill madre de Orquesta. Clasifica el problema empresarial y deriva a la skill de Orquesta correcta según el caso: captación, onboarding, control operativo y reporting, operaciones de ejecución, análisis ejecutivo y priorización, marketing autónomo, procesos de negocio, creatividad audiovisual, control total o capa tech de arquitectura, integraciones, n8n, APIs, Supabase, memoria, RAG y sistemas agentic reales.
---

# Orquesta Router

Esta es la skill madre de Orquesta.

Su función no es resolver en detalle todos los problemas por sí sola, sino identificar correctamente el tipo de reto y activar el enfoque especializado adecuado dentro del ecosistema Orquesta.

## Cuándo usar esta skill

Úsala cuando el usuario pida ayuda sobre Orquesta de forma amplia o ambigua, por ejemplo:

- diseño de una solución basada en agentes IA
- arquitectura para una empresa automatizada
- mejora operativa con IA
- crecimiento comercial automatizado
- producción audiovisual con IA
- gobierno, control o supervisión de automatizaciones
- casos en los que todavía no está claro qué skill especializada encaja mejor

Si el usuario ya pide claramente una de las áreas específicas, usa directamente la skill especializada en vez de esta.

## Skills hijas disponibles

### 1. `orquesta-captacion-leads`
Úsala cuando el reto esté centrado en:
- captación de demanda
- formularios y landings
- lead flow
- lead scoring
- respuesta automática inicial
- integración con CRM
- conversión de lead a cita o venta

### 2. `orquesta-onboarding-clientes`
Úsala cuando el reto esté centrado en:
- alta de nuevos clientes
- bienvenida y kickoff
- petición de datos o accesos
- checklist de arranque
- reparto de tareas internas
- tiempo hasta primer valor
- transición a operación normal

### 3. `orquesta-control-operativo-reporting`
Úsala cuando el reto esté centrado en:
- reporting operativo
- control diario
- cuadros de mando
- SLAs
- backlog
- alertas
- incidencias
- visibilidad para dirección u operaciones

### 4. `orquesta-operaciones-ejecucion`
Úsala cuando el reto esté centrado en:
- operación diaria real
- tareas y responsables
- dependencias
- bloqueos operativos
- handoffs internos
- seguimiento de ejecución
- criterio de cierre
- paso de control a trabajo real

### 5. `orquesta-analisis-ejecutivo`
Úsala cuando el reto esté centrado en:
- decidir el siguiente paso
- priorizar iniciativas
- ordenar un roadmap
- comparar opciones
- detectar el cuello de botella real
- recomendar una secuencia de trabajo clara
- explicar una decisión con criterio ejecutivo

### 6. `orquesta-marketing-autonomo`
Úsala cuando el reto esté centrado en:
- arquitectura global de marketing
- embudos completos
- campañas
- nurturing
- CRM
- contenido orientado a crecimiento
- adquisición, activación, retención o revenue

### 7. `orquesta-procesos-negocio`
Úsala cuando el reto esté centrado en:
- backoffice
- procesos empresariales amplios
- integraciones entre sistemas
- automatización de flujos transversales
- eficiencia operativa de nivel proceso
- aprobaciones, tickets, documentación o circuitos de trabajo más amplios

### 8. `orquesta-creatividad-audiovisual`
Úsala cuando el reto esté centrado en:
- branding audiovisual
- campañas creativas
- vídeo
- piezas visuales
- storytelling
- contenido multiformato
- producción creativa escalable

### 9. `orquesta-control-total`
Úsala cuando el reto esté centrado en:
- gobierno
- observabilidad
- seguridad
- permisos
- supervisión
- métricas
- alertas
- control de agentes
- riesgos operativos o compliance

### 10. `orquesta-tech`
Úsala cuando el reto esté centrado en:
- arquitectura técnica
- integraciones
- n8n o Make
- APIs y webhooks
- Supabase y datos
- memoria y RAG
- evals, control de costes y kill switch
- approval gates
- despliegue de sistemas agentic reales

## Método de clasificación

Antes de derivar, analiza siempre:

1. Objetivo principal del negocio.
2. Área dominante del problema.
3. Qué sistema necesita diseñarse o corregirse.
4. Qué tipo de riesgo tendría una mala decisión.
5. Si el caso pertenece claramente a una skill o mezcla varias.

## Reglas de derivación

### Derivación simple
Si el problema cae claramente en una sola categoría, deriva a esa skill y responde desde ese marco.

### Derivación mixta
Si el problema mezcla varias áreas, haz esto:
- identifica la skill principal
- identifica skills secundarias de apoyo
- responde con liderazgo de la skill principal, pero explicando qué otras capas intervienen

Ejemplo:
- un sistema de captación con formularios, scoring y handoff comercial → principal `orquesta-captacion-leads`, apoyo `orquesta-marketing-autonomo`
- una alta de cliente con accesos, checklist y kickoff → principal `orquesta-onboarding-clientes`, apoyo `orquesta-operaciones-ejecucion`
- una operación con SLAs, incidencias y dashboard semanal → principal `orquesta-control-operativo-reporting`, apoyo `orquesta-control-total`
- una operación diaria con tareas, bloqueos y responsables → principal `orquesta-operaciones-ejecucion`, apoyo `orquesta-control-operativo-reporting`
- una decisión sobre qué hacer primero, qué capa priorizar o cómo secuenciar un roadmap → principal `orquesta-analisis-ejecutivo`, apoyo según el dominio afectado
- una fábrica de contenido con distribución y medición → principal `orquesta-creatividad-audiovisual`, apoyo `orquesta-marketing-autonomo`
- una operación automatizada entre CRM, ERP y aprobaciones con observabilidad → principal `orquesta-procesos-negocio`, apoyo `orquesta-control-total`
- una implantación con n8n, Supabase, webhooks, memoria y aprobación humana → principal `orquesta-tech`, apoyo según el proceso de negocio implicado

### Si falta contexto
Si no está claro qué skill corresponde, pide contexto mínimo antes de profundizar.

Pide solo lo necesario:
- objetivo de negocio
- tipo de proceso o área afectada
- sistemas implicados
- prioridad principal: crecer, operar mejor, crear contenido o controlar riesgo

## Cómo responder

Cuando uses esta skill, responde en tres capas:

1. **Diagnóstico de encaje**
   - qué tipo de problema es
   - por qué pertenece a una skill concreta o a una combinación

2. **Ruta recomendada**
   - skill principal
   - skills secundarias si aplica

3. **Primer marco de trabajo**
   - siguiente enfoque útil
   - quick wins
   - siguiente paso recomendado

## Principios

- No fuerces una sola skill si el caso es realmente mixto.
- Prioriza siempre el problema dominante del negocio.
- Derivar bien es más importante que responder rápido pero mal enfocado.
- Orquesta es un sistema de especialidades coordinadas, no una skill monolítica.

## Formato de salida

Entrega normalmente así:

- tipo de problema
- skill principal recomendada
- skills secundarias si aplica
- por qué
- siguiente paso útil
