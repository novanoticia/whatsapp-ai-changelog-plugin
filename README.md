# WhatsApp AI Changelog v1.5.1

Plugin basado en la skill `whatsapp-ai-changelog` v1.5 del archivo adjunto.
Convierte el README y las novedades verificables de un repositorio de IA en
un mensaje de WhatsApp para usuarios generales o profesionales sin perfil
de desarrollo.

Incluye **Bayesian Compose v1.3.0**, sus 30 criterios, configuración y
referencias. No requiere instalar esa dependencia por separado.

## Idioma

**Español (`es`)** es el idioma predeterminado del plugin y de la
documentación. La entrevista, el mensaje y el diagnóstico se presentan en
español. Puedes pedir otro idioma para la conversación o para el destinatario.

## Uso

```text
/whatsapp-ai-changelog https://github.com/usuario/repositorio
```

También puedes pedir: «Mensaje WhatsApp sobre esta herramienta de IA:
[enlace al repositorio]».

1. Consulta el README y comprueba siempre la última publicación estable
   de GitHub cuando vaya a describir las últimas novedades, incluso si
   el README ya menciona una versión.
2. Pregunta por el perfil del receptor y realiza las cinco preguntas
   adaptadas de la entrevista, una por una.
3. Genera un borrador de 200–350 palabras, con formato de WhatsApp.
4. Evalúa los 30 criterios y presenta score, fortalezas, debilidades y tabla.
5. Permite iterar y entregar el texto limpio para copiar y pegar.

El score estima la calidad del mensaje desde la perspectiva del receptor;
no es una probabilidad calibrada de respuesta. Las notas verificadas de
GitHub se usan aunque el README no tenga una sección de versiones. Solo si
ninguna de esas fuentes aporta cambios verificables se limita a
funcionalidades documentadas, indicando la limitación. Si no puede comprobar
la última publicación, no presenta una versión del README como la más reciente.
El plugin redacta mensajes; no los envía.

## Instalación en Claude Code

Cuando este repositorio esté publicado:

```text
/plugin marketplace add novanoticia/whatsapp-ai-changelog-plugin
/plugin install whatsapp-ai-changelog@whatsapp-ai-changelog-plugin
```

En clientes que usan nombres de comando con namespace, el comando puede ser
`/whatsapp-ai-changelog:whatsapp-ai-changelog [URL]`.

Para probar la carpeta local con Claude Code:

```sh
claude --plugin-dir /ruta/whatsapp-ai-changelog-plugin
```

## Otros clientes

La raíz contiene `plugin.json` para clientes que admitan Agent Plugins
1.0.0, y `skills/` contiene las dos skills en formato SKILL.md.
La disponibilidad de instalación desde GitHub depende del cliente.
El soporte específico de ChatGPT/Codex debe comprobarse en su instalador;
este paquete no crea ni registra por sí solo un plugin en su catálogo.

Si tu cliente importa skills individualmente, importa **ambas** carpetas:
`skills/whatsapp-ai-changelog/` y `skills/bayesian-compose/`.

## Requisitos

Un asistente compatible con skills y acceso de lectura a GitHub mediante
navegación o un conector autorizado. Si no puede leer el repositorio,
puedes pegar o adjuntar el README y las notas de versión. No requiere
servidor MCP, credenciales de WhatsApp ni código ejecutable.

## Estructura

```text
.claude-plugin/
  plugin.json
  marketplace.json
plugin.json
commands/whatsapp-ai-changelog.md
skills/
  whatsapp-ai-changelog/SKILL.md
  bayesian-compose/
    SKILL.md
    config.yaml
    references/
README.md
CHANGELOG.md
PRIVACY.md
THIRD_PARTY_NOTICES.md
LICENSE
```

## Procedencia y licencia

La skill principal procede de `whatsapp-ai-changelog.zip`, de Pablo.
Bayesian Compose procede de
[novanoticia/bayesian-compose-plugin](https://github.com/novanoticia/bayesian-compose-plugin)
y conserva sus escalas y protocolo. Consulta
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) para los archivos y hashes.
Licencia Apache-2.0; consulta [LICENSE](LICENSE).
