# Contrato de datos · Captación → Onboarding v1

## Objetivo
Definir qué datos pasan de Captación a Onboarding y cuáles deben pedirse ya dentro del onboarding.

## Datos mínimos que deben pasar desde Captación
- nombre
- email
- teléfono
- empresa
- cargo o rol
- necesidad o proceso a mejorar
- canal de entrada
- notas comerciales relevantes
- responsable interno
- nivel de urgencia o prioridad
- fecha de cierre

## Datos que pueden pasar si existen
- origen de campaña
- etiquetas comerciales
- scoring o prioridad interna
- contexto resumido de conversaciones previas
- tipo de oferta contratada

## Datos que deben pedirse en Onboarding
- accesos necesarios
- documentación inicial
- datos fiscales si aplican
- materiales de trabajo
- personas de contacto del cliente
- disponibilidad para kickoff
- dependencias operativas necesarias para arrancar

## Regla de datos
- no duplicar recogida si el dato ya existe y es fiable
- no pasar ruido comercial innecesario al onboarding
- sí pasar todo lo que reduzca fricción de arranque

## Identificador recomendado
Debe existir un identificador común o enlazable entre:
- registro de captación
- registro de onboarding

Opciones mínimas viables:
- `lead_id` heredado como referencia
- `client_id` nuevo con referencia al `lead_id`
- email + fecha de cierre como fallback temporal

## Regla de calidad
Si un dato llega dudoso o incompleto, debe marcarse para validación humana en onboarding y no asumirse como correcto por defecto.
