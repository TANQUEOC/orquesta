from __future__ import annotations

from dataclasses import dataclass


@dataclass
class LinkedInConnectionStatus:
    configured: bool
    mode: str
    note: str


@dataclass
class LinkedInPublishResult:
    ok: bool
    remote_post_id: str | None
    status: str
    note: str


class LinkedInAdapter:
    """
    Adaptador de integración futura con LinkedIn.

    Esta versión deja clara la frontera técnica sin fingir que ya existe
    una conexión real de publicación. La pieza queda preparada para:
    - OAuth / credenciales de LinkedIn
    - publicación de posts
    - programación si el proveedor final lo soporta
    - registro de respuesta remota
    """

    def get_status(self) -> LinkedInConnectionStatus:
        return LinkedInConnectionStatus(
            configured=False,
            mode="stub",
            note="La conexión real con LinkedIn aún requiere credenciales, permisos y validación del flujo de publicación.",
        )

    def publish_post(self, publication_payload: dict) -> LinkedInPublishResult:
        return LinkedInPublishResult(
            ok=False,
            remote_post_id=None,
            status="not_configured",
            note="Adaptador LinkedIn aún no conectado a credenciales reales.",
        )
