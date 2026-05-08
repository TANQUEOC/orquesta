# Checklist de implantación · Handoff Onboarding → Control operativo y reporting v1

## Diseño
- [ ] Estados de Onboarding definidos
- [ ] Estados de Control definidos
- [ ] Trigger de handoff validado
- [ ] Datos mínimos de traspaso definidos
- [ ] Responsable interno definido

## Datos
- [ ] Existe identificador común o enlazable
- [ ] Campos mínimos disponibles en Onboarding
- [ ] Campos nuevos definidos en Control
- [ ] Reglas de validación mínima definidas

## Automatización
- [ ] Workflow n8n preparado
- [ ] Lectura de cambio de estado validada
- [ ] Creación o activación del caso en control validada
- [ ] Copia de datos validada
- [ ] Registro en seguimiento validado
- [ ] Aviso interno validado si aplica

## Protección
- [ ] Regla anti-duplicado definida
- [ ] Casos excepcionales contemplados
- [ ] Revisión humana mínima definida

## Prueba
- [ ] Caso real o simulado de arranque ejecutado
- [ ] Caso activo creado correctamente
- [ ] Datos heredados correctos
- [ ] Seguimiento correcto
- [ ] Sin duplicado no deseado

## Criterio de cierre
- [ ] `onboarding.en_arranque` o `handoff_a_operacion` crea o activa `control.caso_activo`
- [ ] El cliente no pierde visibilidad al salir de onboarding
- [ ] El equipo recibe una señal clara de seguimiento operativo
