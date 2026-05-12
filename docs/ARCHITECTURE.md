# ORQUESTA v2

## Estado
Arquitectura aplicada a nivel de proyecto, skills y documentación base.

No significa que todo esté automatizado ya.
Significa que Orquesta ya tiene una estructura operativa clara para seguir creciendo por casos de uso.

## Idea central
Orquesta v2 se organiza como un sistema de especialidades coordinadas.

A partir de ahora además asume una regla estratégica más fuerte:

**Orquesta no debe limitarse a dar herramientas para que el usuario trabaje. Debe diseñarse para que agentes bien orquestados hagan trabajo real por el cliente, con supervisión humana donde haga falta.**

Hay seis capas:

1. **router**
2. **agentes especializados**
3. **skills por proceso real**
4. **memoria y contexto operativo**
5. **integraciones y activos reutilizables**
6. **gobierno de producción**

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

Regla de diseño: cada agente debe trabajar con **objetivo**, no solo con prompt. Eso implica que cada pieza de Orquesta debe poder razonar, usar herramientas, observar resultados y decidir el siguiente paso dentro de límites definidos.

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

A partir del modelo AaaS, estos pilares no deben leerse solo como áreas funcionales. Deben leerse como **capacidades operativas desplegadas mediante agentes especializados**.

Cada pilar debe acabar teniendo:
- visión del pilar
- agente principal o familia de agentes
- casos de uso
- procesos tipo
- trigger de entrada
- contexto y memoria necesarios
- tools utilizables
- approval gates
- outputs esperados
- stack recomendado
- KPIs
- riesgos
- playbooks
- activos reutilizables

## 5. Integraciones y activos reutilizables
La arquitectura prevé conectar progresivamente:

Estas integraciones no son accesorios. Son la base para que los agentes actúen sobre sistemas reales y no se queden en generación de texto.

Regla de stack: cuando no haya una restricción fuerte, ORQUESTA debe favorecer stacks simples, muy conocidos por la IA, bien documentados y fáciles de mantener. Menos rareza técnica, más velocidad de implantación y mejor capacidad de iteración.

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
- catálogos de herramientas y acciones por agente
- contratos de entrada y salida entre procesos

## 5.5. Alineación AaaS de la columna principal
La secuencia prioritaria de ORQUESTA debe leerse ya como una red mínima de agentes operativos conectados:

- **Agente de Captación**
- **Agente de Onboarding**
- **Agente de Control Operativo**
- **Agente de Operaciones**
- **Agentes de Growth y Revenue**

La cadena operativa resultante es:

**Captación → Onboarding → Control → Operaciones → Growth**

La interfaz visible, dashboards, sheets o documentos deben considerarse la capa de supervisión y gobierno, no el producto principal.

## 6. Gobierno de producción
Todo diseño serio en Orquesta debe incorporar desde el principio estas piezas:

- **observabilidad**: ver qué hizo el agente, qué herramientas llamó y dónde falló
- **evals**: casos de prueba para detectar regresiones de comportamiento
- **control de coste**: budgets, alertas y límites por agente
- **kill switch**: corte inmediato si un loop o una ejecución se descontrola
- **approval gates**: acciones destructivas, irreversibles o sensibles requieren humano

Sin esta capa, no estamos construyendo Orquesta en producción. Solo demos bonitas.

## Cómo crecer desde aquí
La unidad de avance recomendada sigue siendo:

**1 semana, 1 proceso, 1 mejora real**

Cada caso nuevo debe pasar por esta secuencia:

1. elegir pilar
2. elegir proceso concreto
3. definir el trabajo real que el sistema debe hacer por el cliente
4. asignar skill principal
5. documentar caso de uso
6. diseñar flujo objetivo
7. definir herramientas, datos y contexto necesarios
8. definir stack
9. definir métricas
10. definir observabilidad, approval gates y límites de coste
11. dejar backlog siguiente

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

Y una regla extra: **cada pieza debe intentar subir de herramienta a ejecución**.

No basta con decir "aquí tienes el dashboard" o "aquí tienes el formulario".
La pregunta de Orquesta debe ser siempre:

**¿qué parte del trabajo completo puede resolver el sistema por el cliente, con qué contexto, con qué herramientas y con qué supervisión?**

## Siguiente fase recomendada
1. completar documentación de pilares
2. crear un caso de uso por pilar
3. generar playbooks concretos
4. conectar integraciones reales
5. definir memoria, herramientas y approval gates por proceso crítico
6. introducir observabilidad y evals en los flujos más maduros
7. separar agentes persistentes cuando compense
