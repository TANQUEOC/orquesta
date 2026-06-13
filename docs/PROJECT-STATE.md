# ORQUESTA · Estado del proyecto

## Qué es la fuente principal aquí
Este documento es la referencia rápida de estado.

Para evitar duplicidad, la estructura canónica queda así:
- visión y posicionamiento general → `README.md`
- arquitectura y reglas de diseño → `docs/ARCHITECTURE.md`
- método de trabajo → `docs/METODOLOGIA-ORQUESTA-1-SEMANA-1-PROCESO.md`
- marco agentic y AaaS → `docs/PRINCIPIOS-AGENTIC-AIAS-PARA-ORQUESTA.md`
- modelo formal AaaS → `docs/ORQUESTA-AAGENTS-AS-A-SERVICE.md`
- reformulación v3 de pilares → `docs/ORQUESTA-v3-PILARES-AGENTIC.md`
- alineación formal de pilares con AaaS → `docs/ORQUESTA-PILARES-AAS-ALIGNMENT.md`
- catálogo formal de agentes → `docs/AGENTES-ORQUESTA-CATALOGO.md`
- detalle operativo por pilar → `docs/pilares/`
- catálogo de casos de uso por pilar → `docs/CATALOGO-CASOS-DE-USO-POR-PILAR.md`
- entregables listos para cliente o implantación → `deliverables/`

## Estado actual
ORQUESTA ya está en fase de sistema estructurado e implantable.

Además, ya está reformulándose explícitamente como arquitectura de **Agents as a Service**, no solo como sistema de procesos, automatizaciones y dashboards.

Lo más maduro ahora mismo es:
- arquitectura v2/v3 y marco AaaS
- skills principales
- documentación por pilares
- captación como caso más cercano a implantación real
- skill `orquesta-tech` para la capa técnica agentic

## Prioridades reales
1. cerrar Captación de extremo a extremo
2. convertir Onboarding en pack real de implementación
3. seguir alineando pilares, skills y entregables al modelo AaaS
4. reforzar conocimiento técnico reusable para MCP, RAG e infraestructura agentic

## Últimos avances relevantes
- creado el agente/skill `orquesta-onboarding` como especialista ORQUESTAonboarding
- creada la referencia técnica reusable `skills/orquesta-onboarding/references/mvp-tecnico-gratuito.md`
- creado el entregable `deliverables/orquesta-onboarding-mvp-instalacion-tecnica-v1.md` con el MVP técnico funcional y stack gratuito para onboarding
- creado el documento maestro de webinar `deliverables/ORQUESTA-ONEPAGER-MAESTRO-WEBINAR.md` para alinear exposición pública, oferta y piezas vendibles
- creada la guía de marca formal cerrada `deliverables/ORQUESTA-GUIA-DE-MARCA-FORMAL-v1.md` tomando como referencia `compan-ia.lovable.app`
- creada la presentación `deliverables/ORQUESTA-DECK-WEBINAR-v2.pptx` con plantilla inspirada en `compan-ia.lovable.app`, fondo hero real, cabecera/pie personalizados y lockup de marca `ORQUESTA · by CompañIA`
- creada la plantilla maestra reutilizable `deliverables/ORQUESTA-DECK-MASTER-TEMPLATE-v1.pptx` con layouts base, más guía de uso `deliverables/ORQUESTA-DECK-MASTER-TEMPLATE-v1-README.md` y generador editable `tmp/pptx-build/build_orquesta_master_template_v1.js`
- registrado el caso de uso `Agente IA especialista en creación y programación de publicaciones en LinkedIn` como caso principal del pilar Growth, y creado el catálogo `docs/CATALOGO-CASOS-DE-USO-POR-PILAR.md` para organizar casos por pilar
- empaquetada la funcionalidad `Campaña publicitaria automática de Growth LinkedIn` como paquete ejecutable canónico en `deliverables/orquesta-v3-caso-uso-growth-linkedin-v1/paquete-ejecutable-v1/`, incluyendo HTML, runtime, SQL y guías de integración/despliegue

## Regla de conocimiento
Si un aprendizaje es estable y reusable, debería vivir en:
- `docs/` si afecta al proyecto entero
- `skills/*/references/` si afecta a una skill concreta
- `deliverables/` si es una pieza vendible o ejecutable para cliente

## Señales de salud del proyecto
- cada pilar tiene documento propio
- existe separación entre visión, arquitectura, skills y entregables
- ya hay paquetes orientados a cliente
- falta seguir endureciendo fuentes principales y evitar nuevos duplicados innecesarios
