---
name: vibe-coding-universal
version: 3.0.0
description: 需求到代码全流程 pipeline — 需求分析 → 7轮设计澄清 → 71套品牌参考生成精确设计规范 → 架构设计 → 任务规划 → 合并为 Build Spec 包交付 vibe coding 工具
author: Hermes Agent
compatible_with: [claude-code, codex, cursor, gemini, qwen, copilot, hermes]
knowledge_base: [awesome-design-md (71 brands), spec-kit (GitHub)]
---

# Vibe Coding Universal v3.0

**从模糊想法到可执行 Build Spec，6 步全流程 pipeline。**

> 知识库: 71 套品牌 DESIGN.md + GitHub Spec Kit 标准模板
> 输出: 符合 Spec Kit 规范的 Build Spec 包 → Claude Code / Codex / Cursor 直接消费

---

## Pipeline 概览

```
Step 1: 需求分析 → PRD
Step 2: 设计澄清 → Design Brief（7轮结构化对话）
Step 3: 设计规范 → DESIGN_SPEC.md（参考71套品牌设计系统）
          ↓ 用户确认
Step 4: 架构设计 → ARCHITECTURE.md（技术选型+数据模型+API）
Step 5: 任务规划 → TASKS.md（按优先级分解可执行任务）
Step 6: 合并输出 → Build Spec 包（specs/目录）
```

---

## Step 2: 设计澄清（7轮结构化对话）

**规则**: 每轮只问一个问题，用选项引导用户。

| 轮次 | 维度 | 选项 |
|------|------|------|
| 1 | 项目类型 & 平台 | Web / iOS / Android / Desktop / 跨平台 |
| 2 | 视觉风格参考 | Stripe / Linear / Airbnb / Vercel / Apple / 自定义 |
| 3 | 色彩与氛围 | 冷色/暖色/中性。专业/温暖/科技感/极简/奢华 |
| 4 | 排版偏好 | Sans-serif / Serif / Mono / 系统默认 |
| 5 | 交互复杂度 | 简约 / 标准 / 复杂 |
| 6 | 布局偏好 | 单页滚动 / 多页面 / 仪表盘 / 卡片网格 |
| 7 | 特殊需求 | 暗色模式 / 多语言 / 无障碍 / 无 |

输出: `docs/design-brief.md`

---

## Step 3: 设计规范生成

**知识库**: 71 套品牌 DESIGN.md（排列在下方品牌分类中）

### 品牌分类速查

| 风格 | 品牌 |
|------|------|
| 精准专业/Fintech | stripe, coinbase, binance, wise, revolut |
| 温暖友好/消费 | airbnb, uber, spotify, pinterest |
| 极简现代/生产力 | linear-app, notion, figma, miro |
| 科技感/DevTools | vercel, cursor, supabase, posthog |
| 奢华高端 | apple, tesla, bmw, ferrari |
| AI/LLM | claude, mistral-ai, cohere, elevenlabs |
| 媒体/内容 | theverge, wired, playstation |

### 自动匹配规则

| 项目类型 | 自动参考品牌 |
|---------|------------|
| SaaS / B2B | stripe + linear-app + vercel |
| 消费类 | airbnb + shopify + stripe |
| 仪表盘 | posthog + stripe + clickhouse |
| AI 工具 | claude + vercel + cursor |
| 移动端 | airbnb + uber + linear-app |
| 金融 | stripe + coinbase + wise |

### DESIGN_SPEC.md 输出结构（10段）

```
1. Visual Theme & Atmosphere  — 视觉氛围描述
2. Color Palette & Roles       — 含hex、CSS变量、用途表
3. Typography Rules            — font stack、type scale、原则
4. Component Stylings          — Buttons/Cards/Inputs/Nav/Tags（精确CSS值）
5. Layout Principles           — 8px grid、container、responsive grid
6. Depth & Elevation           — shadow level table
7. Do's and Don'ts             — 设计约束
8. Responsive Behavior         — breakpoints + collapse策略
9. Agent Prompt Guide          — 可直接粘贴给vibe coding工具的速查
```

---

## Step 6: Build Spec 合并输出

```
{project}/specs/
├── BUILD_SPEC.md           ← 总览入口（可直接粘贴给vibe coding工具）
├── design/DESIGN_SPEC.md   ← 完整设计规范
├── architecture/ARCHITECTURE.md
├── tasks/TASKS.md
└── constitution/CONSTITUTION.md
```

BUILD_SPEC.md 包含 "Quick Start for AI Agent" 段，可直接粘贴给 Claude Code / Codex 使用。

---

## 交付命令

```
Claude Code:  claude --project specs/ --instructions "Follow BUILD_SPEC.md"
Codex:        codex exec "Build according to specs/BUILD_SPEC.md"
Cursor:       打开项目，自动读取 BUILD_SPEC.md 和 DESIGN_SPEC.md
```

---

## 依赖 Skill

| Skill | 步骤 | 调用方式 |
|-------|------|---------|
| `requirements-agent` | Step 1 | delegate_task |
| `architect-agent` | Step 4 | delegate_task |
| `writing-plans` | Step 5 | delegate_task |

*Step 2-3 和 Step 6 由主 Agent 直接执行。*

---

## 使用示例

```
用户: "我想做一个人任务管理 App"

→ 主Agent: 加载 vibe-coding-universal
→ Step 1: delegate_task(requirements-agent) → PRD
→ Step 2: 7轮设计澄清 （Dark mode? → ⌗ Cards layout? → →…）
→ Step 3: 参考 Linear+Notion DESIGN.md → 生成 DESIGN_SPEC
→ [用户确认设计]
→ Step 4-6: 自动完成架构→任务→合并
→ 输出: specs/BUILD_SPEC.md
→ 用户收到: "Build Spec ready. Paste to Claude Code to begin."
```
