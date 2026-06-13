# ORQUESTA · Campaña publicitaria en redes sociales · v1

## Qué es
Pantalla/prototipo HTML de la pieza de Growth para lanzar campañas de publicaciones en redes sociales desde ORQUESTA.

## Objetivo
Dar al usuario una superficie única donde pueda:
- añadir el prompt de creación
- elegir periodicidad
- definir número de publicaciones
- seleccionar canal
- subir imágenes a mano o pedir generación automática
- activar aprobación humana
- lanzar la ejecución del agente

## Estado actual
- diseñado con look & feel cercano a `compan-ia.lovable.app`
- preparado para LinkedIn como canal inicial
- estructurado para escalar a selector multicanal más adelante
- pensado como pieza integrable en Lovable/React o como base de componente real

## Archivos
- `orquesta-v3-campana-publicitaria-redes-sociales-v1.html`

## Qué falta para volverlo runtime real
1. conectar el botón `Lanzar ejecución` con backend
2. persistir el formulario en `linkedin_prompt_runs`
3. disparar el parser del prompt
4. generar lote de publicaciones
5. guardar estados y assets
6. añadir approval gate funcional
7. integrar programación/publicación real en LinkedIn
