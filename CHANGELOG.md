# Changelog

## [1.5.2] — 2026-10-09

- Añadidas distribuciones de una sola skill para Mistral Work y Perplexity, con el
  protocolo y los 30 criterios de Bayesian Compose como referencias internas.
- Eliminada en esa distribución la dependencia de otra skill y de rutas
  entre carpetas. Conservadas las escalas y las correcciones de publicaciones.
- Evitado el registro duplicado de `bayesian-compose` en Perplexity.
- Añadidos generador, instrucciones para cada cliente y ZIP separados:
  carpeta para Mistral y `SKILL.md` en la raíz del ZIP para Perplexity.
- Instalación: en Perplexity, subir `whatsapp-ai-changelog-perplexity-1.5.2.zip`
  directamente; en Mistral, descomprimir `whatsapp-ai-changelog-mistral-1.5.2.zip`
  y utilizar la carpeta resultante.

## [1.5.1] — 2026-10-09

- Comprobada la última publicación estable aunque el README mencione versiones.
- Conservadas las notas de publicación verificadas cuando el README no
  documenta versiones; la alternativa de funcionalidades exige que ninguna
  de las dos fuentes aporte cambios verificables.
- Declarado el español como idioma predeterminado del flujo y traducidas
  las descripciones de los manifiestos y del marketplace.
- Publicación de versiones y ZIP del plugin mediante GitHub Actions.

## [1.5.0] — 2026-10-09

- Empaquetada la skill WhatsApp AI Changelog v1.5 como plugin.
- Añadidos manifiestos para Claude y Agent Plugins 1.0.0, marketplace y comando.
- Incluida Bayesian Compose v1.3.0 con configuración y referencias originales.
- Aclarada la integración para evitar entrevistas duplicadas y preservar escalas.
- Documentadas instalación, privacidad y procedencia.
