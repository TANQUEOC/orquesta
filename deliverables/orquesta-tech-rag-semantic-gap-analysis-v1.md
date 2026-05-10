# ORQUESTA Tech · RAG semántico real · Gap analysis v1

## Estado actual
ORQUESTA ya tiene una base RAG funcional en varios niveles:

- política de ingesta curada
- esquema Supabase con `pgvector`
- fuentes y chunks poblados
- ingesta incremental
- función `match_knowledge_chunks(...)`
- embeddings operativos hash-based

## Qué sí existe ya
- retrieval por metadata y filtros
- retrieval vectorial estructuralmente operativo
- chunking y metadata razonables
- gobierno de fuentes bastante limpio

## Qué falta para llamarlo “RAG semántico real”

### 1. Embeddings semánticos de proveedor real
Ahora mismo los embeddings son deterministas por hashing.
Eso sirve como base operativa y de pruebas, pero no como semántica de calidad real.

Falta conectar uno de estos caminos:
- OpenAI embeddings
- Voyage AI embeddings
- Cohere embeddings
- modelo local equivalente si el host lo soporta de verdad

### 2. Evaluación comparativa
No basta con “embeder”.
Hace falta medir:
- si las queries devuelven chunks más relevantes
- si sube la coherencia del top 3/top 5
- si mejora especialmente en consultas abstractas o paraphraseadas

### 3. Política de proveedor
Hace falta decidir una política explícita:
- proveedor principal
- fallback
- dimensión objetivo
- coste asumible
- cuándo reembeder

### 4. Reembebido gobernado
Cuando se cambie a embeddings reales, hay que:
- reembeder toda la base existente
- mantener incrementalidad después
- evitar mezclar embeddings heterogéneos sin control

## Primer avance útil ya preparado
Se ha creado el script:

- `projects/orquesta/scripts/embed_orquesta_rag_v2_semantic.py`

## Qué hace este script
- usa proveedor seleccionable por entorno
- soporta:
  - `openai`
  - `voyage`
  - `cohere`
  - `hash` como fallback controlado
- rellena o refresca `knowledge_chunks.embedding`
- adapta longitud al vector objetivo de 1536
- puede ejecutar evaluación básica con queries reales de ORQUESTA

## Variables esperadas por proveedor
### OpenAI
- `OPENAI_API_KEY`
- opcional: `OPENAI_EMBED_MODEL`
- opcional: `OPENAI_EMBED_DIM`

### Voyage
- `VOYAGE_API_KEY`
- opcional: `VOYAGE_EMBED_MODEL`

### Cohere
- `COHERE_API_KEY`
- opcional: `COHERE_EMBED_MODEL`

### Generales
- `SUPABASE_SECRET_KEY`
- opcional: `SUPABASE_BASE_URL`
- opcional: `ORQUESTA_EMBED_PROVIDER`

## Comandos recomendados
### Dry run
```bash
python3 projects/orquesta/scripts/embed_orquesta_rag_v2_semantic.py --provider openai --dry-run
```

### Reembebido real con evaluación
```bash
python3 projects/orquesta/scripts/embed_orquesta_rag_v2_semantic.py --provider openai --evaluate
```

## Recomendación práctica
La mejor salida ahora mismo es:

1. elegir proveedor real
2. cargar credenciales por entorno
3. ejecutar dry-run
4. reembeder toda la base
5. correr evaluación sobre queries reales de ORQUESTA
6. dejar `hash` solo como fallback técnico, no como modo principal

## Veredicto
ORQUESTA no necesita rehacer el RAG desde cero.
Necesita completar la última milla: pasar de embeddings operativos hash-based a embeddings semánticos reales con evaluación y política de proveedor.
