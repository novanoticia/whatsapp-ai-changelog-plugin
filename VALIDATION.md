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
- La skill aportada se conserva íntegra, seguida de la sección de integración.
- La dependencia conserva los hashes Git registrados en THIRD_PARTY_NOTICES.md.
- Se verificaron 30 criterios, 12 core y umbrales 10 / 4 / 0.
- Manifiestos y marketplace tienen nombre y versión coherentes.
- Los enlaces locales del README existen.

Estas comprobaciones validan el empaquetado. No se ha ejecutado una sesión
de composición en Claude ni una instalación en ChatGPT/Codex, y el manifiesto
portable no se ha contrastado con un validador de Agent Plugins 1.0.0.
