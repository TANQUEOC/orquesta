from __future__ import annotations

import json
import urllib.error
import urllib.request
from typing import Any

from app.core.config import settings
from app.schemas.campaign import CampaignLaunchRequest, CampaignPreviewResponse


class PersistenceResult(dict):
    pass


def _headers(prefer: str | None = None) -> dict[str, str]:
    headers = {
        "Content-Type": "application/json",
        "apikey": settings.supabase_service_role_key,
        "Authorization": f"Bearer {settings.supabase_service_role_key}",
    }
    if prefer:
        headers["Prefer"] = prefer
    return headers


def _post(path: str, payload: Any, prefer: str | None = None) -> Any:
    url = settings.supabase_url.rstrip("/") + "/rest/v1/" + path.lstrip("/")
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers=_headers(prefer=prefer),
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        raw = response.read().decode("utf-8", "replace")
        return json.loads(raw) if raw else None


async def persist_campaign(payload: CampaignLaunchRequest, preview: CampaignPreviewResponse) -> PersistenceResult:
    if not settings.supabase_service_role_key:
        return PersistenceResult(
            persisted=False,
            prompt_run_id=None,
            note="No hay SUPABASE_SERVICE_ROLE_KEY cargada; se devuelve preview sin persistencia real.",
        )

    prompt_run_payload = {
        "prompt_text": payload.prompt,
        "prompt_version": "v1",
        "topic": preview.prompt_normalized.get("topic"),
        "target_audience": None,
        "tone": payload.tone,
        "style": payload.style,
        "language_code": payload.language_code,
        "cadence_text": payload.periodicity,
        "requested_publications": payload.publication_count,
        "use_hashtags": True,
        "include_cta": True,
        "brand_constraints": payload.extra_instructions,
        "parsed_params": preview.prompt_normalized,
        "run_status": "parsed",
        "created_by": payload.creator,
    }

    try:
        prompt_run_response = _post("linkedin_prompt_runs", prompt_run_payload, prefer="return=representation")
        prompt_run = (prompt_run_response or [None])[0]
        prompt_run_id = prompt_run["id"] if prompt_run else None
        if not prompt_run_id:
            return PersistenceResult(
                persisted=False,
                prompt_run_id=None,
                note="Supabase respondió, pero no devolvió prompt_run_id.",
            )

        publication_rows = []
        status_rows = []
        asset_rows = []
        for publication in preview.publications:
            publication_rows.append(
                {
                    "prompt_run_id": prompt_run_id,
                    "publication_number": publication.publication_number,
                    "internal_title": publication.internal_title,
                    "topic": publication.topic,
                    "target_audience": None,
                    "tone": payload.tone,
                    "style": payload.style,
                    "language_code": payload.language_code,
                    "content": publication.content,
                    "content_short": publication.content[:280],
                    "hashtags": publication.hashtags,
                    "cta_text": publication.cta_text,
                    "channel": payload.channel,
                    "publication_type": "post",
                    "scheduled_for": publication.scheduled_for.isoformat(),
                    "current_status": publication.current_status,
                    "requires_approval": payload.require_approval,
                    "created_by": payload.creator,
                    "metadata": {
                        "image_mode": payload.image_mode,
                        "extra_instructions": payload.extra_instructions,
                    },
                }
            )

        publication_response = _post("linkedin_publications", publication_rows, prefer="return=representation")
        for created_pub in publication_response or []:
            status_rows.append(
                {
                    "publication_id": created_pub["id"],
                    "previous_status": None,
                    "new_status": created_pub["current_status"],
                    "changed_by": payload.creator,
                    "change_origin": "agent",
                    "detail": "Creación inicial de la publicación desde la campaña Growth LinkedIn.",
                }
            )
            asset_rows.append(
                {
                    "publication_id": created_pub["id"],
                    "asset_type": "image",
                    "asset_role": "primary",
                    "source_type": "generated" if payload.image_mode == "auto" else ("uploaded" if payload.image_mode == "manual" else "generated"),
                    "asset_status": "pending",
                    "metadata": {
                        "image_mode": payload.image_mode,
                    },
                }
            )

        if status_rows:
            _post("linkedin_publication_status_history", status_rows)
        if asset_rows:
            _post("linkedin_publication_assets", asset_rows)

        return PersistenceResult(
            persisted=True,
            prompt_run_id=prompt_run_id,
            note=f"Campaña persistida en Supabase ORQUESTA con {len(publication_rows)} publicaciones.",
        )
    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", "replace")
        return PersistenceResult(
            persisted=False,
            prompt_run_id=None,
            note=f"Error HTTP Supabase {exc.code}: {body[:400]}",
        )
    except Exception as exc:
        return PersistenceResult(
            persisted=False,
            prompt_run_id=None,
            note=f"Error de persistencia Supabase: {exc}",
        )
