# Patrones de arquitectura para ORQUESTA Tech

## Patrón 1. Google stack pragmático
Úsalo cuando el objetivo sea velocidad de implantación y baja fricción.

Piezas típicas:
- Google Form
- Google Sheet
- Gmail
- n8n
- Google Docs

Ideal para:
- captación
- onboarding simple
- reporting inicial

## Patrón 2. Supabase como sistema de registro
Úsalo cuando haga falta más estructura, trazabilidad y crecimiento.

Piezas típicas:
- frontend o formulario
- webhook / API
- Supabase Postgres
- funciones o automatización externa
- n8n para orquestación

Ideal para:
- leads persistentes
- estados de proceso
- colas de trabajo
- memoria operativa

## Patrón 3. Híbrido agentic con humano en el loop
Úsalo cuando el sistema deba ejecutar mucho trabajo, pero no pueda cerrar solo acciones sensibles.

Piezas típicas:
- entrada estructurada
- agente de clasificación o preparación
- herramientas externas
- cola de aprobación
- humano que aprueba, corrige o rechaza
- ejecución final

Ideal para:
- emails delicados
- publicación
- cobro
- borrado
- cambios con impacto real

## Regla de selección
- si importa velocidad: patrón 1
- si importa estructura y crecimiento: patrón 2
- si importa autonomía con control: patrón 3
