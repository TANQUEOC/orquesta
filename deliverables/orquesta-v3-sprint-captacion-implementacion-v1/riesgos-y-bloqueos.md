# Riesgos y bloqueos

## Riesgos principales
- credenciales mal configuradas en n8n
- desalineación entre la hoja de respuestas y la hoja maestra
- reprocesado de leads ya tratados
- emails duplicados o no enviados
- mensajes automáticos poco finos
- dependencia excesiva de revisión manual tras cada ejecución

## Bloqueos típicos
- no tener acceso al n8n real del cliente
- no tener identificada la response sheet correcta
- no disponer de credenciales reales de Google Sheets y Gmail
- no poder probar con entradas reales

## Regla operativa
Si no hay prueba real de punta a punta, no debe venderse como implantado.

## Mínimo de robustez exigible
- un lead no debe procesarse dos veces
- el equipo debe enterarse si algo falla
- el flujo debe dejar rastro mínimo
- el sistema no debe depender de parche constante para operar
