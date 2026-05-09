# Máquina de estados · Control operativo y reporting → Operaciones v1

## Objetivo
Definir los estados mínimos para unir ambos pilares con una transición clara.

## Estados recomendados en Control
- `caso_activo`
- `seguimiento_normal`
- `bloqueo_detectado`
- `incidencia_abierta`
- `prioridad_alta`
- `listo_para_operar`
- `cerrado`

## Estados recomendados en Operaciones
- `operacion_abierta`
- `tarea_inicial_creada`
- `en_ejecucion`
- `bloqueada`
- `pendiente_validacion`
- `cerrada`

## Estado puente principal
### Trigger canónico
- `control.status = listo_para_operar`
  o
- `control.status = prioridad_alta` con criterio operativo válido

### Acción resultante
- crear o activar `operaciones.status = operacion_abierta`

## Transición mínima obligatoria
1. Control pasa a `listo_para_operar`
2. el sistema crea o actualiza el registro en operaciones
3. el sistema genera tareas base o unidad operativa inicial
4. el sistema deja trazabilidad del evento
5. el equipo gana visibilidad de ejecución real

## Bloqueos típicos a contemplar
- prioridad sin contexto suficiente
- responsable operativo no definido
- dependencias críticas aún abiertas
- incidencia abierta que impide ejecutar

## Regla operativa
No debe existir un caso `listo_para_operar` sin una de estas dos cosas:
- operación abierta
- excepción humana registrada
