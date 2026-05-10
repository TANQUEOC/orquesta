#!/usr/bin/env python3
import argparse
import hashlib
import json
import math
import os
import re
import sys
from typing import Dict, List, Optional, Tuple

import requests

BASE_URL = os.getenv('SUPABASE_BASE_URL', 'https://wdctlxomislwnonelepv.supabase.co/rest/v1')
SUPABASE_SECRET = os.getenv('SUPABASE_SECRET_KEY', '')
DEFAULT_DIM = 1536
TOKEN_RE = re.compile(r"[\wáéíóúñüç]+", re.IGNORECASE)


class EmbeddingProvider:
    name = 'base'
    dim = DEFAULT_DIM
    semantic = False

    def embed(self, text: str) -> List[float]:
        raise NotImplementedError


class HashEmbeddingProvider(EmbeddingProvider):
    name = 'hash'
    dim = DEFAULT_DIM
    semantic = False

    def tokenize(self, text: str) -> List[str]:
        return [t.lower() for t in TOKEN_RE.findall(text)]

    def embed(self, text: str) -> List[float]:
        vec = [0.0] * self.dim
        tokens = self.tokenize(text)
        if not tokens:
            return vec
        for tok in tokens:
            h1 = hashlib.sha256(tok.encode('utf-8')).digest()
            idx = int.from_bytes(h1[:4], 'big') % self.dim
            sign = 1.0 if (hashlib.md5(tok.encode('utf-8')).digest()[0] % 2 == 0) else -1.0
            vec[idx] += sign
        norm = math.sqrt(sum(v * v for v in vec))
        return [round(v / norm, 8) for v in vec] if norm > 0 else vec


class OpenAIEmbeddingProvider(EmbeddingProvider):
    name = 'openai'
    semantic = True

    def __init__(self, model: str, api_key: str, dim: int = DEFAULT_DIM, base_url: str = 'https://api.openai.com/v1'):
        self.model = model
        self.api_key = api_key
        self.dim = dim
        self.base_url = base_url.rstrip('/')

    def embed(self, text: str) -> List[float]:
        payload = {'model': self.model, 'input': text}
        if self.model == 'text-embedding-3-small' and self.dim:
            payload['dimensions'] = self.dim
        r = requests.post(
            f'{self.base_url}/embeddings',
            headers={'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'},
            data=json.dumps(payload),
            timeout=120,
        )
        if r.status_code != 200:
            raise RuntimeError(f'openai embeddings failed: {r.status_code} {r.text[:500]}')
        data = r.json()['data'][0]['embedding']
        return data


class VoyageEmbeddingProvider(EmbeddingProvider):
    name = 'voyage'
    semantic = True

    def __init__(self, model: str, api_key: str, dim: int = 1024):
        self.model = model
        self.api_key = api_key
        self.dim = dim

    def embed(self, text: str) -> List[float]:
        r = requests.post(
            'https://api.voyageai.com/v1/embeddings',
            headers={'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'},
            data=json.dumps({'model': self.model, 'input': [text], 'input_type': 'document'}),
            timeout=120,
        )
        if r.status_code != 200:
            raise RuntimeError(f'voyage embeddings failed: {r.status_code} {r.text[:500]}')
        return r.json()['data'][0]['embedding']


class CohereEmbeddingProvider(EmbeddingProvider):
    name = 'cohere'
    semantic = True

    def __init__(self, model: str, api_key: str, dim: int = 1024):
        self.model = model
        self.api_key = api_key
        self.dim = dim

    def embed(self, text: str) -> List[float]:
        r = requests.post(
            'https://api.cohere.com/v2/embed',
            headers={'Authorization': f'Bearer {self.api_key}', 'Content-Type': 'application/json'},
            data=json.dumps({'model': self.model, 'texts': [text], 'input_type': 'search_document', 'embedding_types': ['float']}),
            timeout=120,
        )
        if r.status_code != 200:
            raise RuntimeError(f'cohere embeddings failed: {r.status_code} {r.text[:500]}')
        return r.json()['embeddings']['float'][0]


def choose_provider(name: str) -> EmbeddingProvider:
    name = (name or '').strip().lower()
    if name == 'openai':
        api_key = os.getenv('OPENAI_API_KEY', '')
        if not api_key:
            raise RuntimeError('OPENAI_API_KEY is missing.')
        model = os.getenv('OPENAI_EMBED_MODEL', 'text-embedding-3-small')
        dim = int(os.getenv('OPENAI_EMBED_DIM', str(DEFAULT_DIM)))
        return OpenAIEmbeddingProvider(model=model, api_key=api_key, dim=dim)
    if name == 'voyage':
        api_key = os.getenv('VOYAGE_API_KEY', '')
        if not api_key:
            raise RuntimeError('VOYAGE_API_KEY is missing.')
        model = os.getenv('VOYAGE_EMBED_MODEL', 'voyage-3-large')
        return VoyageEmbeddingProvider(model=model, api_key=api_key)
    if name == 'cohere':
        api_key = os.getenv('COHERE_API_KEY', '')
        if not api_key:
            raise RuntimeError('COHERE_API_KEY is missing.')
        model = os.getenv('COHERE_EMBED_MODEL', 'embed-v4.0')
        return CohereEmbeddingProvider(model=model, api_key=api_key)
    if name in ('hash', '', 'fallback'):
        return HashEmbeddingProvider()
    raise RuntimeError(f'Unknown provider: {name}')


def pad_or_trim(vec: List[float], dim: int) -> List[float]:
    if len(vec) == dim:
        return vec
    if len(vec) > dim:
        return vec[:dim]
    return vec + ([0.0] * (dim - len(vec)))


def headers(secret: str) -> Dict[str, str]:
    return {
        'apikey': secret,
        'Authorization': f'Bearer {secret}',
        'Content-Type': 'application/json',
        'Prefer': 'return=representation',
    }


def fetch_chunks(secret: str, limit: int, only_missing: bool = False) -> List[Dict]:
    query = 'select=id,heading,content,embedding,project,pillar,skill,source_type,canonical&order=created_at.asc&limit=' + str(limit)
    if only_missing:
        query += '&embedding=is.null'
    r = requests.get(f'{BASE_URL}/knowledge_chunks?{query}', headers=headers(secret), timeout=120)
    if r.status_code not in (200, 206):
        raise RuntimeError(f'fetch chunks failed: {r.status_code} {r.text[:500]}')
    return r.json()


def update_chunk_embedding(secret: str, chunk_id: str, embedding: List[float]):
    r = requests.patch(
        f'{BASE_URL}/knowledge_chunks?id=eq.{chunk_id}',
        headers=headers(secret),
        data=json.dumps({'embedding': embedding}),
        timeout=120,
    )
    if r.status_code not in (200, 204):
        raise RuntimeError(f'patch failed {chunk_id}: {r.status_code} {r.text[:500]}')


def rpc_match(secret: str, query_embedding: List[float], match_count: int = 5, **filters):
    payload = {'query_embedding': query_embedding, 'match_count': match_count}
    payload.update(filters)
    r = requests.post(f'{BASE_URL}/rpc/match_knowledge_chunks', headers=headers(secret), data=json.dumps(payload), timeout=120)
    if r.status_code != 200:
        raise RuntimeError(f'rpc failed: {r.status_code} {r.text[:500]}')
    return r.json()


def evaluate(secret: str, provider: EmbeddingProvider, dim: int) -> Dict:
    tests = [
        ('captación de leads con n8n y gmail', {'filter_project': 'orquesta'}),
        ('handoff entre onboarding y control operativo', {'filter_project': 'orquesta'}),
        ('arquitectura agentic y observabilidad', {'filter_project': 'orquesta'}),
    ]
    out = []
    for query, filters in tests:
        query_vec = pad_or_trim(provider.embed(query), dim)
        results = rpc_match(secret, query_vec, match_count=3, **filters)
        out.append({
            'query': query,
            'top_results': [
                {
                    'project': r.get('project'),
                    'pillar': r.get('pillar'),
                    'skill': r.get('skill'),
                    'source_type': r.get('source_type'),
                    'heading': r.get('heading'),
                    'similarity': r.get('similarity'),
                }
                for r in results[:3]
            ],
        })
    return {'provider': provider.name, 'semantic': provider.semantic, 'tests': out}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--provider', default=os.getenv('ORQUESTA_EMBED_PROVIDER', 'hash'))
    ap.add_argument('--secret', default=SUPABASE_SECRET)
    ap.add_argument('--limit', type=int, default=1000)
    ap.add_argument('--only-missing', action='store_true')
    ap.add_argument('--dry-run', action='store_true')
    ap.add_argument('--evaluate', action='store_true')
    args = ap.parse_args()

    if not args.secret:
        raise RuntimeError('Missing SUPABASE secret. Set SUPABASE_SECRET_KEY or pass --secret.')

    provider = choose_provider(args.provider)
    target_dim = DEFAULT_DIM

    chunks = fetch_chunks(args.secret, args.limit, only_missing=args.only_missing)
    if args.dry_run:
        print(json.dumps({
            'provider': provider.name,
            'semantic': provider.semantic,
            'chunks_candidate_count': len(chunks),
            'target_dim': target_dim,
        }, ensure_ascii=False, indent=2))
        return

    for i, ch in enumerate(chunks, 1):
        text = ((ch.get('heading') or '') + '\n\n' + (ch.get('content') or '')).strip()
        vec = pad_or_trim(provider.embed(text), target_dim)
        update_chunk_embedding(args.secret, ch['id'], vec)
        if i % 25 == 0:
            print(f'embedded {i}/{len(chunks)} with provider={provider.name}')

    out = {
        'provider': provider.name,
        'semantic': provider.semantic,
        'embedded_chunks': len(chunks),
        'target_dim': target_dim,
    }
    if args.evaluate:
        out['evaluation'] = evaluate(args.secret, provider, target_dim)
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(f'ERROR: {e}', file=sys.stderr)
        sys.exit(1)
