# Handoff funcional · Onboarding → Control operativo y reporting v1

## Idea central
Onboarding pone en marcha al cliente.
Control operativo y reporting empieza a vigilar cómo va ese arranque y qué necesita atención.

La unión entre ambas ocurre cuando el cliente deja de estar solo en preparación y pasa a requerir seguimiento operativo visible.

## Qué hace Onboarding
- recoge datos y accesos
- genera checklist de arranque
- prepara kickoff
- deja el arranque trazado
- detecta bloqueos iniciales
- prepara el handoff a operación

## Qué hace Control operativo y reporting
- da visibilidad global de estados
- registra incidencias
- detecta bloqueos abiertos
- ordena prioridades
- avisa internamente
- deja trazabilidad operativa

## Punto exacto de conexión
El punto de unión es un cambio de estado claro.

### Estado útil de salida en Onboarding
- `en_arranque`
- `handoff_a_operacion`

### Estado útil de entrada en Control
- `caso_activo`
- `seguimiento_activo`

## Evento disparador
El evento canónico es:

**el cliente ya ha entrado en fase real de arranque y necesita seguimiento visible**

Ese evento debe disparar:
1. creación o activación del caso en control
2. copia de datos de contexto útiles
3. creación de trazabilidad mínima
4. visibilidad del estado y prioridad

## Regla de separación
### Onboarding no debe hacer
- sostener el tablero operativo transversal
- registrar histórico completo de incidencias
- priorizar globalmente todos los casos activos
- ejercer como capa permanente de control

### Control no debe hacer
- pedir accesos iniciales desde cero
- recopilar toda la información de arranque
- organizar el kickoff desde el principio

## Resultado funcional esperado
La cadena debe quedar así:
1. onboarding recoge y ordena lo necesario
2. el cliente entra en arranque real
3. se dispara el handoff
4. se crea o activa el caso en control
5. se registran señales y prioridad
6. el negocio gana visibilidad y seguimiento real
