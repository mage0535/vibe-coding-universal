<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0.0-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/AI%20Compatible-All%20Models-green?style=for-the-badge" alt="Compatible">
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" alt="License">
</p>

<h1 align="center">🚀 Vibe Coding Universal Analyzer</h1>

<p align="center">
  <strong>让 AI 听懂你的需求，从第一行代码开始就做对。</strong><br>
  <em>Make AI understand your needs. Get it right from line one.</em>
</p>

<p align="center">
  <a href="#-quick-start">English</a> • 
  <a href="README_CN.md">中文文档</a> • 
  <a href="README_EN.md">Full English Doc</a>
</p>

---

## 💡 这个工具是什么？(What is this?)

你是否经历过：**让 AI 写代码，结果写出一堆 bug，改来改去越改越乱？**
这是因为 AI **没有真正理解你的需求**。

**Vibe Coding Universal Analyzer** 是一个通用的 AI 需求分析技能包。
它可以在写代码前，强制 AI 进行 **"7 轮深度调研"**，生成一份标准化的《开发指导书》。
然后，你可以把这份指导书直接喂给 Claude Code / OpenAI Codex / Cursor，让它们**一次把代码写对**。

**Are you tired of AI writing buggy code?**
That's because it doesn't understand your requirements.
This tool forces AI to **interview you (7 rounds)** before coding, generating a standardized **Blueprint**. Then your AI coder can build it perfectly.

## ✨ 核心亮点 (Features)

- 🧠 **全平台通用**: 兼容 Claude Code, Codex, Cursor, Opencode,Openclaw，Hermes
- 🚫 **零入侵设计**: 绝不修改你的项目文件，只在 `.vibe/` 目录工作。
- 🔄 **记忆进化**: 自动记录客户偏好，越用越懂你。
- 📝 **一键导出**: 自动生成 Claude Code 标准的 `memory-bank/` 和 `AGENTS.md`。

## 🚀 快速上手 (Quick Start)

**无需安装任何软件，只需三步：**

1.  **复制技能**: 复制本项目中的 `SKILL.md` 内容。
2.  **告诉 AI**: 粘贴给 AI 并说 "加载此技能，现在开始调研我的需求"。
3.  **开始开发**: 调研完成后，AI 会生成 `guide.md`，你确认后开始写代码。

## 📂 项目结构 (Structure)

```text
.
├── SKILL.md              # 🧠 核心大脑：包含所有逻辑和提示词
├── vibe_memory.py        # 🛠️ 辅助工具：记忆管理 & 导出 (Python)
├── README_CN.md          # 📖 完整中文文档
├── README_EN.md          # 📖 完整英文文档
└── README.md             # 🏠 首页简介
```

## 🙏 致谢 (Acknowledgements)

本项目灵感来源于以下优秀的开源项目，并在此基础上进行了通用化和自动化优化：
*   [EnzeD/vibe-coding](https://github.com/EnzeD/vibe-coding) - 提供了 Memory Bank 架构基础。
*   [tukuaiai/vibe-coding-cn](https://github.com/tukuaiai/vibe-coding-cn) - 提供了深度的四阶段方法论和中文本地化经验。

---

**Ready to code better? Check out [Full Documentation (中文)](README_CN.md) or [Full Documentation (English)](README_EN.md).**
