# Máquina de estados · Captación → Onboarding v1

## Objetivo
Definir los estados mínimos para unir ambos pilares con una transición clara.

## Estados recomendados en Captación
- `nuevo`
- `contactado`
- `cualificado`
- `en_seguimiento`
- `cerrado_ganado`
- `cerrado_perdido`

## Estados recomendados en Onboarding
- `onboarding_pendiente`
- `datos_solicitados`
- `datos_recibidos`
- `accesos_pendientes`
- `kickoff_pendiente`
- `en_arranque`
- `handoff_a_operacion`
- `completado`

## Estado puente principal
### Trigger canónico
- `captacion.status = cerrado_ganado`

### Acción resultante
- crear `onboarding.status = onboarding_pendiente`

## Transición mínima obligatoria
1. Captación pasa a `cerrado_ganado`
2. el sistema crea registro de onboarding
3. el sistema copia datos mínimos
4. el sistema marca `onboarding_pendiente`
5. el equipo recibe señal o tarea de arranque

## Bloqueos típicos a contemplar
- datos incompletos
- falta de contacto válido
- accesos no entregados
- cliente sin disponibilidad para kickoff

## Regla operativa
No debe existir un cliente `cerrado_ganado` sin una de estas dos cosas:
- onboarding creado
- excepción humana registrada
