# ORQUESTA v3 · Cadena maestra ampliada · Captación → Onboarding → Control operativo y reporting → Operaciones v1

## Qué es esta pieza
Este documento define la primera cadena vertebral operativa completa de ORQUESTA en su versión ampliada.

No describe módulos aislados.
Describe cómo se conectan para formar un sistema continuo que va desde la oportunidad hasta la ejecución real.

## La cadena completa
La secuencia base queda así:

1. **Captación**
2. **Handoff Captación → Onboarding**
3. **Onboarding**
4. **Handoff Onboarding → Control operativo y reporting**
5. **Control operativo y reporting**
6. **Handoff Control operativo y reporting → Operaciones**
7. **Operaciones**

## Propósito de la cadena
Esta cadena permite que ORQUESTA no solo capte oportunidades y arranque clientes, sino que además:
- les dé continuidad operativa
- mantenga visibilidad y seguimiento
- convierta los casos priorizados en trabajo real ejecutado

## 1. Captación
### Qué hace
- recibe leads
- los registra
- los clasifica
- responde de forma inicial
- permite seguimiento comercial
- convierte oportunidades en clientes ganados

### Estado de salida relevante
- `cerrado_ganado`

### Qué no debe hacer
- pedir todos los accesos del proyecto
- organizar el arranque operativo completo
- sostener la ejecución diaria

## 2. Handoff Captación → Onboarding
### Trigger canónico
- `captacion.status = cerrado_ganado`

### Acción
- crea `onboarding.status = onboarding_pendiente`

### Qué pasa aquí
- se crea el registro de onboarding
- se trasladan datos mínimos útiles
- se conserva el contexto comercial relevante
- se lanza la preparación del arranque

## 3. Onboarding
### Qué hace
- recoge datos faltantes
- pide accesos y materiales
- genera checklist de arranque
- prepara kickoff
- deja visible el estado del arranque
- detecta bloqueos iniciales
- prepara la transición a seguimiento operativo

### Estados relevantes
- `onboarding_pendiente`
- `datos_solicitados`
- `datos_recibidos`
- `accesos_pendientes`
- `kickoff_pendiente`
- `en_arranque`
- `handoff_a_operacion`

### Qué no debe hacer
- sostener el tablero operativo permanente
- convertirse en histórico de incidencias
- ejecutar el trabajo diario del servicio

## 4. Handoff Onboarding → Control operativo y reporting
### Trigger canónico
- `onboarding.status = en_arranque`
  o
- `onboarding.status = handoff_a_operacion`

### Acción
- crea o activa `control.status = caso_activo`

### Qué pasa aquí
- el caso entra en visibilidad operativa
- se trasladan datos de contexto de arranque
- se registra trazabilidad mínima
- se activa seguimiento del caso

## 5. Control operativo y reporting
### Qué hace
- da visibilidad global de estados
- registra incidencias
- detecta bloqueos abiertos
- ordena prioridades
- genera seguimiento operativo
- avisa internamente cuando hace falta
- permite entender qué necesita atención primero

### Estados relevantes
- `caso_activo`
- `seguimiento_normal`
- `bloqueo_detectado`
- `incidencia_abierta`
- `prioridad_alta`
- `listo_para_operar`
- `cerrado`

### Qué no debe hacer
- pedir accesos iniciales desde cero
- rehacer el onboarding
- sustituir la ejecución real del trabajo

## 6. Handoff Control operativo y reporting → Operaciones
### Trigger canónico
- `control.status = listo_para_operar`
  o
- `control.status = prioridad_alta` con criterio operativo válido

### Acción
- crea o activa `operaciones.status = operacion_abierta`

### Qué pasa aquí
- el caso deja de estar solo observado y pasa a ejecución
- se crean o activan unidades operativas
- se trasladan prioridad, bloqueos e incidencias relevantes
- se registra trazabilidad mínima de ejecución

## 7. Operaciones
### Qué hace
- recibe trabajo listo para ejecutar
- lo traduce en tareas u operaciones activas
- asigna responsables
- ordena dependencias
- detecta bloqueos operativos
- registra avance y cierre
- mantiene continuidad entre seguimiento y ejecución

### Estados relevantes
- `operacion_abierta`
- `tarea_inicial_creada`
- `en_ejecucion`
- `bloqueada`
- `pendiente_validacion`
- `cerrada`

### Qué no debe hacer
- decidir sola la prioridad estratégica sin contexto
- reconstruir el historial del caso desde cero
- sustituir futuras capas de crecimiento o creatividad

## Regla de continuidad
Ningún caso debe pasar a la siguiente fase sin dejar una huella clara en la siguiente capa.

Eso significa:
- ningún `cerrado_ganado` sin onboarding creado o excepción registrada
- ningún `en_arranque` sin caso activo en control o excepción registrada
- ningún `listo_para_operar` sin operación abierta o excepción registrada

## Reglas de diseño de la cadena
La cadena completa debe cumplir estas reglas:

1. **Trigger explícito** en cada transición
2. **Datos mínimos definidos** para cada handoff
3. **Estados claros** y no ambiguos
4. **Protección anti-duplicado**
5. **Trazabilidad mínima** en cada paso
6. **Supervisión humana** en excepciones, bloqueos y casos sensibles

## Stack pragmático actual
Esta cadena está pensada para operar, en su v1, sobre:
- Google Forms
- Google Sheets
- Gmail
- n8n

## Modelo técnico mínimo recomendado
### Áreas o pestañas base
- `leads`
- `onboarding`
- `clientes_activos`
- `incidencias`
- `bloqueos`
- `seguimiento`
- `operaciones_activas`
- `tareas`
- `dependencias`
- `bloqueos_operativos`
- `seguimiento_operativo`
- `catalogos`

## Secuencia end-to-end resumida
1. entra lead
2. se registra y clasifica
3. se cierra como ganado
4. se crea onboarding
5. se piden datos y accesos
6. se prepara kickoff
7. el caso entra en arranque real
8. se activa el caso en control
9. se prioriza y se declara listo para operar
10. se abre operación
11. se generan tareas y responsables
12. se ejecuta el trabajo con trazabilidad

## Qué gana ORQUESTA con esta cadena
Con esta cadena ORQUESTA deja de ser una colección de automatizaciones sueltas.
Empieza a comportarse como un sistema empresarial orquestado de extremo a extremo.

### Beneficios reales
- menos pérdida de contexto
- menos caos entre fases
- mejor trazabilidad
- mejor continuidad entre comercial, arranque, seguimiento y ejecución
- mejor base para abrir después nuevas capas como creatividad y crecimiento

## Siguiente paso natural
Con esta cadena ya definida, el siguiente paso estructural de ORQUESTA sería:
- **Creatividad y crecimiento**

Pero ya no como pieza aislada, sino conectada a una columna vertebral operativa real.

## Frase síntesis
**Captación consigue y activa la oportunidad. Onboarding convierte ese cierre en arranque ordenado. Control operativo y reporting da visibilidad, prioridad y seguimiento a lo que ya está en marcha. Operaciones convierte esa visibilidad en trabajo real ejecutado. Esa es la primera columna vertebral completa de ORQUESTA.**
