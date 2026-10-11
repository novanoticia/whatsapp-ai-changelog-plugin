<!-- i18n fuente-sha256=640fc9688630 estado=borrador-ia -->

# Fixed-text equivalences — English

This file only translates the fixed texts of `SKILL.md`. If anything differs,
`SKILL.md` governs: its Spanish version is the canonical reference. This file
adds no rules and changes no criteria, scales or scores. Status: machine
translation, `borrador-ia`, not human-reviewed.

## Glossary

| Spanish | English |
| --- | --- |
| mensaje | message |
| borrador | draft |
| novedades | what's new |
| publicación estable | stable release |
| notas de la publicación | release notes |
| destinatario / receptor | recipient |
| entrevista | interview |
| diagnóstico | diagnosis |
| fortalezas / debilidades | strengths / weaknesses |

English has no tú/usted distinction; address the person directly in the second
person.

## Not translated

`/whatsapp-ai-changelog`, `idioma=`, `[NOTA]`, `Score`, `REPLY_NEEDED`,
`REVIEW`, `READING_LATER`, `ARCHIVE`, the emoji, URLs, versions, tool names and
the quoted content of the README or release notes.

## Interview — PHASE 2

| Question | Español | English |
| --- | --- | --- |
| #0 | ¿A quién va dirigido el mensaje? Elige el perfil que mejor describe al receptor: | Who is the message for? Choose the profile that best describes the recipient: |
| #0 a | Usuario general de IA — usa herramientas como ChatGPT, Gemini o Perplexity, sin perfil técnico | General AI user — uses tools such as ChatGPT, Gemini or Perplexity, with no technical background |
| #0 b | Profesional que integra IA en su trabajo — médico, abogado, docente, gestor... sin ser dev | Professional who brings AI into their work — doctor, lawyer, teacher, manager... but not a developer |
| #0 c | Ambos perfiles a la vez — el mensaje debe funcionar para los dos | Both profiles at once — the message must work for both |
| #1 (gate) | ¿Qué quieres que el destinatario haga después de leer el mensaje? | What do you want the recipient to do after reading the message? |
| #2 | ¿Hay una decisión concreta que el destinatario deba tomar? (empezar a usar la herramienta, actualizarla, recomendarla, cambiar cómo la usa...) | Is there a specific decision the recipient has to make? (start using the tool, update it, recommend it, change how they use it...) |
| #3 | ¿Quieres incluir enlace al repositorio, a una demo, a instrucciones de uso, o solo el nombre de la herramienta? | Do you want to include a link to the repository, a demo or usage instructions, or just the name of the tool? |
| #4 | ¿Hay algo que el mensaje debería mencionar pero prefieres no destacar? (limitaciones conocidas, requisitos previos, estado beta, casos en que la herramienta no funciona bien) | Is there anything the message should mention but you would rather not highlight? (known limitations, prerequisites, beta status, cases where the tool does not work well) |
| #5 | ¿Qué pasa si el destinatario lee esto dentro de 3 días en vez de hoy? ¿Hay alguna razón real para que lo lea ahora? | What happens if the recipient reads this in 3 days instead of today? Is there a real reason for them to read it now? |

Gate follow-up when the answer to #1 is vague (for example, "so they know about
it"): ask whether the recipient should try the tool, recommend it to someone,
give feedback, change their workflow, or simply learn about the news.

## Output and iteration — PHASES 4 and 5

| Español | English |
| --- | --- |
| Tu mensaje (Score: XX · TIER) | Your message (Score: XX · TIER) |
| Nivel 1 — Mensaje + veredicto | Level 1 — Message + verdict |
| Nivel 2 — Fortalezas y debilidades | Level 2 — Strengths and weaknesses |
| Nivel 3 — Desglose completo | Level 3 — Full breakdown |
| REPLY_NEEDED 🔴: generaría respuesta activa | REPLY_NEEDED 🔴: would prompt an active reply |
| REVIEW 🟡: leído con atención | REVIEW 🟡: read attentively |
| READING_LATER 🔵: leído "cuando pueda" | READING_LATER 🔵: read "when they get to it" |
| ARCHIVE ⚪: ignorado o archivado | ARCHIVE ⚪: ignored or archived |
| Reescribir incorporando las debilidades | Rewrite incorporating the weaknesses |
| Modificar un punto específico | Change one specific point |
| Cambiar el perfil del destinatario | Change the recipient profile |
| Entregar el mensaje | Deliver the message |
| Score v1: XX → Score v2: YY | Score v1: XX → Score v2: YY |

## Limitations and warnings

| Español | English |
| --- | --- |
| El repositorio es privado o inaccesible: pega el contenido del README directamente. | The repository is private or inaccessible: please paste the README content directly. |
| No se ha comprobado cuál es la última publicación. | The latest release has not been checked. |
| El diagnóstico está pendiente. | The diagnosis is pending. |
| Ninguna fuente aporta cambios verificables; el mensaje se limita a funcionalidades documentadas. | No source provides verifiable changes; the message is limited to documented features. |
| Idioma no disponible. Idiomas disponibles: `es`, `en`, `fr` y `zh`. | Language not available. Available languages: `es`, `en`, `fr` and `zh`. |

Elaborado con asistencia de IA; requiere revisión humana. (AI-assisted;
requires human review.)
