from datetime import date, time, datetime
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field


ImageMode = Literal["auto", "manual", "mixed"]
ChannelType = Literal["linkedin", "instagram", "x", "facebook", "youtube"]


class CampaignLaunchRequest(BaseModel):
    prompt: str = Field(min_length=20)
    periodicity: str = Field(default="2_per_week")
    publication_count: int = Field(default=8, ge=1, le=60)
    channel: ChannelType = "linkedin"
    language_code: str = "es"
    tone: str = "profesional cercano"
    style: str = "claro y útil"
    start_date: date
    preferred_time: time
    image_mode: ImageMode = "auto"
    require_approval: bool = True
    extra_instructions: str | None = None
    creator: str = "luis"


class PublicationPreview(BaseModel):
    publication_number: int
    internal_title: str
    topic: str
    content: str
    cta_text: str
    hashtags: list[str]
    scheduled_for: datetime
    current_status: str
    image_mode: ImageMode


class CampaignPreviewResponse(BaseModel):
    summary: str
    prompt_normalized: dict
    publications: list[PublicationPreview]


class CampaignLaunchResponse(BaseModel):
    ok: bool
    persisted: bool
    prompt_run_id: UUID | None = None
    publications_created: int
    preview: CampaignPreviewResponse
    note: str
