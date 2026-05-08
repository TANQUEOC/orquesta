# Contrato de datos · Onboarding → Control operativo y reporting v1

## Objetivo
Definir qué datos pasan de Onboarding a Control y cuáles nacen ya dentro de la capa de control.

## Datos mínimos que deben pasar desde Onboarding
- client_id
- referencia a lead_id si existe
- nombre del cliente o empresa
- responsable interno
- fecha de inicio o arranque
- estado actual del onboarding
- fase o checklist actual
- bloqueos detectados
- prioridad inicial
- notas relevantes de arranque

## Datos que pueden pasar si existen
- tipo de oferta contratada
- canal de origen
- fecha prevista de kickoff
- contacto principal del cliente
- dependencias ya identificadas

## Datos que nacen en Control
- incidencia_id si aparece una incidencia
- nivel de riesgo operativo
- fecha de última actualización
- responsable actual del caso
- próximos pasos
- alertas activas
- estado de seguimiento transversal

## Regla de datos
- pasar contexto suficiente para no perder continuidad
- no duplicar documentación de arranque innecesariamente
- no mezclar datos permanentes del control con datos puramente transitorios del onboarding

## Identificador recomendado
Debe existir un identificador común o enlazable entre:
- registro de onboarding
- registro de control

Opciones mínimas viables:
- `client_id` como clave principal
- `client_id` + `lead_id` como referencia cruzada
- combinación de empresa + fecha de arranque solo como fallback temporal

## Regla de calidad
Si el arranque pasa a control con datos incompletos, debe quedar marcado explícitamente como caso con contexto parcial y requerir revisión humana.
