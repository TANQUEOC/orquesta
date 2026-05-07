# ORQUESTA v2 · Captación · Implementación base

## Objetivo
Montar una primera versión operativa del proceso de captación usando herramientas Google y n8n.

## Herramientas elegidas
- Google Form
- Google Sheets
- Gmail
- Google Docs
- Google Drive
- Looker Studio
- n8n

## Entregables de esta implementación base
- estructura de datos de leads
- plantilla de emails
- workflow base para n8n
- checklist de puesta en marcha
- especificación de reporting en Looker Studio

## Orden de montaje
1. Crear Google Sheet base
2. Crear pestañas y columnas
3. Crear Google Form conectado
4. Crear workflow n8n
5. Conectar Gmail
6. Configurar emails automáticos
7. Crear dashboard simple en Looker Studio
8. Validar con leads de prueba

## SLA recomendado
- respuesta inicial automática: inmediata
- revisión humana de leads valiosos: menos de 4 horas en horario laboral

## Convención operativa
- un lead = una fila principal en `leads`
- cada cambio relevante = una fila en `seguimiento`
- si hay duplicado, no se borra: se marca

## Validación mínima
Antes de considerarlo operativo:
- 3 leads de prueba completos
- 1 aviso interno enviado
- 1 email automático correcto
- dashboard mostrando datos
- deduplicación básica funcionando
