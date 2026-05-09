# Handoff funcional · Control operativo y reporting → Operaciones v1

## Idea central
Control operativo y reporting hace visible qué necesita atención.
Operaciones convierte esa necesidad visible en trabajo real ejecutable.

La unión entre ambas ocurre cuando un caso deja de necesitar solo seguimiento y pasa a requerir ejecución operativa concreta.

## Qué hace Control
- da visibilidad global de estados
- detecta bloqueos
- registra incidencias
- ordena prioridades
- avisa internamente
- deja trazabilidad de seguimiento

## Qué hace Operaciones
- recibe trabajo listo para ejecutar
- lo traduce en tareas u operaciones activas
- asigna responsables
- ordena dependencias
- detecta bloqueos operativos
- registra avance y cierre

## Punto exacto de conexión
El punto de unión es un cambio de estado claro.

### Estado útil de salida en Control
- `caso_activo`
- `prioridad_alta`
- `listo_para_operar`

### Estado útil de entrada en Operaciones
- `operacion_abierta`
- `tarea_inicial_creada`

## Evento disparador
El evento canónico es:

**el caso ya tiene suficiente contexto y prioridad para entrar en ejecución operativa**

Ese evento debe disparar:
1. creación o activación del registro operativo
2. generación de tareas base
3. copia de datos relevantes de contexto
4. creación de trazabilidad mínima de ejecución

## Regla de separación
### Control no debe hacer
- sostener toda la ejecución diaria
- reemplazar la gestión real del trabajo
- convertirse en la lista permanente de tareas

### Operaciones no debe hacer
- decidir sola la prioridad estratégica sin contexto de control
- reconstruir el historial del caso desde cero
- rehacer la fase de seguimiento previo

## Resultado funcional esperado
La cadena debe quedar así:
1. control detecta un caso priorizado
2. el caso se declara listo para operar
3. se dispara el handoff
4. se crea o activa la operación
5. se generan tareas y responsables
6. el trabajo entra en ejecución real
