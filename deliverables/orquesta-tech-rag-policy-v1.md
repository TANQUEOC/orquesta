# ORQUESTA Tech · Política de ingesta a RAG v1

## Objetivo
Mantener un RAG útil, limpio y gobernable.

El criterio no es meter más información.
Es meter la información correcta, en la capa correcta y con el contexto correcto.

## 1. Jerarquía de fuentes

### Nivel A · Fuente prioritaria
Fuentes canónicas que deben tener máxima prioridad:

#### General
- `MEMORY.md`

#### Memoria temática
- `memory/topics/*.md`

#### Proyectos
- `projects/*/README.md`
- `projects/*/docs/PROJECT-STATE.md`
- `projects/*/docs/ARCHITECTURE.md`

#### Documentación reusable
- `projects/*/docs/*.md`
- `projects/*/docs/pilares/*.md`

#### Skills
- `projects/*/skills/*/SKILL.md`
- `projects/*/skills/*/references/*.md`

#### Entregables maduros
- `projects/*/deliverables/**/README.md`
- paquetes operativos o comerciales ya estabilizados

### Nivel B · Fuente secundaria
Se puede ingerir, pero con menor prioridad:
- `memory/YYYY-MM-DD.md`
- casos de uso formales
- sprints paquetizados
- one-pagers comerciales
- transcripciones depuradas
- notas técnicas útiles

### Nivel C · No ingerir por defecto
- `tmp/`
- binarios
- audios
- `.git/`
- artefactos intermedios
- duplicados
- credenciales
- logs sin curar
- archivos vacíos o plantilla sin rellenar

## 2. Regla por tipo de memoria

### `MEMORY.md`
- ingerir siempre
- prioridad máxima
- usar para preferencias duraderas, reglas estables, proyectos importantes y patrones repetidos

### `memory/YYYY-MM-DD.md`
- ingerir con menor prioridad y ventana temporal
- usar para decisiones recientes, cambios relevantes, restricciones y contexto operativo reciente
- no usar como fuente principal si el mismo conocimiento ya subió a memoria temática, docs o referencias

### `memory/topics/*.md`
- ingerir siempre
- prioridad alta
- usar para memoria persistente por proyecto o dominio

## 3. Regla por proyecto
Para cada proyecto, las fuentes canónicas mínimas son:
1. `README.md`
2. `docs/PROJECT-STATE.md`
3. `docs/ARCHITECTURE.md`

Después se consideran:
4. docs específicos
5. skills
6. deliverables maduros

## 4. Regla de duplicados
Principio: una fuente principal por tema.

Si el mismo contenido vive en varios sitios:
- indexar con prioridad la fuente principal
- marcar el resto como derivado
- evitar retrieval redundante

## 5. Metadata obligatoria por chunk
Cada chunk debe llevar como mínimo:
- `domain`
- `source_type`
- `project`
- `skill`
- `pillar`
- `durability`
- `sensitivity`
- `canonical`
- `updated_at`
- `source_path`
- `source_title`

## 6. Prioridad en retrieval
### Alta
- `MEMORY.md`
- `memory/topics/*.md`
- `docs/PROJECT-STATE.md`
- `docs/ARCHITECTURE.md`
- `skills/*/references/*.md`

### Media
- `README.md`
- docs de pilar
- casos de uso
- deliverables maduros

### Baja
- `memory/YYYY-MM-DD.md`
- one-pagers
- notas operativas recientes

## 7. Reglas de chunking
### Documentos canónicos
- chunk medio
- conservar encabezados
- mantener estructura semántica

### Memoria diaria
- chunk pequeño por sección
- separar decisiones, restricciones, reglas nuevas y contexto

### Skills y references
- chunk por bloque temático
- mantener skill y referencia de origen

## 8. Política de promoción de conocimiento
Si algo aparece en memoria diaria y se repite o se vuelve estable:
- promover a `MEMORY.md` si es general y duradero
- promover a `memory/topics/*.md` si es de proyecto o dominio
- promover a `docs/` si redefine proyecto o arquitectura
- promover a `skills/*/references/` si es reusable operativamente

## 9. Exclusiones sensibles
No ingerir en RAG general:
- tokens
- credenciales
- secretos
- configs sensibles completas
- datos personales crudos
- notas privadas no depuradas

Si un contenido sensible es importante, crear versión resumida y segura.

## 10. Pipeline recomendado
1. selección de rutas permitidas
2. clasificación por canonicidad, durabilidad y sensibilidad
3. limpieza de ruido y duplicados
4. chunking con metadata
5. embeddings sobre texto limpio
6. retrieval con filtros por proyecto, pilar, skill y sensibilidad

## 11. Regla final
Sí entra al RAG si:
- es legible
- tiene valor futuro
- está bien ubicado
- no compite con otra fuente canónica
- ayuda a decidir o ejecutar mejor

No entra si:
- es ruido
- es temporal
- está duplicado
- es sensible
- no está curado
- solo sirve una vez
