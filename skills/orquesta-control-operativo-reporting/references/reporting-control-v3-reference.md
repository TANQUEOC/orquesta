# Referencia reusable · Reporting y control v3

## Fuentes principales
- pilar v3: `projects/orquesta/docs/pilares/04-reporting-control.md`
- caso formal: `projects/orquesta/deliverables/orquesta-v2-caso-uso-control-operativo-reporting-v1/`
- skill de apoyo relevante: `orquesta-control-total`

## Regla del pilar
Reporting y control no es solo mostrar datos.
Debe consolidar señales, detectar anomalías y preparar criterio para decidir.

## Qué piezas debe tener un sistema mínimo de control
- mapa de estados
- eventos registrados
- métricas accionables
- alertas por umbral
- responsable por escalado
- cadencia de revisión

## Qué reutilizar como patrón
1. separación entre vista ejecutiva y vista operativa
2. eventos y estados antes que dashboards complejos
3. alertas con responsable y criterio de cierre
4. fallback humano cuando una automatización crítica falla
