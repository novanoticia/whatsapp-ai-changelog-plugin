<!-- i18n fuente-sha256=5f4cac09c9d4 estado=borrador-ia -->

# WhatsApp AI Changelog v1.7.0

> English translation of [README.md](README.md) (`borrador-ia`: machine
> translation, not human-reviewed). If they differ, the Spanish
> [README.md](README.md) governs.

Plugin based on version 1.5 of the `whatsapp-ai-changelog` skill from the attached
archive. It turns the README and the verifiable news of an AI repository into a
WhatsApp message for general users or for professionals without a developer
profile.

It includes **Bayesian Compose v1.3.0**, with its 30 criteria, configuration and
references. You do not need to install that dependency separately.

## Language

**Spanish (`es`)** is the default language of the plugin and of the documentation.
The interview, the message and the diagnosis are presented in Spanish. You can ask
for another language for the conversation or for the recipient.

To run the interview and the diagnosis in another language, write `idioma=en`,
`idioma=fr` or `idioma=zh` (Simplified Chinese) as a separate word on the first line
of your message, for example
`/whatsapp-ai-changelog idioma=fr https://github.com/user/repository`. Without the
marker nothing changes. Available languages: `es` (reference), `en`, `fr` and `zh`
(machine-translated drafts, not human-reviewed; Traditional Chinese is not
available). Every response in those languages opens with a translation notice in
that language; the final message you copy into WhatsApp never carries it.
Translated documentation: [README.en.md](README.en.md),
[README.fr.md](README.fr.md) and [README.zh.md](README.zh.md), each with its
`CHANGELOG.<code>.md` and `PRIVACY.<code>.md`.

The message itself is written in the language you choose for the recipient; if you
do not choose one, in the language of the conversation. The interface text,
`[NOTA]` markers, tier codes, commands, URLs and the quoted README content are not
translated. The manifests (`plugin.json`, marketplace), `VALIDATION.md`,
`MISTRAL.md`, `PERPLEXITY.md` and `THIRD_PARTY_NOTICES.md` stay in Spanish.

To add a language, create `skills/whatsapp-ai-changelog/references/i18n/<code>.md`
following the structure of `en.md`, add the code to the language block of
`skills/whatsapp-ai-changelog/SKILL.md`, list the file in
`scripts/package_skills.py` and the new language in `tests/test_i18n.py`, and add
its documentation files.

## Usage

```text
/whatsapp-ai-changelog https://github.com/usuario/repositorio
```

You can also ask: "WhatsApp message about this AI tool: [link to the repository]".

1. It reads the README and always checks the latest stable GitHub release when it
   is going to describe the latest news, even if the README already mentions a
   version.
2. It asks about the recipient's profile and then runs the five adapted interview
   questions, one by one.
3. It generates a 200–350 word draft in WhatsApp format.
4. It evaluates the 30 criteria and presents a score, strengths, weaknesses and a
   table.
5. It lets you iterate and hands you the clean text to copy and paste.

The score estimates the quality of the message from the recipient's point of view;
it is not a calibrated probability of a reply. Verified GitHub release notes are
used even if the README has no versions section. Only if neither source provides
verifiable changes does it limit itself to documented features, stating the
limitation. If it cannot check the latest release, it does not present a README
version as the most recent one. The plugin drafts messages; it does not send them.

## Installation in Claude Code

Once this repository is published:

```text
/plugin marketplace add novanoticia/whatsapp-ai-changelog-plugin
/plugin install whatsapp-ai-changelog@whatsapp-ai-changelog-plugin
```

In clients that use namespaced command names, the command may be
`/whatsapp-ai-changelog:whatsapp-ai-changelog [URL]`.

To try the local folder with Claude Code:

```sh
claude --plugin-dir /path/whatsapp-ai-changelog-plugin
```

## Installation in Mistral Work

Use the asset **whatsapp-ai-changelog-mistral-1.7.0.zip** from
[GitHub Releases](https://github.com/novanoticia/whatsapp-ai-changelog-plugin/releases/latest).
Unzip it and create a skill with the `whatsapp-ai-changelog/` folder. The
evaluation protocol is included as internal references; a single skill is enough.
The Claude plugin ZIP has a different format. See [MISTRAL.md](MISTRAL.md) (in
Spanish) for importing the folder or using the editor.

## Installation in Perplexity Computer

Use **whatsapp-ai-changelog-perplexity-1.7.0.zip** from
[GitHub Releases](https://github.com/novanoticia/whatsapp-ai-changelog-plugin/releases/latest)
and upload it directly from **Skills → Create skill → Upload a skill**. Register
only `whatsapp-ai-changelog`: the Bayesian Compose method is included in the
references and avoids a second skill with that name. See
[PERPLEXITY.md](PERPLEXITY.md) (in Spanish) for details.

## Other clients

The root contains `plugin.json` for clients that support Agent Plugins 1.0.0, and
`skills/` contains the two skills in SKILL.md format. Whether you can install from
GitHub depends on the client. ChatGPT/Codex support must be checked in its own
installer; this package does not by itself create or register a plugin in its
catalog.

For other clients that import the plugin's skills one by one, import **both**
folders: `skills/whatsapp-ai-changelog/` and `skills/bayesian-compose/`.

## Requirements

An assistant compatible with skills and read access to GitHub through browsing or
an authorized connector. If it cannot read the repository, you can paste or attach
the README and the release notes. It requires no MCP server, no WhatsApp
credentials and no executable code.

## Structure

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

## Provenance and license

The main skill comes from `whatsapp-ai-changelog.zip`, by Pablo. Bayesian Compose
comes from
[novanoticia/bayesian-compose-plugin](https://github.com/novanoticia/bayesian-compose-plugin)
and keeps its scales and protocol. See
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) for the files and hashes.
Apache-2.0 license; see [LICENSE](LICENSE).

AI-assisted; requires human review.
