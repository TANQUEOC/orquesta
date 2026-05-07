---
name: orquesta-tech
description: Diseña, implementa y gobierna la capa técnica de ORQUESTA. Úsala cuando el trabajo trate de arquitectura técnica, integraciones, n8n, APIs, webhooks, Supabase, bases de datos, memoria, RAG, observabilidad, evals, control de costes, approval gates o despliegue de sistemas agentic reales para clientes o procesos internos.
---

# ORQUESTA Tech

## Para qué existe
Esta skill se encarga de la capa técnica de ORQUESTA.

No se centra en estrategia comercial ni en copy. Se centra en convertir casos de uso en sistemas operativos reales.

## Qué debe resolver
Usa esta skill cuando haya que:
- diseñar arquitectura técnica
- decidir stack e integraciones
- aterrizar flujos en n8n o Make
- definir APIs, webhooks y contratos entre sistemas
- trabajar con Supabase o bases de datos
- diseñar memoria, contexto y RAG
- definir observabilidad, evals y control de costes
- introducir approval gates y kill switch
- preparar despliegues de sistemas agentic reales

## Regla principal
ORQUESTA Tech no debe quedarse en “qué herramienta usamos”.

Debe responder siempre a esto:

1. qué trabajo real debe ejecutar el sistema
2. qué herramientas necesita
3. qué datos y contexto necesita
4. qué parte puede automatizarse
5. qué parte exige supervisión humana
6. cómo se observa, prueba y gobierna en producción

## Forma de trabajar

### 1. Empezar por el trabajo real
Antes de tocar stack o integraciones, deja claro:
- objetivo operativo
- entradas
- salidas
- eventos disparadores
- decisiones críticas
- acciones sensibles

### 2. Diseñar la arquitectura mínima suficiente
Prioriza:
- simplicidad
- trazabilidad
- velocidad de implantación
- facilidad de mantenimiento
- posibilidad de crecer después

Evita sobrearquitectura temprana.

### 3. Separar capas
Toda solución debería distinguir, cuando aplique:
- interfaz o punto de entrada
- lógica de decisión
- herramientas e integraciones
- estado y memoria
- reporting y control
- gates humanos

### 4. Diseñar para producción
Toda pieza técnica seria debe contemplar:
- logs
- observabilidad
- evals o pruebas de comportamiento
- control de coste
- retries o manejo de errores
- kill switch si hay loops o automatizaciones sensibles
- approval gates para acciones irreversibles

## Stack típico recomendado
Según el caso, ORQUESTA Tech suele combinar:
- Google Forms / Sheets / Docs / Gmail
- n8n
- Supabase
- webhooks y APIs REST
- almacenamiento estructurado en Postgres
- RAG simple sobre documentación útil

## Cuándo leer referencias
- Lee `references/architecture-patterns.md` cuando haya que decidir arquitectura o patrón de implantación.
- Lee `references/agentic-production-checklist.md` cuando el trabajo se acerque a producción o implique riesgos operativos.
- Lee `references/orquesta-tech-scope.md` cuando haya que delimitar bien el alcance técnico de esta skill frente a otras skills de ORQUESTA.
- Lee `references/solo-founder-agentic-stack.md` cuando haga falta definir stack, flujo de trabajo o criterio de herramientas para lanzar rápido con un equipo pequeño o un solo founder.
- Lee `references/knowledge-organization-and-rag-readiness.md` cuando el trabajo trate de preparar proyectos, skills o documentación para MCP, Supabase o RAG.

## Entregables típicos
- arquitectura mínima
- mapa de integraciones
- diseño de datos
- workflow n8n o Make
- especificación de webhooks/API
- plan de memoria o RAG
- checklist de producción
- backlog técnico priorizado

## Regla final
ORQUESTA Tech existe para convertir ideas y procesos en sistemas agentic implantables.

Menos herramienta suelta.
Más capacidad técnica que ejecuta trabajo real con control.
