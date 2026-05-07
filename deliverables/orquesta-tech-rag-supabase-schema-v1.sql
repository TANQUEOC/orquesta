-- ORQUESTA Tech · Supabase RAG schema v1
-- Objetivo: base curada para conocimiento, memoria temática y retrieval semántico gobernable

create extension if not exists vector;
create extension if not exists pgcrypto;

create table if not exists public.knowledge_sources (
  id uuid primary key default gen_random_uuid(),
  source_type text not null check (source_type in (
    'memory',
    'topic',
    'project_readme',
    'project_state',
    'architecture',
    'pillar',
    'skill',
    'skill_reference',
    'deliverable',
    'daily_note',
    'transcript',
    'manual'
  )),
  domain text not null,
  project text,
  pillar text,
  skill text,
  source_path text not null,
  source_title text,
  source_url text,
  version text,
  durability text not null default 'durable' check (durability in ('durable','operational','temporary')),
  sensitivity text not null default 'internal' check (sensitivity in ('public','internal','restricted')),
  canonical boolean not null default false,
  tags jsonb not null default '[]'::jsonb,
  content_hash text,
  updated_at timestamptz not null default now(),
  created_at timestamptz not null default now(),
  unique (source_path)
);

create table if not exists public.knowledge_chunks (
  id uuid primary key default gen_random_uuid(),
  source_id uuid not null references public.knowledge_sources(id) on delete cascade,
  chunk_index integer not null,
  heading text,
  content text not null,
  content_summary text,
  embedding vector(1536),
  token_count integer,
  domain text not null,
  project text,
  pillar text,
  skill text,
  source_type text not null,
  durability text not null default 'durable' check (durability in ('durable','operational','temporary')),
  sensitivity text not null default 'internal' check (sensitivity in ('public','internal','restricted')),
  canonical boolean not null default false,
  tags jsonb not null default '[]'::jsonb,
  updated_at timestamptz not null default now(),
  created_at timestamptz not null default now(),
  unique (source_id, chunk_index)
);

create table if not exists public.knowledge_entities (
  id uuid primary key default gen_random_uuid(),
  entity_type text not null,
  name text not null,
  domain text,
  project text,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  unique (entity_type, name, project)
);

create table if not exists public.knowledge_links (
  id uuid primary key default gen_random_uuid(),
  from_chunk_id uuid not null references public.knowledge_chunks(id) on delete cascade,
  to_chunk_id uuid not null references public.knowledge_chunks(id) on delete cascade,
  link_type text not null,
  weight numeric,
  metadata jsonb not null default '{}'::jsonb,
  created_at timestamptz not null default now(),
  unique (from_chunk_id, to_chunk_id, link_type)
);

create index if not exists knowledge_sources_domain_idx on public.knowledge_sources(domain);
create index if not exists knowledge_sources_project_idx on public.knowledge_sources(project);
create index if not exists knowledge_sources_skill_idx on public.knowledge_sources(skill);
create index if not exists knowledge_sources_source_type_idx on public.knowledge_sources(source_type);
create index if not exists knowledge_sources_canonical_idx on public.knowledge_sources(canonical);
create index if not exists knowledge_sources_tags_gin_idx on public.knowledge_sources using gin(tags);

create index if not exists knowledge_chunks_domain_idx on public.knowledge_chunks(domain);
create index if not exists knowledge_chunks_project_idx on public.knowledge_chunks(project);
create index if not exists knowledge_chunks_pillar_idx on public.knowledge_chunks(pillar);
create index if not exists knowledge_chunks_skill_idx on public.knowledge_chunks(skill);
create index if not exists knowledge_chunks_source_type_idx on public.knowledge_chunks(source_type);
create index if not exists knowledge_chunks_canonical_idx on public.knowledge_chunks(canonical);
create index if not exists knowledge_chunks_tags_gin_idx on public.knowledge_chunks using gin(tags);

create index if not exists knowledge_chunks_embedding_ivfflat_idx
  on public.knowledge_chunks using ivfflat (embedding vector_cosine_ops)
  with (lists = 100);

create or replace function public.match_knowledge_chunks (
  query_embedding vector(1536),
  match_count integer default 8,
  filter_domain text default null,
  filter_project text default null,
  filter_pillar text default null,
  filter_skill text default null,
  filter_source_type text default null,
  filter_sensitivity text default null,
  filter_canonical boolean default null
)
returns table (
  id uuid,
  source_id uuid,
  chunk_index integer,
  heading text,
  content text,
  content_summary text,
  domain text,
  project text,
  pillar text,
  skill text,
  source_type text,
  sensitivity text,
  canonical boolean,
  similarity float
)
language sql
as $$
  select
    kc.id,
    kc.source_id,
    kc.chunk_index,
    kc.heading,
    kc.content,
    kc.content_summary,
    kc.domain,
    kc.project,
    kc.pillar,
    kc.skill,
    kc.source_type,
    kc.sensitivity,
    kc.canonical,
    1 - (kc.embedding <=> query_embedding) as similarity
  from public.knowledge_chunks kc
  where (filter_domain is null or kc.domain = filter_domain)
    and (filter_project is null or kc.project = filter_project)
    and (filter_pillar is null or kc.pillar = filter_pillar)
    and (filter_skill is null or kc.skill = filter_skill)
    and (filter_source_type is null or kc.source_type = filter_source_type)
    and (filter_sensitivity is null or kc.sensitivity = filter_sensitivity)
    and (filter_canonical is null or kc.canonical = filter_canonical)
  order by kc.embedding <=> query_embedding
  limit match_count;
$$;

comment on table public.knowledge_sources is 'Catálogo de fuentes documentales canónicas o derivadas para RAG.';
comment on table public.knowledge_chunks is 'Chunks embebidos y etiquetados para retrieval semántico.';
comment on function public.match_knowledge_chunks is 'Búsqueda semántica con filtros por dominio, proyecto, pilar, skill y canonicidad.';
