# Flujo técnico · Onboarding → Control operativo y reporting v1

## Objetivo
Definir cómo se implementa técnicamente el handoff con el stack pragmático actual de ORQUESTA.

## Stack
- Google Sheets
- Gmail
- n8n

## Modelo mínimo recomendado
### Opción base
Una base con áreas o pestañas principales:
- `onboarding`
- `clientes_activos`
- `incidencias`
- `bloqueos`
- `seguimiento`

## Secuencia técnica recomendada
1. el onboarding se registra y evoluciona en su hoja o pestaña
2. el caso cambia a `en_arranque` o `handoff_a_operacion`
3. n8n detecta ese cambio de estado
4. n8n valida que el caso no exista ya como activo en control
5. n8n crea o actualiza la fila en `clientes_activos`
6. n8n copia datos mínimos y prioridad inicial
7. n8n registra un evento en `seguimiento`
8. n8n crea bloqueo o incidencia si ya nace con problema visible
9. n8n avisa internamente al responsable si aplica

## Trigger recomendado en n8n
### Evento base
- cambio o lectura periódica de filas en `onboarding`
- filtro por `status = en_arranque` o `status = handoff_a_operacion`

### Condiciones mínimas antes de crear o activar control
- client_id o identificador equivalente disponible
- responsable interno definido o pendiente explícito
- no existir ya caso activo duplicado
- contexto mínimo de arranque presente

## Acciones mínimas del flujo
- crear o actualizar fila en `clientes_activos`
- asignar `caso_activo`
- guardar referencia cruzada con onboarding
- registrar evento en `seguimiento`
- generar aviso interno si hay bloqueo o prioridad alta

## Protección anti-duplicado
Debe existir una de estas protecciones:
- campo `control_created = yes`
- validación por `client_id`
- validación por referencia cruzada onboarding-control
- tabla o pestaña de logs de activación

## Supervisión humana
Aunque el handoff sea automático, debe haber revisión humana al menos en:
- calidad del contexto trasladado
- casos con bloqueo desde el arranque
- prioridad inicial asignada
- excepciones operativas

## Resultado esperado
Cuando el cliente ya está realmente en arranque, no debe quedar invisible.
Debe entrar automáticamente en control con estado, prioridad y trazabilidad mínima.
