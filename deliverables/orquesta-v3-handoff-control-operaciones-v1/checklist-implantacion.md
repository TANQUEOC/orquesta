# Checklist de implantación · Handoff Control operativo y reporting → Operaciones v1

## Diseño
- [ ] Estados de Control definidos
- [ ] Estados de Operaciones definidos
- [ ] Trigger de handoff validado
- [ ] Datos mínimos de traspaso definidos
- [ ] Responsable operativo definido

## Datos
- [ ] Existe identificador común o enlazable
- [ ] Campos mínimos disponibles en Control
- [ ] Campos nuevos definidos en Operaciones
- [ ] Reglas de validación mínima definidas

## Automatización
- [ ] Workflow n8n preparado
- [ ] Lectura de cambio de estado validada
- [ ] Creación o activación de operación validada
- [ ] Generación de tarea inicial validada
- [ ] Registro en seguimiento operativo validado
- [ ] Aviso interno validado si aplica

## Protección
- [ ] Regla anti-duplicado definida
- [ ] Casos excepcionales contemplados
- [ ] Revisión humana mínima definida

## Prueba
- [ ] Caso real o simulado listo para operar ejecutado
- [ ] Operación creada correctamente
- [ ] Datos heredados correctos
- [ ] Tarea inicial creada
- [ ] Sin duplicado no deseado

## Criterio de cierre
- [ ] `control.listo_para_operar` crea o activa `operaciones.operacion_abierta`
- [ ] El caso no pierde continuidad entre control y ejecución
- [ ] El equipo recibe una señal clara de arranque operativo
