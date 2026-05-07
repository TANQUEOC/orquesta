# Checklist de producción agentic

## Antes de llamar algo “implantado”
- ¿el trabajo real a ejecutar está definido?
- ¿las entradas y salidas están claras?
- ¿hay trazabilidad mínima?
- ¿hay manejo de errores?
- ¿hay control de coste?
- ¿hay approval gates si toca?
- ¿hay prueba real extremo a extremo?

## Observabilidad mínima
- logs por paso
- registro de errores
- visibilidad de herramientas llamadas
- estado final de cada ejecución

## Seguridad operativa mínima
- nada sensible se ejecuta sin humano si es irreversible
- credenciales fuera de documentos públicos
- webhooks y accesos con control
- límites para evitar loops o ejecuciones desbocadas

## Criterio de calidad
Si solo funciona en demo, no está listo.
Si no deja rastro, no está listo.
Si no puede explicarse qué hizo y por qué, no está listo.
