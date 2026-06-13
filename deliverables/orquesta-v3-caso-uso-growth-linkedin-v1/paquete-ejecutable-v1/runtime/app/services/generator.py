from __future__ import annotations

from datetime import datetime, timedelta
from zoneinfo import ZoneInfo

from app.core.config import settings
from app.schemas.campaign import CampaignLaunchRequest, CampaignPreviewResponse, PublicationPreview


def _periodicity_delta(periodicity: str) -> int:
    mapping = {
        "daily": 1,
        "2_per_week": 3,
        "3_per_week": 2,
        "1_per_week": 7,
        "custom": 3,
    }
    return mapping.get(periodicity, 3)


def _extract_topic(prompt: str) -> str:
    text = prompt.strip()
    if "Tema:" in text:
        return text.split("Tema:", 1)[1].split(".", 1)[0].strip()
    return "Campaña editorial de Growth"


def _cta(channel: str) -> str:
    if channel == "linkedin":
        return "Si quieres, te enseño cómo aterrizarlo en tu negocio con ORQUESTA."
    return "Si quieres, te comparto el siguiente paso."


def build_campaign_preview(payload: CampaignLaunchRequest) -> CampaignPreviewResponse:
    tz = ZoneInfo(settings.default_timezone)
    delta_days = _periodicity_delta(payload.periodicity)
    topic = _extract_topic(payload.prompt)
    summary = (
        f"Campaña {payload.channel} de {payload.publication_count} publicaciones sobre '{topic}', "
        f"con periodicidad {payload.periodicity} y modo de imagen {payload.image_mode}."
    )

    start_dt = datetime.combine(payload.start_date, payload.preferred_time, tzinfo=tz)
    publications: list[PublicationPreview] = []
    for i in range(payload.publication_count):
        scheduled_for = start_dt + timedelta(days=i * delta_days)
        internal_title = f"{topic} · Pieza {i + 1:02d}"
        content = (
            f"Publicación {i + 1}. {topic}. "
            f"Idea principal: explicar un ángulo claro y útil para dueños de pymes, "
            f"manteniendo tono {payload.tone} y estilo {payload.style}."
        )
        publications.append(
            PublicationPreview(
                publication_number=i + 1,
                internal_title=internal_title,
                topic=topic,
                content=content,
                cta_text=_cta(payload.channel),
                hashtags=["#ORQUESTA", "#IA", "#Growth", "#Pymes"],
                scheduled_for=scheduled_for,
                current_status="pending_approval" if payload.require_approval else "draft",
                image_mode=payload.image_mode,
            )
        )

    return CampaignPreviewResponse(
        summary=summary,
        prompt_normalized={
            "topic": topic,
            "channel": payload.channel,
            "periodicity": payload.periodicity,
            "publication_count": payload.publication_count,
            "tone": payload.tone,
            "style": payload.style,
            "language_code": payload.language_code,
            "require_approval": payload.require_approval,
        },
        publications=publications,
    )
