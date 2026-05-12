# ORQUESTA · Alineación formal de pilares con el modelo Agents as a Service

## 1. Objetivo del documento
Este documento alinea los pilares actuales de ORQUESTA con el modelo formal de **Agents as a Service**.

Su función es evitar que el modelo AaaS quede solo como manifiesto conceptual y convertirlo en una estructura operativa coherente, reutilizable y desplegable.

## 2. Regla de alineación
Cada pilar de ORQUESTA debe dejar de leerse únicamente como:
- área funcional
- proceso empresarial
- flujo de automatización
- conjunto de documentos o herramientas

Y debe pasar a leerse como:

**una capacidad operativa desplegada mediante uno o más agentes especializados que ejecutan trabajo real por el cliente con supervisión humana**.

## 3. Estructura obligatoria por pilar
A partir de ahora, cada pilar debe definirse con estas capas mínimas:

1. **capacidad de negocio** que se quiere desplegar
2. **agente principal** o familia de agentes asociados
3. **trabajo real que ejecuta**
4. **trigger de entrada**
5. **contexto y memoria necesarios**
6. **tools que puede usar**
7. **approval gates**
8. **outputs esperados**
9. **métricas de rendimiento**
10. **handoff al siguiente pilar o capa**

## 4. Alineación por pilar

### 4.1. Captación
#### Lectura AaaS
Captación debe entenderse como el despliegue de un **Agente de Captación**.

#### Capacidad desplegada
Detectar, capturar, clasificar y activar oportunidades de negocio.

#### Trabajo real
- registrar leads
- enriquecer datos
- clasificar y priorizar
- responder con el siguiente paso inicial
- preparar handoff comercial o de onboarding

#### Trigger típico
- nuevo lead
- formulario completado
- oportunidad entrante desde campaña, comunidad o fuente externa

#### Tools típicas
- formularios
- Google Sheets / CRM ligero
- Gmail
- n8n
- enriquecimiento de datos si aplica

#### Approval gates
- respuestas delicadas
- cambios de criterio comercial
- cuentas estratégicas

#### Output principal
- lead activado, clasificado y listo para seguimiento o conversión

#### Handoff natural
- `Captación → Onboarding`

---

### 4.2. Onboarding
#### Lectura AaaS
Onboarding debe entenderse como el despliegue de un **Agente de Onboarding**.

#### Capacidad desplegada
Convertir una venta en un arranque ordenado, trazable y rápido.

#### Trabajo real
- recoger datos y accesos
- generar checklist de arranque
- preparar kickoff
- registrar estado del onboarding
- detectar bloqueos iniciales

#### Trigger típico
- oportunidad cerrada
- cambio a cliente ganado
- alta manual aprobada

#### Tools típicas
- Google Forms / fichas de arranque
- Google Sheets
- Gmail
- Docs
- n8n

#### Approval gates
- validación de excepciones
- decisiones de relación con cliente
- cambios de alcance

#### Output principal
- cliente en arranque real con estado visible y contexto suficiente

#### Handoff natural
- `Onboarding → Control operativo y reporting`

---

### 4.3. Control operativo y reporting
#### Lectura AaaS
Control operativo y reporting debe entenderse como el despliegue de un **Agente de Control Operativo**.

#### Capacidad desplegada
Consolidar señales, detectar anomalías, ordenar prioridades y hacer visible lo que necesita atención.

#### Trabajo real
- consolidar estados
- registrar incidencias
- detectar bloqueos
- ordenar prioridades
- generar seguimiento y alertas
- declarar cuándo un caso está listo para operar

#### Trigger típico
- cambio de estado en onboarding
- actualización operativa relevante
- incidencia o SLA comprometido

#### Tools típicas
- Sheets o base ligera
- dashboards simples
- Gmail / alertas
- n8n
- fuentes de estado distribuidas

#### Approval gates
- umbrales críticos
- decisiones correctivas relevantes
- escalados sensibles

#### Output principal
- caso visible, priorizado y gobernable

#### Handoff natural
- `Control operativo y reporting → Operaciones`

---

### 4.4. Operaciones
#### Lectura AaaS
Operaciones debe entenderse como el despliegue de un **Agente de Operaciones**.

#### Capacidad desplegada
Convertir casos activos en trabajo real ejecutable con responsables, tareas, dependencias, bloqueos y cierre.

#### Agente principal
- `orquesta-operaciones-ejecucion`

#### Trabajo real
- crear o activar operaciones
- generar tareas base
- asignar responsables
- sostener seguimiento de ejecución
- detectar bloqueos operativos
- registrar avance y cierre

#### Trigger típico
- caso `listo_para_operar`
- prioridad alta validada
- handoff desde control

#### Tools típicas
- hojas o bases operativas
- n8n
- email
- checklists y documentación de soporte

#### Approval gates
- cambios críticos de prioridad
- cierres sensibles
- acciones externas comprometidas

#### Output principal
- trabajo real en curso con trazabilidad y criterio de cierre

#### Handoff natural
- hacia revisión, servicio completado o capas de crecimiento/expansión según el caso

---

### 4.5. Creatividad y crecimiento
#### Lectura AaaS
Creatividad y crecimiento debe entenderse como el despliegue de una **familia de agentes de Growth**.

#### Capacidad desplegada
Sostener ideación, producción, distribución y optimización de crecimiento con continuidad y aprendizaje.

#### Trabajo real
- proponer temas e ideas
- generar borradores y piezas iniciales
- adaptar formatos
- sostener ritmo de publicación o campaña
- detectar señales de rendimiento
- iterar sobre resultados

#### Trigger típico
- calendario de contenidos
- necesidad comercial o de growth
- señal de bajo rendimiento o nueva campaña

#### Tools típicas
- documentos
- calendarios editoriales
- automatizadores
- herramientas de canal
- fuentes de analítica

#### Approval gates
- aprobación de narrativa
- publicaciones sensibles
- campañas de impacto reputacional

#### Output principal
- capacidad continua de crecimiento asistido, no solo piezas aisladas

#### Handoff natural
- realimentación hacia Captación, venta o retención según objetivo de growth

## 5. Cambios de lectura estratégica
Alinear los pilares con AaaS implica tres cambios estratégicos:

### 5.1. De herramienta a capacidad
La unidad vendible deja de ser “te monto esto” y pasa a ser “te despliego esta capacidad operativa”.

### 5.2. De flujo a agente
Cada flujo maduro debe poder formularse como un agente con:
- objetivo
- contexto
- tools
- límites
- outputs
- supervisión humana

### 5.3. De documentación pasiva a catálogo operativo
Los documentos del pilar deben servir para:
- venderlo
- entenderlo
- implantarlo
- medirlo
- operarlo

## 6. Ajustes recomendados en ORQUESTA
Para que el modelo quede coherente, ORQUESTA debería reflejar este alineamiento en:

1. documentación de pilares
2. documentación de arquitectura
3. skills principales por pilar
4. entregables comerciales
5. handoffs entre pilares
6. playbooks de implantación

## 7. Prioridad de implantación
La secuencia operativa recomendada sigue siendo:

1. Captación
2. Onboarding
3. Control operativo y reporting
4. Operaciones
5. Growth y expansión

Esta secuencia ahora debe leerse como:

**despliegue progresivo de agentes operativos conectados**

no solo como despliegue de procesos sueltos.

## 8. Síntesis final
ORQUESTA ya no debe presentar sus pilares solo como áreas de trabajo.

Debe presentarlos como:

- agentes o familias de agentes
- capacidades operativas desplegables
- piezas de una red coherente de trabajo delegado con supervisión humana

La estructura correcta es:

**Captación activa oportunidades → Onboarding arranca clientes → Control hace visible y priorizable el sistema → Operaciones ejecuta trabajo real → Growth expande el valor generado**.
