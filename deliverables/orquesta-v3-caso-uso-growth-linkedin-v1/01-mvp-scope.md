# 01 · MVP scope

## Objetivo de esta v1
Construir una primera versión gobernable del agente LinkedIn que permita pasar de una instrucción editorial por prompt a un lote de publicaciones estructuradas, almacenadas y listas para aprobación/programación.

## Qué incluye la v1
- entrada por prompt libre
- extracción estructurada de parámetros
- generación de lote de publicaciones
- planificación básica de calendario
- soporte de imagen por referencia o placeholder
- persistencia en base de datos
- estados mínimos del ciclo de vida
- aprobación humana opcional/por defecto activada
- preparación para programación en LinkedIn
- logging y trazabilidad mínimos

## Qué no incluye todavía
- optimización automática de mejores horarios
- aprendizaje automático fino del estilo de marca
- publicación multicanal
- analítica avanzada de rendimiento
- A/B testing de copies
- autonomía ciega sin approval gate

## Decisión de producto para la v1
La v1 debe construirse primero como **MVP editorial gobernable**, no como publicación totalmente automática desde el minuto uno.

## Resultado esperado de la v1
Al terminar esta fase, ORQUESTA debe poder:
1. recibir un prompt editorial
2. convertirlo en una estructura normalizada
3. generar publicaciones consistentes
4. asignarles fechas
5. guardarlas con estado
6. dejarlas listas para revisión, aprobación y posterior programación

## Modo operativo recomendado
- modo por defecto: `Pendiente de aprobación`
- publicación automática: solo como fase posterior o modo controlado

## Estados mínimos de la v1
- `Borrador`
- `Pendiente de aprobación`
- `Aprobada`
- `Programada`
- `Publicada`
- `Error de publicación`
- `Cancelada`

## Reglas de aceptación de la v1
La v1 se considera construida cuando:
- genera publicaciones desde un prompt real
- guarda cada publicación en base de datos
- calcula fechas válidas
- deja cada pieza con estado y trazabilidad
- permite revisión humana
- deja preparada la integración con LinkedIn sin acoplar todo el sistema a ella
