# 06 · Decisiones del modelo de datos

## Qué hemos decidido

### 1. El prompt vive como entidad propia
No se incrusta solo dentro de cada publicación.

**Por qué:**
- una sola instrucción puede generar muchas publicaciones
- permite trazabilidad del lote
- facilita medir reutilización del prompt

### 2. La publicación es la entidad central
Cada publicación tiene su propio estado, copy, fechas, aprobación y errores.

**Por qué:**
- el sistema debe gobernar piezas individuales
- no todo el lote avanza igual

### 3. El historial de estados va separado
No se guarda solo el estado actual.

**Por qué:**
- necesitamos auditoría
- necesitamos saber qué cambió, cuándo y por qué

### 4. Los assets van desacoplados
La imagen no se mete solo como un campo plano.

**Por qué:**
- deja espacio para variantes
- soporta error visual sin romper la publicación
- permite futuro multiformato

### 5. Delivery se separa de la publicación
Los eventos contra LinkedIn no se guardan mezclados con el registro principal.

**Por qué:**
- puede haber varios intentos
- puede haber errores y reintentos
- la publicación no debe contaminarse con demasiado ruido técnico

### 6. Approval gate nativo desde la v1
La aprobación humana no se deja para después.

**Por qué:**
- reduce riesgo de publicación incorrecta
- encaja mejor con ORQUESTA como sistema gobernable

## Resultado
Con estas decisiones, la pieza ya puede crecer desde MVP a sistema serio sin rehacer todo el modelo desde cero.
