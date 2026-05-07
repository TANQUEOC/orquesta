# n8n · Alineación con la hoja real

## Workflow preparado
Se ha dejado un workflow base alineado a la Google Sheet real:
- Spreadsheet ID: `1Qg-KGo6i1bma04k7KL7B3pwJGrlDADtgS52dWtn3Piw`
- Hoja principal: `leads`

## Qué hace
1. genera un lead demo
2. lo añade a la hoja `leads`
3. envía email al lead
4. envía aviso interno por Gmail

## Qué debes sustituir en n8n
### Credenciales Google Sheets
- `REPLACE_SHEETS_CREDENTIAL_ID`
- `REPLACE_SHEETS_CREDENTIAL_NAME`

### Credenciales Gmail
- `REPLACE_GMAIL_CREDENTIAL_ID`
- `REPLACE_GMAIL_CREDENTIAL_NAME`

## Siguiente mejora recomendada
Después de validar este flujo manual, el siguiente paso es cambiar el disparador por uno real:
- entrada desde Google Form
- o polling de nuevas filas

## Validación mínima
- importar workflow
- configurar credenciales
- ejecutar manualmente
- comprobar fila nueva en `leads`
- comprobar email al lead
- comprobar aviso interno
