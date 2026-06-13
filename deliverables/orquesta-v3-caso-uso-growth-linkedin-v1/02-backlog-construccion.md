# 02 · Backlog de construcción

## Fase 0 · Cierre funcional
- [ ] Validar y congelar el alcance de la v1
- [ ] Confirmar estados del ciclo de vida
- [ ] Confirmar si la aprobación humana será obligatoria en la v1
- [ ] Confirmar canal inicial: LinkedIn personal, página o ambos

## Fase 1 · Modelo de datos
- [ ] Crear esquema mínimo de `publicaciones_linkedin`
- [ ] Crear tabla de historial de estados
- [ ] Definir campos obligatorios y opcionales
- [ ] Definir estrategia de almacenamiento de imágenes

## Fase 2 · Prompt parser
- [ ] Diseñar el JSON objetivo de extracción
- [ ] Implementar extractor de parámetros desde prompt
- [ ] Añadir validaciones de campos mínimos
- [ ] Añadir manejo de prompts incompletos

## Fase 3 · Generación de calendario
- [ ] Implementar generador de calendario según periodicidad
- [ ] Definir reglas base de horarios de publicación
- [ ] Evitar solapamientos o fechas inválidas
- [ ] Permitir reprogramación posterior

## Fase 4 · Generación de copy
- [ ] Diseñar plantilla maestra de prompt para LinkedIn
- [ ] Generar copies por lote
- [ ] Añadir CTA, hashtags y restricciones de marca
- [ ] Añadir variante o regeneración en caso de baja calidad

## Fase 5 · Imagen
- [ ] Definir estrategia MVP: placeholder, asset existente o generación simple
- [ ] Asociar imagen a cada publicación
- [ ] Gestionar estado `Pendiente de imagen` si falla

## Fase 6 · Persistencia
- [ ] Guardar cada publicación con metadatos
- [ ] Guardar prompt de origen
- [ ] Guardar transiciones de estado
- [ ] Guardar errores y observaciones

## Fase 7 · Revisión / approval gate
- [ ] Definir vista o mecanismo de revisión
- [ ] Permitir aprobar, rechazar, editar o cancelar
- [ ] Registrar aprobador y fecha

## Fase 8 · Integración LinkedIn
- [ ] Verificar capacidades reales de API/permisos
- [ ] Diseñar adaptador de publicación/programación
- [ ] Gestionar errores de autenticación y rate limit
- [ ] Registrar ID remoto y respuesta técnica

## Fase 9 · Monitorización
- [ ] Revisar estados programados
- [ ] Confirmar publicación efectiva
- [ ] Reintentar o escalar errores
- [ ] Añadir logs mínimos y alertas

## Fase 10 · Demo operativa
- [ ] Ejecutar un prompt real
- [ ] Generar un lote real de publicaciones
- [ ] Revisar aprobaciones
- [ ] Dejar al menos una publicación lista para programación

## Orden de construcción recomendado
1. modelo de datos
2. parser del prompt
3. generador de calendario
4. generador de copy
5. persistencia
6. approval gate
7. integración LinkedIn
8. monitorización

## Siguiente acción inmediata
**Construir primero el modelo de datos y el contrato mínimo del objeto publicación.**

Sin eso, el resto nace difuso.
