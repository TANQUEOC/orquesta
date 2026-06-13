# 03 · Contrato mínimo de datos del objeto publicación

## Objeto lógico: `publicacion_linkedin`

```json
{
  "id_publicacion": "pub_000001",
  "tema": "IA aplicada a pymes",
  "audiencia": "dueños de pymes y directivos",
  "idioma": "es",
  "tono": "profesional cercano",
  "estilo": "claro y útil",
  "contenido": "Texto final de la publicación",
  "hashtags": ["#IA", "#Pymes"],
  "cta": "Si quieres, te comparto más ejemplos.",
  "fecha_creacion": "2026-06-12T18:40:00Z",
  "fecha_programada": "2026-06-16T09:00:00Z",
  "fecha_publicacion": null,
  "estado": "Pendiente de aprobación",
  "canal": "LinkedIn",
  "prompt_origen": "Quiero 8 publicaciones...",
  "imagen": {
    "tipo": "placeholder",
    "url": null,
    "referencia": null,
    "estado": "Pendiente"
  },
  "requiere_aprobacion": true,
  "usuario_creador": "luis",
  "observaciones_error": null,
  "metadata": {
    "periodicidad": "2 por semana",
    "numero_lote": 8,
    "version_prompt": "v1"
  }
}
```

## Campos mínimos obligatorios
- `id_publicacion`
- `tema`
- `audiencia`
- `idioma`
- `tono`
- `estilo`
- `contenido`
- `fecha_creacion`
- `fecha_programada`
- `estado`
- `canal`
- `prompt_origen`
- `usuario_creador`

## Reglas mínimas
- no pasa a `Programada` si `contenido` está vacío
- no pasa a `Programada` si `fecha_programada` es nula
- no pasa a `Publicada` sin marca temporal real de publicación
- `observaciones_error` debe poblarse cuando el estado entra en error
- `requiere_aprobacion=true` debe bloquear el salto directo de `Borrador` a `Programada`

## Estados válidos v1
- `Borrador`
- `Pendiente de aprobación`
- `Aprobada`
- `Programada`
- `Publicada`
- `Error de publicación`
- `Cancelada`
