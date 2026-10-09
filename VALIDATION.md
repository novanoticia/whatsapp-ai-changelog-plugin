# Validación del paquete

Comprobaciones realizadas el 9 de octubre de 2026:

- Marketplace: `claude plugin validate .` — Validation passed.
- Manifiesto: `claude plugin validate .claude-plugin/plugin.json` — Validation passed.
- Validador utilizado: Claude Code 2.1.295, instalado en una caché temporal
  mediante npm; no es una dependencia del plugin.
- Los tres JSON y la configuración YAML se analizan sin errores.
- Ambos SKILL.md tienen frontmatter válido y nombres coherentes con sus carpetas.
- Descripciones: WhatsApp AI Changelog, 451 caracteres / 456 bytes;
  Bayesian Compose, 459 caracteres / 471 bytes.
- La skill aportada se adapta para comprobar publicaciones y conservar sus
  notas verificadas; incluye la sección de integración y el idioma español.
- La dependencia conserva los hashes Git registrados en THIRD_PARTY_NOTICES.md.
- Se verificaron 30 criterios, 12 core y umbrales 10 / 4 / 0.
- Manifiestos y marketplace tienen nombre y versión coherentes.
- Los enlaces locales del README existen.

## Revisión de las correcciones de `58779ad`

Se revisaron las instrucciones con estos escenarios; son comprobaciones
del flujo descrito, no una ejecución de composición con un asistente:

| Fuentes disponibles | Comportamiento previsto |
|---|---|
| README con insignia v1; publicación estable v2 con notas | Comprobar GitHub y usar v2; excluir cambios de v1 de las últimas novedades. |
| README sin versiones; publicación con cambios verificables | Redactar con las notas y versión de esa publicación. |
| Ninguna fuente aporta cambios verificables | Describir funcionalidades y explicar la limitación, sin inventar novedades. |
| Falla la consulta de publicaciones; README con cambios de v1 | Conservar los cambios documentados y advertir que no se ha comprobado si v1 es la última publicación. |

El español se declara en `metadata.language: es` de la skill principal,
en sus reglas de idioma y en el README. Los manifiestos y el marketplace
tienen descripciones en español. Se repitieron sus validaciones nativas,
el análisis JSON/YAML y la comprobación de hashes de la dependencia.

Estas comprobaciones validan el empaquetado. No se ha ejecutado una sesión
de composición en Claude ni una instalación en ChatGPT/Codex, y el manifiesto
portable no se ha contrastado con un validador de Agent Plugins 1.0.0.
