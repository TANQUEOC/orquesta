# Deploy de la pieza HTML + runtime

## HTML
Archivo:
- `deliverables/orquesta-v3-campana-publicitaria-redes-sociales-v1.html`

## Runtime
Carpeta:
- `apps/linkedin-growth-campaign/`

## Opción recomendada
Servir el HTML desde la web principal y exponer el runtime en una URL propia, por ejemplo:
- `https://compan-ia.lovable.app/campana-redes-sociales`
- `https://api.compan-ia.lovable.app/linkedin-growth-campaign`

## Cómo apuntar el HTML al runtime
Antes de cargar la página, define:
```html
<script>
  window.ORQUESTA_API_BASE = 'https://api.tu-dominio.com';
</script>
```

Alternativa rápida en navegador:
```js
localStorage.setItem('orquesta_api_base', 'https://api.tu-dominio.com')
```

## Puesta en marcha del runtime
```bash
cd apps/linkedin-growth-campaign
cp .env.example .env
# rellenar SUPABASE_SERVICE_ROLE_KEY
bash deploy-docker.sh
```

## Verificación mínima
- `GET /health`
- `GET /runtime/meta`
- `POST /campaigns/preview`
- `POST /campaigns/launch`

## Estado del canal LinkedIn
La app ya persiste campañas en Supabase, pero la publicación real en LinkedIn sigue pendiente de credenciales y permisos del canal.
