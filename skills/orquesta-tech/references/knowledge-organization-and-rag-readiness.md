# Organización de conocimiento y preparación para RAG

## Propósito
Esta referencia fija cómo debe organizarse el conocimiento antes de conectarlo a MCP, Supabase o RAG.

## Regla base
No hace falta más volumen de información.
Hace falta mejor forma.

## Jerarquía recomendada
### 1. Proyecto
- `README.md` para visión rápida
- `docs/PROJECT-STATE.md` para estado y fuentes principales
- `docs/ARCHITECTURE.md` para arquitectura y reglas
- `deliverables/` para piezas ejecutables o compartibles
- `skills/` para conocimiento reusable por capacidad

### 2. Skill
- `SKILL.md` para cuándo usarla y cómo pensar
- `references/` para conocimiento durable y reusable

### 3. RAG futuro
Solo debe indexar fuentes principales, no ruido temporal.

## Qué sí es buena fuente para RAG
- arquitectura
- pilares
- playbooks
- referencias de skills
- casos formales maduros
- entregables operativos valiosos

## Qué no debería entrar sin filtrar
- chats crudos
- duplicados
- basura temporal
- artefactos intermedios sin valor estable
- archivos vacíos o plantilla sin rellenar

## Criterio de fuente principal
Por cada tema importante debería existir una fuente principal clara.
Los demás documentos deben ampliar, derivar o empaquetar, no competir con ella.

## Señales de mala organización
- la misma idea en 4 sitios
- un README diciendo una cosa y la arquitectura otra
- skills sin referencias reutilizables
- deliverables usados como si fueran la documentación canónica

## Señales de buena organización
- cada proyecto tiene mapa claro
- cada skill tiene referencias donde toca
- cada entregable apunta a un marco superior
- los temas importantes tienen documento fuente principal
