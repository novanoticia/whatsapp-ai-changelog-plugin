<!-- i18n fuente-sha256=640fc9688630 estado=borrador-ia -->

# 固定文本对照表 — 中文（简体）

本文件仅翻译 `SKILL.md` 中的固定文本。如有出入，以 `SKILL.md` 为准，其西班牙语
版本是权威参考。本文件不增加任何规则，也不改变标准、量表或评分。状态：机器翻译，
`borrador-ia`，未经人工审核。本文件为简体中文；繁体中文（`zh-Hant`、`zh-TW`、
`zh-HK`）暂不提供。

## 术语表

| Español | 中文 |
| --- | --- |
| mensaje | 消息 |
| borrador | 草稿 |
| novedades | 新变化 / 更新内容 |
| publicación estable | 稳定版本（release） |
| notas de la publicación | 版本说明 |
| destinatario / receptor | 收件人 |
| entrevista | 访谈 |
| diagnóstico | 诊断 |
| fortalezas / debilidades | 优点 / 不足 |

称呼方式：使用“你”（对应西班牙语的 tú），不使用“您”。

## 不翻译的内容

`/whatsapp-ai-changelog`、`idioma=`、`[NOTA]`、`Score`、`REPLY_NEEDED`、`REVIEW`、
`READING_LATER`、`ARCHIVE`、表情符号、URL、版本号、工具名称，以及引用的 README
或版本说明内容。

## 访谈 — 第 2 阶段

| 问题 | Español | 中文 |
| --- | --- | --- |
| #0 | ¿A quién va dirigido el mensaje? Elige el perfil que mejor describe al receptor: | 这条消息是写给谁的？请选择最符合收件人的画像： |
| #0 a | Usuario general de IA — usa herramientas como ChatGPT, Gemini o Perplexity, sin perfil técnico | 普通 AI 用户——使用 ChatGPT、Gemini 或 Perplexity 等工具，没有技术背景 |
| #0 b | Profesional que integra IA en su trabajo — médico, abogado, docente, gestor... sin ser dev | 在工作中使用 AI 的专业人士——医生、律师、教师、管理者等，但不是开发者 |
| #0 c | Ambos perfiles a la vez — el mensaje debe funcionar para los dos | 两类画像兼顾——消息要对两者都适用 |
| #1 (gate) | ¿Qué quieres que el destinatario haga después de leer el mensaje? | 你希望收件人读完消息后做什么？ |
| #2 | ¿Hay una decisión concreta que el destinatario deba tomar? (empezar a usar la herramienta, actualizarla, recomendarla, cambiar cómo la usa...) | 收件人是否需要做出某个具体决定？（开始使用该工具、更新、推荐给他人、改变使用方式……） |
| #3 | ¿Quieres incluir enlace al repositorio, a una demo, a instrucciones de uso, o solo el nombre de la herramienta? | 你想附上仓库链接、演示链接、使用说明，还是只写工具名称？ |
| #4 | ¿Hay algo que el mensaje debería mencionar pero prefieres no destacar? (limitaciones conocidas, requisitos previos, estado beta, casos en que la herramienta no funciona bien) | 有没有消息应该提到、但你不想突出的内容？（已知限制、前提条件、测试版状态、工具效果不佳的情况） |
| #5 | ¿Qué pasa si el destinatario lee esto dentro de 3 días en vez de hoy? ¿Hay alguna razón real para que lo lea ahora? | 如果收件人三天后才读到，而不是今天，会怎样？有没有真正的理由让他现在就读？ |

当 #1 的回答含糊时（例如“让他知道一下”）：追问收件人是应该试用该工具、推荐给别人、
提供反馈、改变工作方式，还是只是了解这个新变化。

## 输出与迭代 — 第 4 和第 5 阶段

| Español | 中文 |
| --- | --- |
| Tu mensaje (Score: XX · TIER) | 你的消息（Score: XX · TIER） |
| Nivel 1 — Mensaje + veredicto | 第 1 层 — 消息 + 结论 |
| Nivel 2 — Fortalezas y debilidades | 第 2 层 — 优点与不足 |
| Nivel 3 — Desglose completo | 第 3 层 — 完整明细 |
| REPLY_NEEDED 🔴: generaría respuesta activa | REPLY_NEEDED 🔴：会引发主动回复 |
| REVIEW 🟡: leído con atención | REVIEW 🟡：会被认真阅读 |
| READING_LATER 🔵: leído "cuando pueda" | READING_LATER 🔵：会在“有空时”阅读 |
| ARCHIVE ⚪: ignorado o archivado | ARCHIVE ⚪：会被忽略或归档 |
| Reescribir incorporando las debilidades | 针对不足重写 |
| Modificar un punto específico | 修改某一个具体点 |
| Cambiar el perfil del destinatario | 更换收件人画像 |
| Entregar el mensaje | 交付消息 |
| Score v1: XX → Score v2: YY | Score v1：XX → Score v2：YY |

## 限制与提示

| Español | 中文 |
| --- | --- |
| El repositorio es privado o inaccesible: pega el contenido del README directamente. | 该仓库是私有的或无法访问：请直接粘贴 README 的内容。 |
| No se ha comprobado cuál es la última publicación. | 尚未核实最新发布的版本。 |
| El diagnóstico está pendiente. | 诊断尚未完成。 |
| Ninguna fuente aporta cambios verificables; el mensaje se limita a funcionalidades documentadas. | 没有任何来源提供可核实的变更；消息仅限于已有文档记录的功能。 |
| Idioma no disponible. Idiomas disponibles: `es`, `en`, `fr` y `zh`. | 该语言不可用。可用语言：`es`、`en`、`fr` 和 `zh`。 |

Elaborado con asistencia de IA; requiere revisión humana.（由 AI 辅助编写；需要人工审核。）
