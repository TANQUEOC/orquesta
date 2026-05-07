# Cómo invocar ORQUESTA v2

## Idea simple
No hace falta invocar un comando técnico especial.

La mejor forma de activarla es pedir el trabajo indicando:

1. pilar
2. proceso
3. objetivo
4. trabajo real que el sistema debe ejecutar
5. contexto mínimo
6. entregable esperado
7. nivel de autonomía permitido

## Plantilla base
Usa esta estructura:

```text
ORQUESTA v2
Pilar: <captación | onboarding | operaciones | reporting-control | creatividad-crecimiento>
Proceso: <nombre del proceso>
Objetivo: <qué queremos conseguir>
Trabajo a ejecutar: <qué parte del trabajo hará realmente el sistema>
Contexto: <negocio, cliente, stack, restricciones>
Autonomía: <solo proponer | preparar + pedir aprobación | ejecutar dentro de límites>
Entregable: <documentación, caso de uso, flujo, dashboard, playbook, automatización, checklist>
```

## Ejemplos buenos

### 1. Crear un caso de uso
```text
ORQUESTA v2
Pilar: captación
Proceso: captación de leads para comunidad Orquesta
Objetivo: aumentar leads cualificados y responder en menos de 10 minutos
Trabajo a ejecutar: capturar, clasificar y responder al lead con seguimiento inicial
Contexto: formulario web, Gmail, Google Sheets, futura conexión con CRM
Autonomía: preparar + pedir aprobación para acciones sensibles
Entregable: caso de uso completo + flujo + KPIs + riesgos
```

### 2. Crear documentación de un pilar
```text
ORQUESTA v2
Pilar: onboarding
Proceso: onboarding de nuevos clientes de servicio
Objetivo: reducir caos tras la venta
Trabajo a ejecutar: recoger datos, solicitar accesos, preparar kickoff y dejar trazabilidad
Contexto: venta consultiva, kickoff manual, accesos por email
Autonomía: ejecutar dentro de límites
Entregable: documento del proceso + checklist + estados + SLA
```

### 3. Diseñar una automatización
```text
ORQUESTA v2
Pilar: reporting-control
Proceso: dashboard operativo semanal
Objetivo: ver atascos y SLAs incumplidos
Trabajo a ejecutar: consolidar señales, detectar incidencias y preparar revisión semanal
Contexto: datos repartidos entre n8n, email y hojas de cálculo
Autonomía: ejecutar dentro de límites
Entregable: arquitectura mínima + métricas + alertas + roadmap técnico
```

## Cómo seguir creando casos de uso
Para avanzar bien, usa esta secuencia:

### Opción A. Una orden directa
```text
ORQUESTA v2: crea el caso de uso del pilar captación para <x>
```

### Opción B. Un sprint completo
```text
ORQUESTA v2: trabaja el pilar onboarding y saca documento, flujo, checklist y métricas
```

### Opción C. Documentación estructurada
```text
ORQUESTA v2: documenta el pilar operaciones con 5 casos de uso, riesgos, stack y quick wins
```

## Tipos de entregables que puedes pedirme
- caso de uso
- documento de proceso
- playbook
- checklist
- arquitectura técnica
- skill nueva
- flujo n8n o Make
- dashboard y KPIs
- documento de Google Docs
- roadmap del pilar

## Regla práctica
Si quieres que vaya fino, empieza tus peticiones con:

**`ORQUESTA v2`**

No es obligatorio, pero me deja claro que debo trabajar con esta arquitectura y no con una respuesta genérica.

Y si el caso es importante, añade también estas dos líneas:

- `Trabajo a ejecutar:`
- `Autonomía:`

Eso obliga a diseñar Orquesta como sistema que hace trabajo real y no solo como asesor que propone cosas.

## Recomendación de uso
La forma más rentable de avanzar es:

- 1 pilar
- 1 proceso
- 1 documento de caso de uso
- 1 siguiente automatización

Así Orquesta crece ordenada y reusable.
