#!/usr/bin/env python3
import argparse
import hashlib
import json
import math
import os
import re
from typing import List

import requests

BASE_URL = os.getenv('SUPABASE_BASE_URL', 'https://wdctlxomislwnonelepv.supabase.co/rest/v1')
DEFAULT_SECRET = os.getenv('SUPABASE_SECRET_KEY', '')
DIM = 1536
TOKEN_RE = re.compile(r"[\wáéíóúñüç]+", re.IGNORECASE)


def headers(secret: str):
    return {
        'apikey': secret,
        'Authorization': f'Bearer {secret}',
        'Content-Type': 'application/json',
        'Prefer': 'return=representation'
    }


def tokenize(text: str) -> List[str]:
    return [t.lower() for t in TOKEN_RE.findall(text)]


def token_index(token: str) -> int:
    h = hashlib.sha256(token.encode('utf-8')).digest()
    return int.from_bytes(h[:4], 'big') % DIM


def token_sign(token: str) -> float:
    h = hashlib.md5(token.encode('utf-8')).digest()
    return 1.0 if (h[0] % 2 == 0) else -1.0


def embed_text(text: str) -> List[float]:
    vec = [0.0] * DIM
    tokens = tokenize(text)
    if not tokens:
        return vec
    for tok in tokens:
        idx = token_index(tok)
        # tiny weight boost for repeated tokens but sublinear
        vec[idx] += token_sign(tok)
    norm = math.sqrt(sum(v * v for v in vec))
    if norm > 0:
        vec = [round(v / norm, 8) for v in vec]
    return vec


def fetch_chunks(secret: str, limit: int = 1000):
    r = requests.get(
        f"{BASE_URL}/knowledge_chunks?select=id,heading,content&order=created_at.asc&limit={limit}",
        headers=headers(secret), timeout=120
    )
    if r.status_code not in (200, 206):
        raise RuntimeError(f'fetch chunks failed: {r.status_code} {r.text[:500]}')
    return r.json()


def update_chunk_embedding(secret: str, chunk_id: str, embedding: List[float]):
    r = requests.patch(
        f"{BASE_URL}/knowledge_chunks?id=eq.{chunk_id}",
        headers=headers(secret),
        data=json.dumps({'embedding': embedding}),
        timeout=120,
    )
    if r.status_code not in (200, 204):
        raise RuntimeError(f'patch failed {chunk_id}: {r.status_code} {r.text[:500]}')


def rpc_match(secret: str, query: str, match_count: int = 5, **filters):
    payload = {'query_embedding': embed_text(query), 'match_count': match_count}
    payload.update(filters)
    r = requests.post(f"{BASE_URL}/rpc/match_knowledge_chunks", headers=headers(secret), data=json.dumps(payload), timeout=120)
    if r.status_code != 200:
        raise RuntimeError(f'rpc failed: {r.status_code} {r.text[:500]}')
    return r.json()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--secret', default=os.getenv('SUPABASE_SECRET_KEY', DEFAULT_SECRET))
    ap.add_argument('--limit', type=int, default=1000)
    ap.add_argument('--query', default=None)
    args = ap.parse_args()

    if not args.secret:
        raise RuntimeError('Missing SUPABASE secret. Set SUPABASE_SECRET_KEY or pass --secret.')

    chunks = fetch_chunks(args.secret, args.limit)
    for i, ch in enumerate(chunks, 1):
        text = (ch.get('heading') or '') + '\n\n' + (ch.get('content') or '')
        update_chunk_embedding(args.secret, ch['id'], embed_text(text))
        if i % 25 == 0:
            print(f'embedded {i}/{len(chunks)}')

    print(json.dumps({'embedded_chunks': len(chunks)}, ensure_ascii=False))

    if args.query:
        res = rpc_match(args.secret, args.query)
        print(json.dumps({'query': args.query, 'results': res[:5]}, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
