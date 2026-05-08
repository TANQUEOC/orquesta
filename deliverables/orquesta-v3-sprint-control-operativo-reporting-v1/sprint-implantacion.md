# ORQUESTA v3 · Sprint de implantación real · Control operativo y reporting v1

## Propósito
Este sprint existe para convertir el pilar de Control operativo y reporting en una capacidad operativa real de ORQUESTA.

No se trata de seguir describiendo el sistema.
Se trata de dejarlo funcionando con señales, seguimiento, incidencias, bloqueos y visibilidad mínima.

## Duración
5 días.

## Objetivo del sprint
Al terminar el sprint, la capa de control debe poder:

- ver estados operativos clave
- detectar bloqueos relevantes
- registrar incidencias
- priorizar casos
- asignar responsables
- avisar internamente
- dejar trazabilidad mínima
- mostrar una visión resumida del sistema

## Stack reutilizado
Se reutiliza la misma lógica y familia de herramientas que en Captación y Onboarding:
- Google Sheets
- Gmail
- n8n
- Looker Studio opcional en fase posterior

## Alcance del sprint por días

### Día 1 · Cierre del mapa de control
#### Objetivo
Definir qué se va a controlar y con qué criterios.

#### Trabajo
- definir estados operativos comunes
- definir fases mínimas a vigilar
- decidir bloqueos importantes
- decidir incidencias que deben registrarse
- definir prioridades y responsables

#### Entregable
- mapa de control definido
- bloqueos clave definidos
- incidencias base definidas

### Día 2 · Montaje de la base operativa
#### Objetivo
Dejar creada la base donde vivirá el control.

#### Trabajo
- crear hoja maestra o base operativa
- montar pestañas recomendadas
- definir columnas y relaciones mínimas
- definir campos de estado, prioridad, responsable y fecha

#### Tabs recomendadas
- `pipeline_resumen`
- `clientes_activos`
- `incidencias`
- `bloqueos`
- `seguimiento`
- `catalogos`

#### Entregable
- base operativa creada
- estructura mínima usable cerrada

### Día 3 · Automatización de señales
#### Objetivo
Dejar automatizada la captura de eventos importantes.

#### Trabajo
- configurar workflows n8n para detectar cambios de estado
- registrar incidencias
- marcar bloqueos
- enviar avisos internos
- conectar Captación y Onboarding con esta capa
- registrar eventos relevantes en seguimiento

#### Entregable
- workflow base de control operativo
- avisos internos mínimos funcionando
- trazabilidad inicial activa

### Día 4 · Reporting base
#### Objetivo
Tener visibilidad simple pero útil.

#### Trabajo
- crear vista resumen de estados
- crear vista de bloqueos abiertos
- crear vista de prioridades
- crear vista de carga o casos activos
- definir indicadores mínimos

#### Indicadores mínimos sugeridos
- clientes en onboarding
- bloqueos abiertos
- incidencias abiertas
- handoffs pendientes
- tiempos básicos si aplica

#### Entregable
- cuadro de control base
- reporting operativo v1 visible

### Día 5 · Prueba real y cierre operativo
#### Objetivo
Validar el sistema con casos reales o simulados.

#### Trabajo
- probar varios cambios de estado
- probar creación de incidencia
- probar detección de bloqueo
- probar avisos internos
- revisar claridad del tablero
- corregir fallos
- documentar uso mínimo y backlog v2

#### Entregable
- capa de control v1 validada
- incidencias corregidas
- criterio operativo documentado

## Definición de éxito
El sprint se considera bien cerrado cuando se puede:

- ver qué clientes o casos están activos
- ver en qué estado está cada uno
- detectar bloqueos
- registrar incidencias
- recibir avisos internos
- entender qué necesita atención primero

## Definición de no terminado
No debe considerarse implantado de verdad si:

- solo existe una hoja bonita sin uso real
- no hay avisos internos funcionando
- no hay prueba real o simulada
- no hay responsables claros
- no se distingue entre estado normal y bloqueo
