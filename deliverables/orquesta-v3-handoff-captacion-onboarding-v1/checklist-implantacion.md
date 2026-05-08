# Checklist de implantación · Handoff Captación → Onboarding v1

## Diseño
- [ ] Estados de Captación definidos
- [ ] Estados de Onboarding definidos
- [ ] Trigger de handoff validado
- [ ] Datos mínimos de traspaso definidos
- [ ] Responsable interno definido

## Datos
- [ ] Existe identificador común o enlazable
- [ ] Campos mínimos disponibles en Captación
- [ ] Campos nuevos definidos en Onboarding
- [ ] Reglas de validación mínima definidas

## Automatización
- [ ] Workflow n8n preparado
- [ ] Lectura de cambio de estado validada
- [ ] Creación de registro en onboarding validada
- [ ] Copia de datos validada
- [ ] Email o solicitud inicial validada
- [ ] Log de handoff validado

## Protección
- [ ] Regla anti-duplicado definida
- [ ] Casos excepcionales contemplados
- [ ] Revisión humana mínima definida

## Prueba
- [ ] Caso de cierre real o simulado ejecutado
- [ ] Onboarding creado correctamente
- [ ] Datos heredados correctos
- [ ] Aviso interno correcto
- [ ] Sin duplicado no deseado

## Criterio de cierre
- [ ] El paso `cerrado_ganado` crea `onboarding_pendiente`
- [ ] El cliente no pierde contexto entre comercial y arranque
- [ ] El equipo recibe una señal clara de inicio
