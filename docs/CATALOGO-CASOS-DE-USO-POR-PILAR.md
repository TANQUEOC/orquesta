# ORQUESTA · Catálogo de casos de uso por pilar

## Qué es este documento
Este catálogo organiza los casos de uso de ORQUESTA por pilar, para que no queden como entregables sueltos y se vea mejor qué parte del sistema cubre cada uno.

Su función es ayudar a:
- ubicar cada caso dentro de la arquitectura ORQUESTA
- ver huecos por pilar
- priorizar siguientes desarrollos
- mantener continuidad entre documentación, skills y entregables

---

## 1. Pilar de Captación

### Casos registrados
- **Captación de leads / captación operativa v2**
  - ruta principal: `deliverables/orquesta-v2-caso-uso-captacion-v1/caso-de-uso.md`
  - artefactos relacionados:
    - `deliverables/orquesta-v2-caso-uso-captacion-v1/checklist-implantacion.md`
    - `deliverables/orquesta-v2-caso-uso-captacion-v1/resumen-ejecutivo.md`

### Lectura rápida
Caso orientado a detectar, capturar, clasificar y activar oportunidades de negocio.

---

## 2. Pilar de Onboarding

### Casos registrados
- **Onboarding operativo v2**
  - ruta principal: `deliverables/orquesta-v2-caso-uso-onboarding-v1/caso-de-uso.md`
  - artefactos relacionados:
    - `deliverables/orquesta-v2-caso-uso-onboarding-v1/checklist-implantacion.md`
    - `deliverables/orquesta-v2-caso-uso-onboarding-v1/resumen-ejecutivo.md`
- **ORQUESTAonboarding MVP técnico**
  - ruta principal: `deliverables/orquesta-onboarding-mvp-instalacion-tecnica-v1.md`

### Lectura rápida
Casos orientados a convertir una venta en un arranque claro, trazable y rápido.

---

## 3. Pilar de Operaciones

### Casos registrados
- **[pendiente de caso formal dominante]**

### Lectura rápida
El pilar está definido arquitectónicamente, pero todavía no tiene un caso de uso tan asentado como Captación u Onboarding.

---

## 4. Pilar de Reporting y Control

### Casos registrados
- **Control operativo y reporting v2**
  - ruta principal: `deliverables/orquesta-v2-caso-uso-control-operativo-reporting-v1/caso-de-uso.md`
  - artefactos relacionados:
    - `deliverables/orquesta-v2-caso-uso-control-operativo-reporting-v1/checklist-implantacion.md`
    - `deliverables/orquesta-v2-caso-uso-control-operativo-reporting-v1/resumen-ejecutivo.md`
- **Dashboards de control operativo**
  - ruta principal: `deliverables/orquesta-control-operativo-dashboards-v1/README.md`

### Lectura rápida
Casos orientados a hacer visible el estado real del sistema, detectar bloqueos y ordenar prioridades.

---

## 5. Pilar de Growth

### Casos registrados
- **Agente IA especialista en creación y programación de publicaciones en LinkedIn**
  - ruta principal: `deliverables/ORQUESTA-CASO-DE-USO-AGENTE-LINKEDIN-v1.md`
  - paquete ejecutable: `deliverables/orquesta-v3-caso-uso-growth-linkedin-v1/paquete-ejecutable-v1/README.md`
  - encaje principal: **Growth**
  - pilares de soporte: **Tech transversal** y **Control**

### Lectura rápida
Caso orientado a sostener crecimiento mediante generación, planificación, almacenamiento y programación de publicaciones en LinkedIn con trazabilidad de estados.

---

## 6. Pilar Tech transversal

### Casos registrados
- **Soporte transversal a múltiples casos**
  - rutas relacionadas:
    - `deliverables/ORQUESTA-CHECKLIST-TECNICO-POR-PILAR-v1.md`
    - `docs/ARCHITECTURE.md`
    - `docs/AGENTES-ORQUESTA-CATALOGO.md`

### Lectura rápida
No actúa como caso de uso comercial aislado, sino como capa que permite memoria, tools, runtime, observabilidad, approval gates e integraciones para todos los demás pilares.

---

## Resumen ejecutivo
### Más asentados hoy
- Captación
- Onboarding
- Reporting y Control

### Nuevo caso registrado en Growth
- Agente IA para creación y programación de publicaciones en LinkedIn

### Huecos más visibles
- Operaciones todavía necesita un caso de uso dominante más cerrado
- Growth tiene ya este caso, pero aún puede ampliarse con otros de distribución, campañas o content factory completa
