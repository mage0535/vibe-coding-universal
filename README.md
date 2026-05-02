<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0.0-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/AI%20Compatible-All%20Models-green?style=for-the-badge" alt="Compatible">
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge" alt="License">
</p>

<h1 align="center">🚀 Vibe Coding Universal v2.0</h1>

<p align="center">
  <strong>从模糊想法到精确设计规范 + 可执行代码方案</strong><br>
  <em>Vague idea → precise design spec → executable build plan</em>
</p>

<p align="center">
  <a href="README_CN.md">📖 中文完整文档</a> •
  <a href="README_EN.md">📖 Full English Doc</a> •
  <a href="#quick-start">⚡ Quick Start</a>
</p>

---

## What is this?

AI coding assistants are great at writing code but terrible at knowing what you want it to **look like**. They default to generic blue-button-white-card layouts that all look the same.

**Vibe Coding Universal v2.0** solves this by adding a **structured design clarification pipeline** before any code is written. It:

1. **Interviews you** about design preferences (7 rounds, one question each)
2. **Matches your preferences** against 71 real-world brand design systems (Stripe, Linear, Airbnb, Apple…)
3. **Generates a precise DESIGN_SPEC.md** with exact colors, typography, component styles, and layout rules
4. **Combines everything** (PRD + Design + Architecture + Tasks) into a single Build Spec package
5. **Feeds directly** into Claude Code, Codex, Cursor, or any vibe coding tool

> **Result**: Your AI coder builds exactly what you imagined — on the first try.

---

## Quick Start

### For Hermes Agent:

```bash
/skill vibe-coding-universal
# Then tell AI: "I want to build [your project idea]"
```

### For Any AI (Claude Code / Codex / Cursor / ChatGPT / Gemini):

Copy [`SKILL.md`](SKILL.md) content, paste to AI, say:
> "Load this skill. Now analyze my project idea."

---

## What's New in v2.0

| Feature | v2.0 | v2.0 |
|---------|------|------|
| Design clarification | ❌ | ✅ 7-round structured dialogue |
| Design spec generation | ❌ | ✅ Full DESIGN_SPEC with CSS tokens |
| Brand references | 0 | 71 (Stripe, Linear, Airbnb…) |
| Output format | Single guide.md | Multi-doc Build Spec package |
| Spec Kit compatible | ❌ | ✅ |
| Auto brand matching | ❌ | ✅ By project type |

---

## Pipeline

```
User idea
  → Step 1: Requirements analysis → PRD
     → Step 2: 7-round design dialogue → Design Brief
        → Step 3: Match 71 brand systems → DESIGN_SPEC
           ↓ User confirms
        → Step 4: Architecture design
        → Step 5: Task planning
        → Step 6: Merge → Build Spec package
           ↓
    Claude Code / Codex / Cursor
```

---

## Compatible With

| AI Tool | Support |
|---------|---------|
| **Hermes Agent** | ✅ Native |
| **Claude Code** | ✅ Skills system |
| **OpenAI Codex** | ✅ Skills system |
| **Cursor** | ✅ Rules system |
| **GitHub Copilot** | ✅ Instructions |
| **Gemini CLI** | ✅ File-based |
| **ChatGPT / Qwen / Kimi** | ✅ Paste SKILL.md |

---

## Install

```bash
# Full install (includes 71 brand design references)
git clone https://github.com/magicwe/vibe-coding-universal.git ~/.vibe-universal
ln -s ~/.vibe-universal ~/.hermes/skills/vibe-coding-universal

# Or skill file only
curl -o ~/.hermes/skills/vibe-coding-universal/SKILL.md \
  https://raw.githubusercontent.com/magicwe/vibe-coding-universal/main/SKILL.md
```

**Zero dependencies. No npm, no pip. Just [`SKILL.md`](SKILL.md).**

---

## Usage Example

```
User: "I want a developer tool discovery platform"

AI:
  Q1/7: Web, mobile, or desktop?
  User: Web
  Q2/7: Any brand styles you like? (Stripe, Linear, Airbnb...)
  User: Linear + Vercel
  Q3/7: Dark or light theme? Color vibe?
  User: Dark, professional, tech feel
  ...

→ AI auto-matches Linear + Vercel DESIGN.md files
→ Generates DESIGN_SPEC with exact hex codes, fonts, spacing
→ User confirms: "Looks great!"
→ AI completes architecture + tasks
→ Output: specs/BUILD_SPEC.md (ready for Claude Code)

Claude Code: $ claude --project specs/ --instructions "Follow BUILD_SPEC.md"
→ Builds the app exactly matching the design spec
```

---

## Acknowledgements

Built on top of:
- [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) (67.8k ⭐) — 71 brand DESIGN.md files
- [open-design](https://github.com/nexu-io/open-design) (11.8k ⭐) — Design system architecture
- [spec-kit](https://github.com/github/spec-kit) — Spec-Driven Development standard
- [vibe-coding](https://github.com/EnzeD/vibe-coding) — Memory Bank foundation
- [vibe-coding-cn](https://github.com/tukuaiai/vibe-coding-cn) — Chinese localization

---

<p align="center">
  📖 <a href="README_CN.md">完整中文文档</a> · <a href="README_EN.md">Full English Documentation</a>
</p>
