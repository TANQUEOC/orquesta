# Máquina de estados · Onboarding → Control operativo y reporting v1

## Objetivo
Definir los estados mínimos para unir ambos pilares con una transición clara.

## Estados recomendados en Onboarding
- `onboarding_pendiente`
- `datos_solicitados`
- `datos_recibidos`
- `accesos_pendientes`
- `kickoff_pendiente`
- `en_arranque`
- `handoff_a_operacion`
- `completado`

## Estados recomendados en Control
- `caso_activo`
- `seguimiento_normal`
- `bloqueo_detectado`
- `incidencia_abierta`
- `prioridad_alta`
- `cerrado`

## Estado puente principal
### Trigger canónico
- `onboarding.status = en_arranque`
  o
- `onboarding.status = handoff_a_operacion`

### Acción resultante
- crear o activar `control.status = caso_activo`

## Transición mínima obligatoria
1. Onboarding pasa a `en_arranque` o `handoff_a_operacion`
2. el sistema crea o actualiza el registro en control
3. el sistema copia datos mínimos y prioridad inicial
4. el sistema deja trazabilidad del evento
5. el equipo gana visibilidad del caso activo

## Bloqueos típicos a contemplar
- arranque incompleto
- checklist parcialmente cerrada
- accesos críticos aún pendientes
- ausencia de responsable claro

## Regla operativa
No debe existir un caso en arranque real sin una de estas dos cosas:
- registro activo en control
- excepción humana registrada
