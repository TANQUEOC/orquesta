# ORQUESTA v3 · Sprint de implantación real · Captación v1

## Propósito
Este sprint existe para convertir el pilar de Captación en una capacidad operativa real de ORQUESTA.

No se trata de seguir diseñando el sistema.
Se trata de dejarlo funcionando de extremo a extremo con datos, automatización, seguimiento y control mínimo.

## Duración
5 días.

## Objetivo del sprint
Al terminar el sprint, la captación debe poder:

- recibir leads reales
- guardar respuestas correctamente
- clasificarlos
- disparar una respuesta automática
- avisar internamente
- registrar seguimiento
- evitar duplicados básicos
- quedar lista para operar con estabilidad razonable

## Alcance del sprint por días

### Día 1 · Cierre de la entrada real
#### Objetivo
Dejar bien conectada la entrada del sistema.

#### Trabajo
- confirmar que el Google Form sigue correcto
- conectar el Form con su hoja real de respuestas
- obtener el Spreadsheet ID real
- sustituir `REPLACE_FORM_RESPONSES_SPREADSHEET_ID`
- revisar columnas y estructura final de datos

#### Entregable
- formulario conectado
- sheet real identificada
- estructura de entrada cerrada

### Día 2 · Cierre del workflow de n8n
#### Objetivo
Dejar importado y configurado el workflow real.

#### Trabajo
- importar `n8n-captacion-produccion-v1.json` en el n8n del cliente
- sustituir credenciales reales de Google Sheets y Gmail
- revisar nodos uno por uno
- validar lectura de la hoja correcta
- validar escritura en la sheet maestra correcta

#### Entregable
- workflow cargado
- credenciales reales puestas
- flujo técnicamente operativo

### Día 3 · Anti-duplicados y control mínimo
#### Objetivo
Evitar reprocesado y fragilidad operativa.

#### Trabajo
- crear mecanismo persistente anti-duplicados
- usar una pestaña `processed_responses` o marcador persistente equivalente
- definir criterio de qué cuenta como procesado
- registrar error básico si falla algo

#### Entregable
- control anti-duplicados activo
- criterio de procesamiento definido
- base mínima de robustez

### Día 4 · Prueba real extremo a extremo
#### Objetivo
Validar el sistema completo con entradas reales.

#### Trabajo
- enviar 2 o 3 formularios reales de prueba
- comprobar lectura correcta
- comprobar scoring o clasificación
- comprobar escritura en `leads`
- comprobar escritura en `seguimiento`
- comprobar email automático al lead
- comprobar email interno de aviso
- detectar y corregir fallos

#### Entregable
- test E2E completado
- incidencias corregidas
- flujo validado en condiciones reales

### Día 5 · Cierre operativo
#### Objetivo
Dejar Captación v1 lista para uso estable.

#### Trabajo
- revisar tiempos de ejecución
- revisar errores posibles
- revisar textos finales de emails
- documentar funcionamiento
- documentar qué revisar si falla
- documentar qué queda fuera de alcance
- definir siguiente mejora prioritaria

#### Entregable
- Captación v1 operativa
- checklist de operación
- backlog de mejora v2

## Definición de éxito
El sprint se considera correctamente cerrado cuando ocurre esto:

- entra un lead real
- se procesa una sola vez
- se clasifica bien
- recibe email
- el equipo recibe aviso interno
- queda trazado
- no depende de tocarlo a mano cada vez

## Definición de no terminado
No debe considerarse implantado de verdad si:

- solo existe documentación
- el flujo no fue probado de punta a punta
- sigue reprocesando entradas
- la respuesta automática no sale
- los estados no quedan registrados
- depende de parche manual constante
