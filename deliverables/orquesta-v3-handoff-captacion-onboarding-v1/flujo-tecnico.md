# Flujo técnico · Captación → Onboarding v1

## Objetivo
Definir cómo se implementa técnicamente el handoff con el stack pragmático actual de ORQUESTA.

## Stack
- Google Forms
- Google Sheets
- Gmail
- n8n

## Modelo mínimo recomendado
### Opción base
Una base con dos áreas o pestañas principales:
- `leads`
- `onboarding`

Y opcionalmente:
- `seguimiento`
- `catalogos`
- `logs_handoffs`

## Secuencia técnica recomendada
1. el lead entra por el formulario o canal de captación
2. Captación guarda el lead en `leads`
3. el equipo o el flujo marca el lead como `cerrado_ganado`
4. n8n detecta ese cambio de estado
5. n8n valida que no exista onboarding previo
6. n8n crea registro en `onboarding`
7. n8n copia los datos mínimos necesarios
8. n8n dispara email o formulario de arranque
9. n8n crea log de handoff
10. n8n avisa internamente al responsable

## Trigger recomendado en n8n
### Evento base
- cambio o lectura periódica de filas en `leads`
- filtro por `status = cerrado_ganado`

### Condiciones mínimas antes de crear onboarding
- email presente o contacto equivalente válido
- empresa o identificador mínimo disponible
- responsable interno definido
- no existir onboarding ya creado para ese lead

## Acciones mínimas del flujo
- crear fila nueva en `onboarding`
- rellenar datos heredados
- asignar `onboarding_pendiente`
- guardar `lead_id` o referencia cruzada
- enviar email inicial de arranque
- crear evento en `logs_handoffs` o `seguimiento`

## Protección anti-duplicado
Debe existir una de estas protecciones:
- campo `handoff_created = yes`
- tabla o pestaña `logs_handoffs`
- validación por `lead_id`
- validación por `email + fecha_cierre`

## Supervisión humana
Aunque el handoff sea automático, debe haber revisión humana al menos en:
- calidad de los datos traspasados
- tono o contenido del email inicial
- casos excepcionales o cierres especiales

## Resultado esperado
Cuando se cierre una oportunidad, el cliente no debe caer en un vacío.
Debe aparecer automáticamente en onboarding con contexto suficiente para arrancar.
