<!-- i18n fuente-sha256=f14a6950c1cf estado=borrador-ia -->

# Privacy

> English translation of [PRIVACY.md](PRIVACY.md) (`borrador-ia`: machine
> translation, not human-reviewed). If they differ, the Spanish file governs.

WhatsApp AI Changelog drafts text inside the assistant's conversation. The package
contains no server, scripts, sending tools or storage services of its own.

To extract information, the assistant queries GitHub through the browsing or
connector the user has available. How that data is handled depends on the
assistant, the connector and GitHub.

Bayesian Compose supports personal configuration outside the package and optional
local telemetry. No sessions or patterns are recorded without the user's express
request, even if a configuration folder exists. Telemetry allows only metadata:
never the text of the message or identifying data. See STEP 7 of its SKILL.md.

The final message is copied into WhatsApp manually. The plugin does not send
messages or connect to the WhatsApp account.

AI-assisted; requires human review.
