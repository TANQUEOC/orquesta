from fastapi import APIRouter

from app.core.config import settings
from app.schemas.campaign import CampaignLaunchRequest, CampaignLaunchResponse, CampaignPreviewResponse
from app.services.generator import build_campaign_preview
from app.services.linkedin_adapter import LinkedInAdapter
from app.services.persistence import persist_campaign

router = APIRouter()
linkedin_adapter = LinkedInAdapter()


@router.get('/')
def root() -> dict:
    return {
        'ok': True,
        'service': 'orquesta-linkedin-growth-campaign',
        'runtime_public_base_url': settings.runtime_public_base_url,
        'endpoints': ['/health', '/runtime/meta', '/campaigns/preview', '/campaigns/launch', '/linkedin/status'],
    }


@router.get('/health')
def health() -> dict:
    return {'ok': True, 'service': 'orquesta-linkedin-growth-campaign'}


@router.get('/runtime/meta')
def runtime_meta() -> dict:
    return {
        'ok': True,
        'service': settings.app_name,
        'environment': settings.app_env,
        'default_channel': settings.default_channel,
        'supabase_configured': bool(settings.supabase_service_role_key),
        'runtime_public_base_url': settings.runtime_public_base_url,
    }


@router.get('/linkedin/status')
def linkedin_status() -> dict:
    status = linkedin_adapter.get_status()
    return {
        'ok': True,
        'configured': status.configured,
        'mode': status.mode,
        'note': status.note,
    }


@router.post('/campaigns/preview', response_model=CampaignPreviewResponse)
def preview_campaign(payload: CampaignLaunchRequest) -> CampaignPreviewResponse:
    return build_campaign_preview(payload)


@router.post('/campaigns/launch', response_model=CampaignLaunchResponse)
async def launch_campaign(payload: CampaignLaunchRequest) -> CampaignLaunchResponse:
    preview = build_campaign_preview(payload)
    persistence = await persist_campaign(payload, preview)
    return CampaignLaunchResponse(
        ok=True,
        persisted=bool(persistence.get('persisted')),
        prompt_run_id=persistence.get('prompt_run_id'),
        publications_created=len(preview.publications),
        preview=preview,
        note=str(persistence.get('note')),
    )
