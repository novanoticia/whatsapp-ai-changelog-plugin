<!-- i18n fuente-sha256=312ef33d0ebe estado=borrador-ia -->

# 更新日志

> [CHANGELOG.md](CHANGELOG.md) 的简体中文翻译（`borrador-ia`：机器翻译，未经人工
> 审核）。如有出入，以西班牙语文件为准。在 GitHub 上发布的版本说明来自西班牙语文件。

## [未发布]

- 新增法语（`fr`）和简体中文（`zh`）作为界面语言，使用 `idioma=fr` 和 `idioma=zh`，
  固定文本对照表位于 `skills/whatsapp-ai-changelog/references/i18n/fr.md` 和
  `zh.md`。繁体中文（`zh-Hant`、`zh-TW`、`zh-HK`）不可用，也不会用简体中文代替。
  不写标记时，行为不变。
- 新增法语和中文文档：`README`、`CHANGELOG` 和 `PRIVACY`（`.fr.md` 和 `.zh.md`）。
  它们是 AI 草稿，未经人工审核。
- 修改翻译提示：每种语言都用该语言显示提示；启用安全回退（缺少对照表文件）时，回复
  改为西班牙语，并附上所请求语言的提示行（此前会继续使用所请求的语言；修复情景评估
  中的发现 S6）。
- Mistral 和 Perplexity 的软件包包含 `fr.md` 和 `zh.md`。
- 不修改 `description`：在法语和中文中，自然语言触发取决于平台；命令
  `/whatsapp-ai-changelog` 始终可用。
- 待办：对翻译进行人工审核（中文的不确定性更大），并重新进行情景评估。

由 AI 辅助编写；需要人工审核。

## [1.6.0] — 2026-10-11

新增：

- 可在消息第一行使用 `idioma=en` 选择英语界面（可用 `es` 和 `en`），固定文本对照表
  位于 `skills/whatsapp-ai-changelog/references/i18n/en.md`。不写标记时，行为不变。
- 英语文档：`README.en.md`、`CHANGELOG.en.md` 和 `PRIVACY.en.md`。
- 在 `tests/test_i18n.py` 中新增测试；Mistral 和 Perplexity 的软件包现在包含
  `references/i18n/en.md`。
- 新增 `Pruebas` 工作流，在每个拉取请求上运行 `tests/`。

变更（对默认输出的已批准例外；撤销此变更即可取消）：

- 主技能的 `description` 以及单技能软件包的描述现在也提到英语触发短语，使技能能够在
  英语请求下被激活。这会改变技能被激活的时机。
- 每条英语回复都以提示“Translation machine-generated, not human-reviewed.”开头。该提示
  绝不会出现在西班牙语回复中，也不会出现在要复制的最终消息里。

限制：

- 英语文件是机器翻译（`borrador-ia`），未经人工审核。
- 清单文件、`VALIDATION.md`、`MISTRAL.md`、`PERPLEXITY.md` 和
  `THIRD_PARTY_NOTICES.md` 仍只提供西班牙语。清单的模式中没有经过验证的多语言描述
  字段。
- 新语言块的情景评估尚未运行（待办）。

## [1.5.2] — 2026-10-09

- 为 Mistral Work 和 Perplexity 新增单技能发行版，把 Bayesian Compose 协议及其 30 条
  标准作为内部参考资料。
- 在该发行版中移除了对另一个技能以及跨文件夹路径的依赖。保留了量表和发布版本的修正。
- 避免了 `bayesian-compose` 在 Perplexity 中被重复注册。
- 新增生成器、各客户端的说明以及独立的 ZIP：Mistral 使用文件夹，Perplexity 的 ZIP 根目录
  放置 `SKILL.md`。
- 安装：在 Perplexity 中直接上传 `whatsapp-ai-changelog-perplexity-1.5.2.zip`；在
  Mistral 中解压 `whatsapp-ai-changelog-mistral-1.5.2.zip` 并使用得到的文件夹。

## [1.5.1] — 2026-10-09

- 即使 README 提到了版本，也会检查最新的稳定发布版本。
- 当 README 没有记录版本时，保留已核实的版本说明；只有当两个来源都无法提供可核实的
  变更时，才退回到仅介绍功能。
- 声明西班牙语为流程的默认语言，并翻译了清单文件和 marketplace 的描述。
- 通过 GitHub Actions 发布版本和插件 ZIP。

## [1.5.0] — 2026-10-09

- 把 WhatsApp AI Changelog v1.5 技能打包为插件。
- 新增适用于 Claude 和 Agent Plugins 1.0.0 的清单文件、marketplace 和命令。
- 包含 Bayesian Compose v1.3.0 及其原始配置和参考资料。
- 澄清集成方式，避免重复访谈并保留量表。
- 记录了安装、隐私和来源。

由 AI 辅助编写；需要人工审核。
