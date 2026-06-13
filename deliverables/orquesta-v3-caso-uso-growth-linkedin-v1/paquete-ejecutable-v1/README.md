# ORQUESTA · Paquete ejecutable v1 · Growth LinkedIn

## Qué es
Paquete canónico y portable del caso de uso:

**Agente IA especialista en creación y programación de publicaciones en LinkedIn**

## Pilar principal
- **Growth**

## Caso de uso
- **Campaña publicitaria automática de Growth LinkedIn**

## Qué contiene
- `html/` → pantalla operativa de campaña
- `runtime/` → backend desplegable/ejecutable
- `sql/` → esquema Supabase de la pieza
- `docs/` → integración y despliegue

## Estado
- UI construida
- runtime construido
- persistencia Supabase validada
- publicación real en LinkedIn aún pendiente de credenciales/permisos del canal

## Ruta principal en ORQUESTA
- `deliverables/orquesta-v3-caso-uso-growth-linkedin-v1/`

## Archivos clave
- `html/orquesta-v3-campana-publicitaria-redes-sociales-v1.html`
- `runtime/README.md`
- `runtime/Dockerfile`
- `runtime/docker-compose.yml`
- `sql/orquesta-linkedin-growth-campaign-supabase.sql`

## Uso recomendado
Este paquete está pensado para:
- mover la pieza entre entornos
- desplegar el runtime
- conectar el HTML a una URL real de API
- dejar trazabilidad clara dentro del pilar Growth
