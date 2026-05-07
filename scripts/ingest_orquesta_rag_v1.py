#!/usr/bin/env python3
import argparse
import hashlib
import json
import os
import re
from pathlib import Path
from typing import List, Dict, Optional

import requests

WORKSPACE = Path('/data/.openclaw/workspace')
BASE_URL = os.getenv('SUPABASE_BASE_URL', 'https://wdctlxomislwnonelepv.supabase.co/rest/v1')
DEFAULT_SECRET = os.getenv('SUPABASE_SECRET_KEY', '')

SOURCES = [
    ('MEMORY.md', dict(source_type='memory', domain='general', project=None, pillar=None, skill=None, durability='durable', sensitivity='internal', canonical=True)),
    ('memory/topics/orquesta.md', dict(source_type='topic', domain='orquesta', project='orquesta', pillar=None, skill=None, durability='durable', sensitivity='internal', canonical=True)),
    ('memory/topics/systema-operativo-tanque.md', dict(source_type='topic', domain='general', project=None, pillar=None, skill='orquesta-tech', durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/README.md', dict(source_type='project_readme', domain='orquesta', project='orquesta', pillar=None, skill=None, durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/docs/PROJECT-STATE.md', dict(source_type='project_state', domain='orquesta', project='orquesta', pillar=None, skill=None, durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/docs/ARCHITECTURE.md', dict(source_type='architecture', domain='orquesta', project='orquesta', pillar=None, skill=None, durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/docs/PRINCIPIOS-AGENTIC-AIAS-PARA-ORQUESTA.md', dict(source_type='architecture', domain='orquesta', project='orquesta', pillar=None, skill='orquesta-tech', durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/docs/ORQUESTA-v3-PILARES-AGENTIC.md', dict(source_type='pillar', domain='orquesta', project='orquesta', pillar='all', skill=None, durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/docs/METODOLOGIA-ORQUESTA-1-SEMANA-1-PROCESO.md', dict(source_type='manual', domain='orquesta', project='orquesta', pillar=None, skill=None, durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/skills/orquesta-tech/SKILL.md', dict(source_type='skill', domain='orquesta', project='orquesta', pillar='tech', skill='orquesta-tech', durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/skills/orquesta-tech/references/architecture-patterns.md', dict(source_type='skill_reference', domain='orquesta', project='orquesta', pillar='tech', skill='orquesta-tech', durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/skills/orquesta-tech/references/agentic-production-checklist.md', dict(source_type='skill_reference', domain='orquesta', project='orquesta', pillar='tech', skill='orquesta-tech', durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/skills/orquesta-tech/references/orquesta-tech-scope.md', dict(source_type='skill_reference', domain='orquesta', project='orquesta', pillar='tech', skill='orquesta-tech', durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/skills/orquesta-tech/references/solo-founder-agentic-stack.md', dict(source_type='skill_reference', domain='orquesta', project='orquesta', pillar='tech', skill='orquesta-tech', durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/skills/orquesta-tech/references/knowledge-organization-and-rag-readiness.md', dict(source_type='skill_reference', domain='orquesta', project='orquesta', pillar='tech', skill='orquesta-tech', durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/docs/pilares/01-captacion.md', dict(source_type='pillar', domain='orquesta', project='orquesta', pillar='captacion', skill='orquesta-captacion-leads', durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/skills/orquesta-captacion-leads/SKILL.md', dict(source_type='skill', domain='orquesta', project='orquesta', pillar='captacion', skill='orquesta-captacion-leads', durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/skills/orquesta-captacion-leads/references/captacion-v3-reference.md', dict(source_type='skill_reference', domain='orquesta', project='orquesta', pillar='captacion', skill='orquesta-captacion-leads', durability='durable', sensitivity='internal', canonical=True)),
    ('projects/orquesta/deliverables/orquesta-v3-sprint-captacion-implementacion-v1/README.md', dict(source_type='deliverable', domain='orquesta', project='orquesta', pillar='captacion', skill='orquesta-captacion-leads', durability='operational', sensitivity='internal', canonical=False)),
    ('projects/orquesta/deliverables/orquesta-v3-sprint-captacion-implementacion-v1/sprint-implantacion.md', dict(source_type='deliverable', domain='orquesta', project='orquesta', pillar='captacion', skill='orquesta-captacion-leads', durability='operational', sensitivity='internal', canonical=False)),
]


def clean_text(text: str) -> str:
    text = text.replace('\r\n', '\n').replace('\r', '\n')
    text = re.sub(r'\n{3,}', '\n\n', text)
    return text.strip()


def source_title(path: str) -> str:
    p = Path(path)
    return p.stem.replace('-', ' ').replace('_', ' ').strip()


def split_sections(text: str) -> List[Dict[str, str]]:
    text = clean_text(text)
    lines = text.split('\n')
    sections = []
    current_heading = 'Inicio'
    buff = []
    heading_re = re.compile(r'^(#{1,6})\s+(.*)')
    for line in lines:
        m = heading_re.match(line)
        if m:
            if buff:
                body = '\n'.join(buff).strip()
                if body:
                    sections.append({'heading': current_heading, 'content': body})
            current_heading = m.group(2).strip()
            buff = []
        else:
            buff.append(line)
    if buff:
        body = '\n'.join(buff).strip()
        if body:
            sections.append({'heading': current_heading, 'content': body})
    if not sections and text:
        sections.append({'heading': 'Inicio', 'content': text})
    return sections


def chunk_section(heading: str, content: str, max_chars: int = 1800) -> List[Dict[str, str]]:
    paras = [p.strip() for p in content.split('\n\n') if p.strip()]
    chunks = []
    cur = ''
    for p in paras:
        candidate = p if not cur else cur + '\n\n' + p
        if len(candidate) <= max_chars:
            cur = candidate
        else:
            if cur:
                chunks.append({'heading': heading, 'content': cur})
            if len(p) <= max_chars:
                cur = p
            else:
                parts = [p[i:i+max_chars] for i in range(0, len(p), max_chars)]
                for part in parts[:-1]:
                    chunks.append({'heading': heading, 'content': part})
                cur = parts[-1]
    if cur:
        chunks.append({'heading': heading, 'content': cur})
    return chunks


def summarize(content: str, max_len: int = 240) -> str:
    one = re.sub(r'\s+', ' ', content).strip()
    return one[:max_len] + ('…' if len(one) > max_len else '')


def sha(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def headers(secret: str) -> Dict[str, str]:
    return {
        'apikey': secret,
        'Authorization': f'Bearer {secret}',
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
    }


def upsert_source(secret: str, rel_path: str, meta: Dict) -> Dict:
    path = str(WORKSPACE / rel_path)
    text = clean_text(Path(path).read_text())
    payload = {
        'source_type': meta['source_type'],
        'domain': meta['domain'],
        'project': meta.get('project'),
        'pillar': meta.get('pillar'),
        'skill': meta.get('skill'),
        'source_path': rel_path,
        'source_title': source_title(rel_path),
        'source_url': None,
        'version': 'v1',
        'durability': meta['durability'],
        'sensitivity': meta['sensitivity'],
        'canonical': meta['canonical'],
        'tags': [x for x in [meta['domain'], meta.get('project'), meta.get('pillar'), meta.get('skill')] if x],
        'content_hash': sha(text),
    }
    url = f"{BASE_URL}/knowledge_sources?on_conflict=source_path"
    r = requests.post(url, headers=headers(secret), data=json.dumps(payload), timeout=60)
    if r.status_code not in (200, 201):
        raise RuntimeError(f'source upsert failed {rel_path}: {r.status_code} {r.text}')
    return r.json()[0]


def delete_existing_chunks(secret: str, source_id: str):
    r = requests.delete(f"{BASE_URL}/knowledge_chunks?source_id=eq.{source_id}", headers=headers(secret), timeout=60)
    if r.status_code not in (200, 204):
        raise RuntimeError(f'delete chunks failed {source_id}: {r.status_code} {r.text}')


def insert_chunks(secret: str, source: Dict, rel_path: str, meta: Dict) -> int:
    text = clean_text((WORKSPACE / rel_path).read_text())
    sections = split_sections(text)
    chunks = []
    idx = 0
    for sec in sections:
        for ch in chunk_section(sec['heading'], sec['content']):
            chunks.append({
                'source_id': source['id'],
                'chunk_index': idx,
                'heading': ch['heading'],
                'content': ch['content'],
                'content_summary': summarize(ch['content']),
                'token_count': max(1, len(ch['content']) // 4),
                'domain': meta['domain'],
                'project': meta.get('project'),
                'pillar': meta.get('pillar'),
                'skill': meta.get('skill'),
                'source_type': meta['source_type'],
                'durability': meta['durability'],
                'sensitivity': meta['sensitivity'],
                'canonical': meta['canonical'],
                'tags': [x for x in [meta['domain'], meta.get('project'), meta.get('pillar'), meta.get('skill')] if x],
            })
            idx += 1
    if not chunks:
        return 0
    r = requests.post(f"{BASE_URL}/knowledge_chunks", headers=headers(secret), data=json.dumps(chunks), timeout=120)
    if r.status_code not in (200, 201):
        raise RuntimeError(f'insert chunks failed {rel_path}: {r.status_code} {r.text[:500]}')
    return len(r.json())


def count_table(secret: str, table: str) -> int:
    r = requests.get(f"{BASE_URL}/{table}?select=count", headers={**headers(secret), 'Prefer': 'count=exact'}, timeout=60)
    if r.status_code not in (200, 206):
        raise RuntimeError(f'count failed {table}: {r.status_code} {r.text}')
    data = r.json()
    return data[0]['count'] if data else 0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--secret', default=os.getenv('SUPABASE_SECRET_KEY', DEFAULT_SECRET))
    args = ap.parse_args()

    if not args.secret:
        raise RuntimeError('Missing SUPABASE secret. Set SUPABASE_SECRET_KEY or pass --secret.')

    processed = []
    for rel_path, meta in SOURCES:
        if not (WORKSPACE / rel_path).exists():
            continue
        src = upsert_source(args.secret, rel_path, meta)
        delete_existing_chunks(args.secret, src['id'])
        chunk_count = insert_chunks(args.secret, src, rel_path, meta)
        processed.append({'path': rel_path, 'source_id': src['id'], 'chunks': chunk_count})

    print(json.dumps({
        'processed_sources': processed,
        'knowledge_sources_count': count_table(args.secret, 'knowledge_sources'),
        'knowledge_chunks_count': count_table(args.secret, 'knowledge_chunks'),
    }, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
