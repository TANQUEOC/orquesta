# ORQUESTA · Mapa de relaciones entre agentes, handoffs y approval gates

## 1. Objetivo del documento
Este documento hace visible la arquitectura relacional de ORQUESTA como sistema de **Agents as a Service**.

No se limita a listar agentes. Explica:
- cómo se relacionan entre sí
- qué handoffs se producen entre capas
- qué información debe pasar
- dónde debe intervenir la supervisión humana

## 2. Principio general
La red de agentes de ORQUESTA debe leerse como una cadena de trabajo delegado con control humano.

La regla marco es:

- cada agente ejecuta una parte real del trabajo
- cada agente deja contexto suficiente para el siguiente
- cada handoff debe ser explícito
- toda acción sensible debe poder pasar por approval gate

## 3. Cadena principal de agentes
La secuencia operativa principal actual es:

1. **Agente de Captación**
2. **Agente de Venta Consultiva**
3. **Agente de Onboarding**
4. **Agente de Control Operativo**
5. **Agente de Operaciones**
6. **Agente de Growth y Revenue**

Los agentes transversales de soporte son:
- **Agente de Análisis Ejecutivo**
- **Agente de Evaluación de Calidad**
- **Agente de Verticalización para pymes de servicios**

## 4. Mapa simplificado de relaciones

### Flujo principal
`Captación → Venta Consultiva → Onboarding → Control Operativo → Operaciones → Growth/Revenue`

### Agentes de soporte
- `Análisis Ejecutivo` puede intervenir sobre cualquier capa cuando haya que decidir, priorizar o secuenciar.
- `Evaluación de Calidad` puede intervenir antes de compartir una propuesta, respuesta, entregable o cierre importante.
- `Verticalización pymes de servicios` adapta el diseño completo al contexto de implantación del cliente.

## 5. Handoffs principales

### 5.1. Captación → Venta Consultiva
#### Qué activa el handoff
- lead con interés o cualificación suficiente

#### Qué debe pasar
- datos del lead
- fuente de entrada
- dolor o necesidad detectada
- prioridad inicial
- notas comerciales relevantes

#### Qué debe producir el siguiente agente
- cualificación más profunda
- decisión de seguir, madurar o descartar

#### Approval gate humano recomendado
- cuentas estratégicas
- casos con alto valor potencial
- leads ambiguos con posible coste de oportunidad alto

---

### 5.2. Venta Consultiva → Onboarding
#### Qué activa el handoff
- oportunidad cerrada o cliente ganado

#### Qué debe pasar
- datos de contacto relevantes
- servicio vendido
- alcance inicial
- objeciones o riesgos comerciales conocidos
- responsable interno
- fecha de cierre

#### Qué debe producir el siguiente agente
- arranque estructurado
- checklist de onboarding
- solicitud de datos y accesos

#### Approval gate humano recomendado
- validación final de alcance
- condiciones comerciales especiales
- cuentas con excepciones de arranque

---

### 5.3. Onboarding → Control Operativo
#### Qué activa el handoff
- cliente en arranque real
- onboarding con suficiente contexto para seguimiento visible

#### Qué debe pasar
- `client_id`
- estado del onboarding
- checklist actual
- bloqueos iniciales
- responsable interno
- prioridad inicial
- notas de arranque

#### Qué debe producir el siguiente agente
- caso activo visible
- señales de seguimiento
- prioridad operativa
- alertas si aplica

#### Approval gate humano recomendado
- onboarding con contexto incompleto
- accesos críticos sin resolver
- clientes sensibles o con alto impacto

---

### 5.4. Control Operativo → Operaciones
#### Qué activa el handoff
- caso marcado como `listo_para_operar`
- prioridad alta con criterio operativo válido

#### Qué debe pasar
- `client_id`
- estado actual del caso
- prioridad
- bloqueos activos
- incidencias abiertas
- siguiente paso recomendado
- responsable actual

#### Qué debe producir el siguiente agente
- operación activa
- tarea inicial o unidad de ejecución
- responsable operativo
- seguimiento de avance

#### Approval gate humano recomendado
- prioridad alta no estándar
- operación sin responsable claro
- incidencias abiertas que afecten alcance, calidad o reputación

---

### 5.5. Operaciones → Growth y Revenue
#### Qué activa el handoff
- servicio estabilizado
- necesidad de crecer, expandir, retener o mejorar monetización
- datos suficientes para detectar fugas o palancas de crecimiento

#### Qué debe pasar
- estado del servicio
- datos básicos de rendimiento
- fricciones observadas
- señales de retención, expansión o caída
- contexto del cliente y capacidad del equipo

#### Qué debe producir el siguiente agente
- hipótesis de growth
- mejora prioritaria
- experimento o ajuste con foco en revenue

#### Approval gate humano recomendado
- cambios de pricing
- campañas sensibles
- cambios de posicionamiento o narrativa

## 6. Approval gates transversales
Hay acciones que deben pasar por supervisión humana independientemente del pilar.

### 6.1. Acciones externas sensibles
- envío de emails delicados
- propuestas comerciales finales
- publicaciones públicas
- mensajes a terceros
- cobros o acciones económicas

### 6.2. Acciones irreversibles o destructivas
- borrados
- cierres definitivos
- modificaciones estructurales críticas
- acciones con impacto legal o reputacional

### 6.3. Acciones con alto coste de error
- cambios de prioridad estratégicos
- respuestas comerciales en cuentas clave
- escalados de crisis
- validaciones de alcance o compromiso

## 7. Relación de agentes transversales

### 7.1. Agente de Análisis Ejecutivo
Puede intervenir:
- antes de abrir un nuevo frente
- para decidir prioridad entre capas
- para secuenciar roadmap
- para resolver tradeoffs

### 7.2. Agente de Evaluación de Calidad
Puede intervenir:
- antes de enviar propuestas
- antes de compartir entregables con cliente
- antes de cerrar un caso importante
- cuando haya dudas sobre claridad, foco o rigor

### 7.3. Agente de Verticalización pymes de servicios
Puede intervenir:
- al inicio de un diseño de implantación
- cuando haga falta adaptar toda la cadena a la realidad de una pyme de servicios
- cuando haya que simplificar stack, estados o procesos para un equipo pequeño

## 8. Reglas de calidad del handoff
Todo handoff serio en ORQUESTA debe cumplir estas reglas:

1. **tiene trigger explícito**
2. **deja datos mínimos definidos**
3. **no obliga al siguiente agente a reconstruir contexto desde cero**
4. **deja trazabilidad visible**
5. **permite intervención humana si el contexto es incompleto o sensible**

## 9. Reglas de diseño de approval gates
Los approval gates no deben usarse como burocracia ciega.

Se usan para proteger:
- reputación
- alcance
- coste
- daño operativo
- decisiones humanas no delegables

La regla práctica es:

- si el error tiene bajo coste y es reversible, el agente puede avanzar
- si el error tiene alto coste o impacto externo, el humano debe revisar

## 10. Síntesis del mapa
La arquitectura de ORQUESTA no debe verse como una serie de automatizaciones sueltas.

Debe verse como una red de agentes conectados por handoffs explícitos y gobernados por approval gates donde el riesgo lo exige.

La cadena operativa resultante es:

**Captación detecta → Venta Consultiva cualifica → Onboarding arranca → Control visibiliza → Operaciones ejecuta → Growth expande**

Todo ello bajo una capa transversal de:
- análisis ejecutivo
- evaluación de calidad
- verticalización por tipo de cliente

## 11. Cierre
Este mapa convierte ORQUESTA en una arquitectura más gobernable y explicable.

Ya no solo dice qué agentes existen. También deja visible:
- cómo colaboran
- qué se pasan
- dónde puede romperse la cadena
- dónde debe intervenir el humano
