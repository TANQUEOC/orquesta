# ORQUESTA · Catálogo formal de agentes

## 1. Propósito del catálogo
Este catálogo describe los agentes operativos que componen ORQUESTA como arquitectura de **Agents as a Service**.

Su función es hacer visible qué capacidades reales despliega ORQUESTA, cómo se relacionan entre sí y qué trabajo ejecuta cada agente por el cliente.

## 2. Regla de lectura
Cada agente debe entenderse como una **capacidad operativa especializada**, no como un chatbot genérico ni como una automatización aislada.

La unidad de valor no es la pantalla, sino el trabajo real que el agente es capaz de ejecutar con contexto, tools, memoria y supervisión humana.

## 3. Estructura base de un agente ORQUESTA
Todo agente del catálogo debe poder describirse por estas capas:

1. misión
2. trigger principal
3. trabajo real que ejecuta
4. tools principales
5. memoria y contexto necesarios
6. approval gates
7. outputs esperados
8. métricas de control
9. relación con otros agentes

## 4. Catálogo actual

### 4.1. Agente de Captación
#### Misión
Detectar, capturar, clasificar y activar oportunidades de negocio.

#### Trigger principal
- entrada de nuevo lead
- formulario completado
- oportunidad entrante desde campaña, comunidad o fuente externa

#### Trabajo real que ejecuta
- registrar lead
- enriquecer o limpiar datos
- clasificar y priorizar
- activar respuesta inicial
- preparar handoff posterior

#### Tools principales
- formularios
- Google Sheets / CRM ligero
- Gmail
- n8n

#### Memoria y contexto
- criterios de lead válido
- prioridades comerciales
- contexto de campaña o fuente
- reglas de clasificación

#### Approval gates
- cuentas estratégicas
- respuestas delicadas
- cambios de criterio comercial

#### Outputs
- lead activado
- clasificación inicial
- siguiente paso comercial
- handoff a onboarding o seguimiento

#### Métricas
- tiempo de respuesta
- lead válido
- lead a cita
- tasa de conversión inicial

#### Relación con otros agentes
- entrega contexto al **Agente de Onboarding**
- recibe apoyo de **Venta Consultiva** cuando haga falta profundizar en la oportunidad

---

### 4.2. Agente de Venta Consultiva
#### Misión
Convertir interés comercial en oportunidad real, bien cualificada y movible hacia cierre.

#### Trigger principal
- lead con interés activo
- conversación comercial en curso
- objeción o propuesta en revisión

#### Trabajo real que ejecuta
- discovery
- cualificación de oportunidad
- priorización comercial
- preparación de argumentos
- tratamiento de objeciones
- recomendación de siguiente paso comercial

#### Tools principales
- CRM ligero o base comercial
- email
- documentación de propuesta
- secuencias de seguimiento

#### Memoria y contexto
- dolor del cliente
- punto del pipeline
- objeciones previas
- valor esperado de la cuenta

#### Approval gates
- propuestas sensibles
- compromisos de alcance
- pricing especial

#### Outputs
- oportunidad cualificada
- siguiente paso comercial claro
- propuesta mejor enfocada
- decisión de seguir, madurar o descartar

#### Métricas
- oportunidad real vs lead tibio
- avance por etapas
- objeciones resueltas
- cierre o descarte con criterio

#### Relación con otros agentes
- trabaja sobre leads captados
- prepara el paso al **Agente de Onboarding** cuando hay cierre

---

### 4.3. Agente de Onboarding
#### Misión
Convertir la venta en un arranque ordenado, trazable y rápido.

#### Trigger principal
- oportunidad cerrada
- alta de cliente aprobada

#### Trabajo real que ejecuta
- pedir datos y accesos
- generar checklist de arranque
- preparar kickoff
- registrar estado del onboarding
- detectar bloqueos iniciales

#### Tools principales
- Google Forms o ficha de arranque
- Sheets
- Docs
- Gmail
- n8n

#### Memoria y contexto
- datos del cliente
- tipo de servicio
- alcance inicial
- accesos pendientes
- responsable interno

#### Approval gates
- excepciones de arranque
- cambios de alcance
- decisiones sensibles con cliente

#### Outputs
- onboarding activo
- checklist inicial
- cliente en arranque real
- handoff a control

#### Métricas
- tiempo hasta kickoff
- tiempo hasta primer valor
- bloqueos por accesos
- onboardings en plazo

#### Relación con otros agentes
- recibe contexto de **Captación/Venta Consultiva**
- entrega visibilidad al **Agente de Control Operativo**

---

### 4.4. Agente de Control Operativo
#### Misión
Hacer visible el estado real del sistema, priorizar atención y detectar bloqueos o incidencias.

#### Trigger principal
- caso en arranque
- cambio de estado relevante
- aparición de incidencia o SLA comprometido

#### Trabajo real que ejecuta
- consolidar estados
- registrar incidencias
- detectar bloqueos
- ordenar prioridades
- generar alertas y seguimiento
- declarar casos listos para operar

#### Tools principales
- bases de control ligeras
- dashboards simples
- email o avisos
- n8n

#### Memoria y contexto
- estado operativo actual
- historial de incidencias
- prioridad del caso
- señales de carga y bloqueo

#### Approval gates
- escalados sensibles
- umbrales críticos
- cambios de prioridad relevantes

#### Outputs
- caso activo
- alerta o incidencia
- seguimiento operativo
- paso a operación

#### Métricas
- SLA cumplido
- bloqueos abiertos
- incidencias críticas
- tiempo medio de resolución

#### Relación con otros agentes
- recibe del **Agente de Onboarding**
- entrega trabajo al **Agente de Operaciones**

---

### 4.5. Agente de Operaciones
#### Misión
Convertir casos activos en trabajo real ejecutable con responsables, dependencias, bloqueos y cierre.

#### Trigger principal
- caso marcado como `listo_para_operar`
- prioridad alta validada

#### Trabajo real que ejecuta
- crear operaciones activas
- generar tareas base
- asignar responsables
- registrar dependencias
- detectar bloqueos operativos
- registrar avance y cierre

#### Tools principales
- base de operaciones
- tareas y seguimiento
- email
- n8n
- documentación de soporte

#### Memoria y contexto
- estado del caso
- prioridad
- responsable
- bloqueos activos
- siguiente acción necesaria

#### Approval gates
- cambios críticos de prioridad
- cierres sensibles
- acciones externas comprometidas

#### Outputs
- operación activa
- tareas en curso
- estado de ejecución
- cierre o escalado

#### Métricas
- operaciones abiertas
- tareas bloqueadas
- tiempo hasta cierre
- carga por responsable

#### Relación con otros agentes
- recibe del **Agente de Control Operativo**
- puede alimentar a agentes de growth, expansión o revisión según el tipo de servicio

---

### 4.6. Agente de Growth y Revenue
#### Misión
Mejorar crecimiento real del negocio con foco en revenue, no solo en volumen o vanidad de canal.

#### Trigger principal
- necesidad de crecer
- caída de conversión
- fuga de embudo
- baja retención o expansión

#### Trabajo real que ejecuta
- detectar palanca dominante
- identificar fuga principal
- proponer experimento o mejora
- ordenar métricas de negocio
- iterar sobre adquisición, activación, retención o monetización

#### Tools principales
- analítica ligera
- dashboards
- documentos de hipótesis
- secuencias de campañas y seguimiento

#### Memoria y contexto
- embudo actual
- métricas principales
- restricciones del equipo
- hipótesis previas
- aprendizajes de iteraciones anteriores

#### Approval gates
- campañas sensibles
- cambios de pricing
- decisiones de posicionamiento o marca

#### Outputs
- hipótesis prioritaria
- mejora o experimento propuesto
- palanca de growth activada
- siguiente iteración recomendada

#### Métricas
- conversión
- activación
- retención
- expansión
- revenue
- tiempo hasta impacto

#### Relación con otros agentes
- se alimenta de datos de captación, venta, onboarding, control y operación
- puede realimentar especialmente a **Captación** y **Venta Consultiva**

## 5. Agentes transversales de soporte
Además de los agentes operativos principales, ORQUESTA ya cuenta con capas especializadas que actúan como soporte transversal.

### 5.1. Agente de Análisis Ejecutivo
Aporta priorización, diagnóstico y recomendación clara cuando el problema no es ejecutar una tarea, sino decidir bien.

### 5.2. Agente de Evaluación de Calidad
Aporta revisión crítica de propuestas, respuestas, entregables y materiales antes de darlos por buenos o compartirlos con cliente.

### 5.3. Agente de Verticalización para pymes de servicios
Aterriza ORQUESTA a un tipo de negocio concreto y adapta la secuencia a la realidad operativa de una pyme de servicios.

## 6. Lectura estratégica del catálogo
Este catálogo deja claro que ORQUESTA no se limita a implantar procesos sueltos.

ORQUESTA despliega una red mínima de agentes que:
- detectan trabajo
- preparan arranques
- vigilan el sistema
- coordinan ejecución
- sostienen crecimiento

Todo ello con memoria, tools, trazabilidad y supervisión humana donde corresponda.

## 7. Evolución prevista
La evolución natural del catálogo es:

1. reforzar agentes actuales con más observabilidad y runtime real
2. verticalizar por nuevos tipos de cliente
3. ampliar agentes de soporte transversal
4. separar agentes persistentes cuando el uso lo justifique
5. convertir casos maduros en productos AaaS más explícitos

## 8. Mensaje de síntesis
ORQUESTA ya no debe presentarse como una suma de automatizaciones, dashboards y flujos.

Debe presentarse como un **catálogo de agentes operativos especializados** que ejecutan trabajo real por el cliente bajo supervisión humana.
