<!-- i18n fuente-sha256=5f4cac09c9d4 estado=borrador-ia -->

# WhatsApp AI Changelog v1.7.0

> [README.md](README.md) 的简体中文翻译（`borrador-ia`：机器翻译，未经人工审核）。
> 如有出入，以西班牙语的 [README.md](README.md) 为准。

本插件基于所附压缩包中的 `whatsapp-ai-changelog` 技能 1.5 版。它把某个 AI 仓库的
README 和可核实的更新内容，转换成一条 WhatsApp 消息，面向普通用户或没有开发背景的
专业人士。

它内置 **Bayesian Compose v1.3.0**，包含其 30 条标准、配置和参考资料。无需单独安装
该依赖。

## 语言

**西班牙语（`es`）** 是插件和文档的默认语言。访谈、消息和诊断都以西班牙语呈现。你可以
要求用其他语言进行对话，或用其他语言撰写给收件人的消息。

若要用其他语言进行访谈和诊断，请在消息第一行把 `idioma=en`、`idioma=fr` 或
`idioma=zh`（简体中文）作为独立的词写出，例如
`/whatsapp-ai-changelog idioma=zh https://github.com/usuario/repositorio`。不写标记时
一切保持不变。可用语言：`es`（基准语言）、`en`、`fr` 和 `zh`（机器翻译草稿，未经人工
审核；不提供繁体中文）。这些语言的每条回复都以该语言写成的翻译提示开头；你复制到
WhatsApp 的最终消息从不包含该提示。已翻译的文档：[README.en.md](README.en.md)、
[README.fr.md](README.fr.md) 和 [README.zh.md](README.zh.md)，各自配有
`CHANGELOG.<代码>.md` 和 `PRIVACY.<代码>.md`。

消息本身使用你为收件人选择的语言；如果你没有选择，则使用对话所用的语言。界面文本、
`[NOTA]` 标记、等级代码、命令、URL 以及引用的 README 内容不会被翻译。清单文件
（`plugin.json`、marketplace）、`VALIDATION.md`、`MISTRAL.md`、`PERPLEXITY.md` 和
`THIRD_PARTY_NOTICES.md` 仍只提供西班牙语。

要添加一种语言，请按照 `en.md` 的结构创建
`skills/whatsapp-ai-changelog/references/i18n/<代码>.md`，把该代码加入
`skills/whatsapp-ai-changelog/SKILL.md` 的语言块，在 `scripts/package_skills.py` 中
登记该文件，在 `tests/test_i18n.py` 中登记新语言，并添加相应的文档文件。

## 使用方法

```text
/whatsapp-ai-changelog https://github.com/usuario/repositorio
```

你也可以这样请求：“请为这个 AI 工具写一条 WhatsApp 消息：[仓库链接]”。

1. 读取 README，并在需要描述最新更新时，始终检查 GitHub 上最新的稳定版本，即使
   README 已经提到某个版本。
2. 询问收件人的画像，然后逐个提出经过调整的五个访谈问题。
3. 生成 200–350 字、符合 WhatsApp 格式的草稿。
4. 按 30 条标准评估，并给出分数、优点、不足和一张表格。
5. 允许你反复修改，并交付可直接复制粘贴的干净文本。

分数是从收件人的角度估计消息的质量；它不是经过校准的回复概率。即使 README 没有版本
章节，也会使用已核实的 GitHub 版本说明。只有当两个来源都无法提供可核实的变更时，才会
仅限于已有文档记录的功能，并说明这一限制。如果无法核实最新发布的版本，就不会把
README 中的某个版本当作最新版本。该插件只负责撰写消息，不负责发送。

## 在 Claude Code 中安装

本仓库发布后：

```text
/plugin marketplace add novanoticia/whatsapp-ai-changelog-plugin
/plugin install whatsapp-ai-changelog@whatsapp-ai-changelog-plugin
```

在使用带命名空间命令名称的客户端中，命令可能是
`/whatsapp-ai-changelog:whatsapp-ai-changelog [URL]`。

要在 Claude Code 中试用本地文件夹：

```sh
claude --plugin-dir /ruta/whatsapp-ai-changelog-plugin
```

## 在 Mistral Work 中安装

使用 [GitHub Releases](https://github.com/novanoticia/whatsapp-ai-changelog-plugin/releases/latest)
中的资源 **whatsapp-ai-changelog-mistral-1.7.0.zip**。解压后，用
`whatsapp-ai-changelog/` 文件夹创建一个技能。评估协议已作为内部参考资料包含在内；
只需一个技能即可。Claude 插件的 ZIP 格式不同。导入文件夹或使用编辑器的方法，请参见
[MISTRAL.md](MISTRAL.md)（西班牙语）。

## 在 Perplexity Computer 中安装

使用 [GitHub Releases](https://github.com/novanoticia/whatsapp-ai-changelog-plugin/releases/latest)
中的 **whatsapp-ai-changelog-perplexity-1.7.0.zip**，并通过
**Skills → Create skill → Upload a skill** 直接上传。只注册
`whatsapp-ai-changelog`：Bayesian Compose 方法已包含在参考资料中，从而避免出现
同名的第二个技能。详情请参见 [PERPLEXITY.md](PERPLEXITY.md)（西班牙语）。

## 其他客户端

根目录包含供支持 Agent Plugins 1.0.0 的客户端使用的 `plugin.json`，`skills/` 目录
包含两个 SKILL.md 格式的技能。能否从 GitHub 安装取决于客户端。对 ChatGPT/Codex 的
支持需要在其自带的安装器中确认；本软件包本身不会在其目录中创建或注册插件。

对于逐个导入插件技能的其他客户端，请导入**两个**文件夹：
`skills/whatsapp-ai-changelog/` 和 `skills/bayesian-compose/`。

## 要求

一个兼容技能的助手，并能通过浏览或已授权的连接器读取 GitHub。如果它无法读取仓库，
你可以粘贴或附上 README 和版本说明。不需要 MCP 服务器、WhatsApp 凭据或可执行代码。

## 结构

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

## 来源与许可

主技能来自 Pablo 的 `whatsapp-ai-changelog.zip`。Bayesian Compose 来自
[novanoticia/bayesian-compose-plugin](https://github.com/novanoticia/bayesian-compose-plugin)，
并保留其量表和协议。文件与哈希值请参见
[THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)。采用 Apache-2.0 许可；参见
[LICENSE](LICENSE)。

由 AI 辅助编写；需要人工审核。
