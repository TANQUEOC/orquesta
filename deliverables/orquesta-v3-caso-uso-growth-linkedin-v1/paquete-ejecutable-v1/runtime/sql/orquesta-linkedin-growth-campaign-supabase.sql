-- Proyecto Supabase ORQUESTA
-- Runtime mínimo de la campaña publicitaria automática de Growth LinkedIn

create extension if not exists pgcrypto;

-- Reutiliza el modelo MVP ya diseñado para LinkedIn.
-- Fuente canónica actual:
-- deliverables/orquesta-v3-caso-uso-growth-linkedin-v1/05-sql-inicial-mvp.sql

-- Copia mínima operacional aquí para despliegue rápido.

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
  current_status text not null default 'draft' check (current_status in ('draft','pending_approval','approved','scheduled','published','publication_error','cancelled','rescheduled')),
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

create table if not exists linkedin_approval_events (
  id uuid primary key default gen_random_uuid(),
  publication_id uuid not null references linkedin_publications(id) on delete cascade,
  reviewer text not null,
  decision text not null check (decision in ('approved', 'rejected', 'changes_requested')),
  comments text,
  created_at timestamptz not null default now()
);

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
