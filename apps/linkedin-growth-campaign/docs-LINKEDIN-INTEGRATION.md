# LinkedIn integration layer

## Estado actual
La pieza `linkedin-growth-campaign` ya tiene:
- UI de campaña
- runtime mínimo
- persistencia Supabase para campañas y publicaciones
- frontera técnica definida para integración LinkedIn

## Lo que falta para publicar en LinkedIn de verdad
1. credenciales reales de LinkedIn
2. flujo OAuth o credencial técnica equivalente
3. confirmar si se publicará en:
   - perfil personal
   - página de empresa
   - ambas
4. confirmar si habrá programación nativa o cola propia
5. mapear errores y límites de rate

## Adaptador actual
Archivo:
- `app/services/linkedin_adapter.py`

## Regla de diseño
No acoplar ORQUESTA al proveedor final. La pieza debe poder:
- generar campaña
- persistir campaña
- aprobar piezas
- publicar hoy en LinkedIn
- mañana extender a otros canales

## Recomendación
Usar una capa `channel adapter` más adelante:
- `linkedin_adapter`
- `instagram_adapter`
- `x_adapter`
- `facebook_adapter`
