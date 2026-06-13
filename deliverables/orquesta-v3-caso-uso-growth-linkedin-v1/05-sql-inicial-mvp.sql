-- ORQUESTA
-- Caso de uso Growth: Agente IA especialista en creación y programación de publicaciones en LinkedIn
-- SQL inicial MVP

create extension if not exists pgcrypto;

-- =========================================================
-- 1. LOTES / PROMPTS DE ORIGEN
-- =========================================================

create table if not exists linkedin_prompt_runs (
  id uuid primary key default gen_random_uuid(),
  prompt_text text not null,
  prompt_version text not null default 'v1',
  topic text,
  target_audience text,
  tone text,
  style text,
  language_code text not null default 'es',
  cadence_text text,
  requested_publications integer not null default 1 check (requested_publications > 0),
  use_hashtags boolean not null default true,
  include_cta boolean not null default true,
  brand_constraints text,
  parsed_params jsonb,
  run_status text not null default 'received' check (run_status in ('received', 'parsed', 'failed', 'completed')),
  created_by text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  failure_reason text
);

create index if not exists idx_linkedin_prompt_runs_status on linkedin_prompt_runs(run_status);
create index if not exists idx_linkedin_prompt_runs_created_at on linkedin_prompt_runs(created_at desc);

-- =========================================================
-- 2. PUBLICACIONES
-- =========================================================

create table if not exists linkedin_publications (
  id uuid primary key default gen_random_uuid(),
  prompt_run_id uuid not null references linkedin_prompt_runs(id) on delete cascade,
  publication_number integer not null default 1 check (publication_number > 0),
  internal_title text,
  topic text not null,
  target_audience text,
  tone text not null,
  style text not null,
  language_code text not null default 'es',
  content text not null,
  content_short text,
  hashtags jsonb not null default '[]'::jsonb,
  cta_text text,
  channel text not null default 'linkedin',
  publication_type text not null default 'post' check (publication_type in ('post', 'article', 'carousel', 'image_post')),
  scheduled_for timestamptz,
  published_at timestamptz,
  current_status text not null default 'draft' check (current_status in (
    'draft',
    'pending_approval',
    'approved',
    'scheduled',
    'published',
    'publication_error',
    'cancelled',
    'rescheduled'
  )),
  requires_approval boolean not null default true,
  approved_by text,
  approved_at timestamptz,
  created_by text not null,
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  last_error text,
  metadata jsonb not null default '{}'::jsonb,
  constraint uq_linkedin_publication_number unique (prompt_run_id, publication_number)
);

create index if not exists idx_linkedin_publications_prompt_run on linkedin_publications(prompt_run_id);
create index if not exists idx_linkedin_publications_status on linkedin_publications(current_status);
create index if not exists idx_linkedin_publications_scheduled_for on linkedin_publications(scheduled_for);
create index if not exists idx_linkedin_publications_channel on linkedin_publications(channel);

-- =========================================================
-- 3. HISTORIAL DE ESTADOS
-- =========================================================

create table if not exists linkedin_publication_status_history (
  id uuid primary key default gen_random_uuid(),
  publication_id uuid not null references linkedin_publications(id) on delete cascade,
  previous_status text,
  new_status text not null,
  changed_by text not null,
  changed_at timestamptz not null default now(),
  change_origin text not null default 'system' check (change_origin in ('system', 'agent', 'human', 'linkedin_api')),
  detail text
);

create index if not exists idx_linkedin_status_history_publication on linkedin_publication_status_history(publication_id);
create index if not exists idx_linkedin_status_history_changed_at on linkedin_publication_status_history(changed_at desc);

-- =========================================================
-- 4. ASSETS VISUALES
-- =========================================================

create table if not exists linkedin_publication_assets (
  id uuid primary key default gen_random_uuid(),
  publication_id uuid not null references linkedin_publications(id) on delete cascade,
  asset_type text not null default 'image' check (asset_type in ('image', 'video', 'carousel_cover', 'document')),
  asset_role text not null default 'primary' check (asset_role in ('primary', 'alternative', 'thumbnail')),
  source_type text not null default 'placeholder' check (source_type in ('placeholder', 'generated', 'uploaded', 'library')),
  storage_url text,
  storage_ref text,
  prompt_image text,
  asset_status text not null default 'pending' check (asset_status in ('pending', 'generated', 'selected', 'error', 'cancelled')),
  created_at timestamptz not null default now(),
  updated_at timestamptz not null default now(),
  error_detail text,
  metadata jsonb not null default '{}'::jsonb
);

create index if not exists idx_linkedin_assets_publication on linkedin_publication_assets(publication_id);
create index if not exists idx_linkedin_assets_status on linkedin_publication_assets(asset_status);

-- =========================================================
-- 5. APROBACIONES
-- =========================================================

create table if not exists linkedin_approval_events (
  id uuid primary key default gen_random_uuid(),
  publication_id uuid not null references linkedin_publications(id) on delete cascade,
  reviewer text not null,
  decision text not null check (decision in ('approved', 'rejected', 'changes_requested')),
  comments text,
  created_at timestamptz not null default now()
);

create index if not exists idx_linkedin_approval_events_publication on linkedin_approval_events(publication_id);

-- =========================================================
-- 6. DELIVERY / INTEGRACION LINKEDIN
-- =========================================================

create table if not exists linkedin_delivery_events (
  id uuid primary key default gen_random_uuid(),
  publication_id uuid not null references linkedin_publications(id) on delete cascade,
  event_type text not null check (event_type in ('schedule_attempt', 'schedule_success', 'publish_attempt', 'publish_success', 'cancel_attempt', 'cancel_success', 'error')),
  provider text not null default 'linkedin',
  remote_post_id text,
  remote_status text,
  response_payload jsonb,
  error_code text,
  error_message text,
  happened_at timestamptz not null default now(),
  created_by text not null default 'system'
);

create index if not exists idx_linkedin_delivery_publication on linkedin_delivery_events(publication_id);
create index if not exists idx_linkedin_delivery_happened_at on linkedin_delivery_events(happened_at desc);

-- =========================================================
-- 7. VISTAS UTILES MVP
-- =========================================================

create or replace view vw_linkedin_publications_overview as
select
  p.id,
  p.prompt_run_id,
  p.publication_number,
  p.internal_title,
  p.topic,
  p.language_code,
  p.current_status,
  p.scheduled_for,
  p.published_at,
  p.requires_approval,
  p.created_by,
  p.created_at,
  p.updated_at,
  p.last_error,
  r.run_status as prompt_run_status,
  r.target_audience,
  r.cadence_text
from linkedin_publications p
join linkedin_prompt_runs r on r.id = p.prompt_run_id;

-- =========================================================
-- 8. NOTAS DE USO
-- =========================================================

-- Flujo mínimo recomendado del MVP:
-- 1. crear linkedin_prompt_runs
-- 2. crear N linkedin_publications asociadas
-- 3. registrar estado inicial en linkedin_publication_status_history
-- 4. asociar asset placeholder o generado en linkedin_publication_assets
-- 5. aprobar/rechazar en linkedin_approval_events
-- 6. registrar intentos de integración en linkedin_delivery_events
