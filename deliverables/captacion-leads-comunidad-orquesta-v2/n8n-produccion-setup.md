# n8n producción · Captación ORQUESTA v2

## Objetivo
Dejar un workflow listo para pasar de prueba manual a operación recurrente con Google Form, Google Sheets y Gmail.

## Archivo principal
- `n8n-captacion-produccion-v1.json`

## Qué hace este workflow
1. se ejecuta cada 5 minutos
2. lee respuestas del Google Form
3. normaliza datos
4. calcula score inicial
5. guarda lead en la hoja maestra `leads`
6. envía email automático al lead
7. envía aviso interno por Gmail
8. registra un evento en `seguimiento`

## Lo que debes configurar en n8n
### 1. Credencial Google Sheets
Sustituir:
- `REPLACE_SHEETS_CREDENTIAL_ID`
- `REPLACE_SHEETS_CREDENTIAL_NAME`

### 2. Credencial Gmail
Sustituir:
- `REPLACE_GMAIL_CREDENTIAL_ID`
- `REPLACE_GMAIL_CREDENTIAL_NAME`

### 3. Spreadsheet de respuestas del formulario
Sustituir:
- `REPLACE_FORM_RESPONSES_SPREADSHEET_ID`

Ese ID será el de la hoja donde Google Forms guarda respuestas.

## Flujo recomendado de puesta en marcha
1. conectar el formulario a una hoja de respuestas de Google Forms
2. copiar el ID de esa hoja
3. importar `n8n-captacion-produccion-v1.json` en n8n
4. sustituir credenciales e ID pendiente
5. ejecutar primero en manual
6. revisar que:
   - entra la respuesta
   - se crea lead en hoja maestra
   - sale email al lead
   - sale aviso interno
   - se registra evento en `seguimiento`
7. activar workflow

## Riesgos a vigilar
- duplicados si no se filtra por clave persistente
- respuestas antiguas reimportadas si la lectura no controla histórico
- mapeo roto si cambian los títulos del formulario
- Gmail bloqueado por credenciales caducadas

## Recomendación de endurecimiento
Antes de llamarlo producción del todo, conviene añadir una de estas dos defensas:
- una hoja `processed_responses` con claves ya tratadas
- o leer solo filas nuevas con una marca persistente

## Siguiente mejora útil
Después de validar este workflow, el siguiente salto bueno es:
- mover lead score y estado a reglas más finas
- añadir owner automático
- crear resumen diario o semanal
- conectar Looker Studio con la hoja maestra
