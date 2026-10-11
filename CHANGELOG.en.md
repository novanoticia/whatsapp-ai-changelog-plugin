<!-- i18n fuente-sha256=a1a8e2d6f5eb estado=borrador-ia -->

# Changelog

> English translation of [CHANGELOG.md](CHANGELOG.md) (`borrador-ia`: machine
> translation, not human-reviewed). If they differ, the Spanish file governs.
> Release notes published on GitHub come from the Spanish file.

## [Unreleased]

Added:

- English interface selectable with `idioma=en` on the first line of the message
  (`es` and `en` available), with fixed-text equivalences in
  `skills/whatsapp-ai-changelog/references/i18n/en.md`. Without the marker the
  behavior does not change.
- English documentation: `README.en.md`, `CHANGELOG.en.md` and `PRIVACY.en.md`.
- Tests in `tests/test_i18n.py`, and the Mistral and Perplexity packages now
  include `references/i18n/en.md`.
- Added the `Pruebas` workflow, which runs `tests/` on every pull request.

Changed (approved exceptions to the default output, to withdraw by reverting
this change):

- The `description` of the main skill and the description of the single-skill
  packages now also mention the English trigger phrase, so the skill can
  activate on English requests. This changes when the skill activates.
- Every English response opens with the notice "Translation machine-generated,
  not human-reviewed.". It never appears in Spanish nor inside the final message
  to copy.

Limitations:

- The English files are machine translations (`borrador-ia`), with no human
  review.
- The manifests, `VALIDATION.md`, `MISTRAL.md`, `PERPLEXITY.md` and
  `THIRD_PARTY_NOTICES.md` remain in Spanish only. The manifest schema has no
  verified multilingual description field.
- The scenario evaluation of the new language block has not been run (pending).
- The version has not been bumped; bumping `plugin.json` triggers the release
  workflow.

## [1.5.2] — 2026-10-09

- Added single-skill distributions for Mistral Work and Perplexity, with the
  Bayesian Compose protocol and its 30 criteria as internal references.
- Removed, in that distribution, the dependency on another skill and on paths
  between folders. Kept the scales and the release corrections.
- Avoided the duplicate registration of `bayesian-compose` in Perplexity.
- Added a generator, per-client instructions and separate ZIPs: a folder for
  Mistral and `SKILL.md` at the root of the ZIP for Perplexity.
- Installation: in Perplexity, upload `whatsapp-ai-changelog-perplexity-1.5.2.zip`
  directly; in Mistral, unzip `whatsapp-ai-changelog-mistral-1.5.2.zip` and use
  the resulting folder.

## [1.5.1] — 2026-10-09

- Checked the latest stable release even when the README mentions versions.
- Kept the verified release notes when the README documents no versions; the
  features-only fallback requires that neither source provides verifiable changes.
- Declared Spanish as the default language of the flow and translated the
  descriptions of the manifests and the marketplace.
- Publication of versions and plugin ZIPs through GitHub Actions.

## [1.5.0] — 2026-10-09

- Packaged the WhatsApp AI Changelog v1.5 skill as a plugin.
- Added manifests for Claude and Agent Plugins 1.0.0, a marketplace and a command.
- Included Bayesian Compose v1.3.0 with its original configuration and references.
- Clarified the integration to avoid duplicate interviews and preserve scales.
- Documented installation, privacy and provenance.

AI-assisted; requires human review.
