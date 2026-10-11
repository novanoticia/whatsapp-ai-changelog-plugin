# Changelog

<!-- i18n:inicio -->
## [Sin publicar]

- Añadida la interfaz en inglés, seleccionable con `idioma=en` en la primera
  línea del mensaje (`es` y `en`), con equivalencias de textos fijos en
  `skills/whatsapp-ai-changelog/references/i18n/en.md`. Sin marcador, el
  comportamiento no cambia.
- Añadida documentación en inglés: `README.en.md`, `CHANGELOG.en.md` y
  `PRIVACY.en.md`. Las traducciones son borradores de IA sin revisión humana.
- Excepciones aprobadas: la `description` de la skill principal y la de los
  paquetes de una sola skill mencionan también la frase de activación en inglés
  (cambia cuándo se activa la skill; se retira revirtiendo ese cambio), y toda
  respuesta en inglés empieza con un aviso de traducción automática (nunca en
  español ni dentro del mensaje final).
- Los paquetes de Mistral y Perplexity incluyen `references/i18n/en.md`.
- Pendiente: evaluación por escenarios del bloque de idioma, revisión humana de
  las traducciones y decidir la versión (cambiar `plugin.json` dispara la
  publicación).

Elaborado con asistencia de IA; requiere revisión humana.
<!-- i18n:fin -->

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
