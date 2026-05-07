# ORQUESTA v2

## Estado
Arquitectura aplicada a nivel de proyecto, skills y documentación base.

No significa que todo esté automatizado ya.
Significa que Orquesta ya tiene una estructura operativa clara para seguir creciendo por casos de uso.

## Idea central
Orquesta v2 se organiza como un sistema de especialidades coordinadas.

Hay cinco capas:

1. **router**
2. **agentes especializados**
3. **skills por proceso real**
4. **memoria y documentación por pilar**
5. **integraciones y activos reutilizables**

## 1. Router
El router decide por dónde entra cada reto.

Skill actual:
- `orquesta-router`

Su función es:
- clasificar el problema
- decidir skill principal
- detectar skills de apoyo
- convertir peticiones difusas en una ruta operativa clara

## 2. Agentes especializados
Aunque hoy operemos desde una misma sesión, la arquitectura ya contempla estos agentes funcionales:

- **agent-direccion**: visión, priorización, roadmap, decisiones de negocio
- **agent-leads**: captación, scoring, CRM, embudos
- **agent-onboarding**: arranque de clientes, accesos, kickoff, checklist
- **agent-operaciones**: procesos internos, handoffs, eficiencia operativa
- **agent-reporting**: métricas, alertas, cuadros de mando y control
- **agent-creatividad**: contenido, storytelling, piezas audiovisuales
- **agent-control**: gobierno, permisos, observabilidad y riesgos

## 3. Skills por proceso real
### Skills marco ya existentes
- `orquesta-router`
- `orquesta-marketing-autonomo`
- `orquesta-procesos-negocio`
- `orquesta-creatividad-audiovisual`
- `orquesta-control-total`

### Skills operativas v2 ya creadas
- `orquesta-captacion-leads`
- `orquesta-onboarding-clientes`
- `orquesta-control-operativo-reporting`

Estas tres son la base real de Orquesta v2 porque atacan procesos vendibles y repetibles.

## 4. Pilares de Orquesta
Orquesta v2 se apoya en cinco pilares documentales y operativos:

1. **captación**
2. **onboarding**
3. **operaciones**
4. **reporting y control**
5. **creatividad y crecimiento**

Cada pilar debe acabar teniendo:
- visión del pilar
- casos de uso
- procesos tipo
- stack recomendado
- KPIs
- riesgos
- playbooks
- activos reutilizables

## 5. Integraciones y activos reutilizables
La arquitectura prevé conectar progresivamente:

- CRM
- formularios
- Gmail
- Google Docs
- Google Drive
- Calendar
- n8n / Make
- dashboards
- base de datos / memoria operativa

Y además crear:
- plantillas
- checklists
- flujos JSON
- prompts reutilizables
- documentos de trabajo por caso

## Cómo crecer desde aquí
La unidad de avance recomendada sigue siendo:

**1 semana, 1 proceso, 1 mejora real**

Cada caso nuevo debe pasar por esta secuencia:

1. elegir pilar
2. elegir proceso concreto
3. asignar skill principal
4. documentar caso de uso
5. diseñar flujo objetivo
6. definir stack
7. definir métricas
8. dejar backlog siguiente

## Casos de uso prioritarios iniciales
### Pilar 1. Captación
- captación de leads
- lead scoring
- respuesta automática inicial
- handoff a comercial

### Pilar 2. Onboarding
- alta de cliente
- recogida de datos y accesos
- kickoff
- tiempo hasta primer valor

### Pilar 3. Operaciones
- seguimiento de tareas
- aprobaciones
- handoffs internos
- incidencias de servicio

### Pilar 4. Reporting y control
- dashboard operativo
- reporting semanal
- SLAs
- alertas y escalado

### Pilar 5. Creatividad y crecimiento
- fábrica de contenidos
- campañas
- distribución
- medición de rendimiento

## Regla de diseño
Orquesta no crece por ideas sueltas.
Crece por piezas reutilizables:
- un proceso
- una skill
- un documento
- una métrica
- una automatización
- una lección aprendida

## Siguiente fase recomendada
1. completar documentación de pilares
2. crear un caso de uso por pilar
3. generar playbooks concretos
4. conectar integraciones reales
5. separar agentes persistentes cuando compense
