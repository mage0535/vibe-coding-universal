<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0.0-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge">
</p>

<h1 align="center">🚀 Vibe Coding Universal v2.0</h1>

<p align="center">
  <strong>从模糊想法到精确设计规范 + 可执行代码方案 — 全流程 pipeline。</strong><br>
  <em>From vague idea → precise design spec → build plan. Feed directly into vibe coding tools.</em>
</p>

<p align="center">
  <a href="#-whats-new-in-v30">What's New</a> •
  <a href="#-why-this-exists">Why</a> •
  <a href="#-how-it-works">How</a> •
  <a href="#-installation">Install</a> •
  <a href="#-usage">Use</a> •
  <a href="#-acknowledgements">Thanks</a>
</p>

---

## ✨ What's New in v2.0

v1.0 只做需求调研和开发指导书。v2.0 是一次**架构级升级**：

| v1.0 (旧) | v2.0 (新) |
|-----------|-----------|
| 7 轮需求澄清 | 7 轮需求澄清 + **7轮设计偏好澄清** |
| 无设计规范 | **完整 DESIGN_SPEC.md**（10段: 色彩/字体/组件/布局/阴影/响应式） |
| 单一 guide.md | **多文档 Build Spec 包**（PRD + Design + Architecture + Tasks + Constitution） |
| 无参考源 | **71 套品牌设计系统**（Stripe/Linear/Airbnb/Apple…） |
| 手写样式 | **精确 CSS token** 输出，vibe coding 工具直接可用 |
| — | **GitHub Spec Kit 兼容**输出格式 |

---

## 💡 为什么会有这个项目

### 我们遇到的问题

在实际使用 AI 辅助开发（Vibe Coding）的过程中，反复遇到以下痛点：

1. **AI 生成的设计千篇一律** — 每次都是"蓝色按钮 + 白色卡片 + Inter 字体"，没有任何视觉个性
2. **需求理解偏差** — 用户说"做个好看的工具网站"，AI 的理解和用户期望的差距巨大
3. **改设计改到吐** — 用户看了第一版不满意，反复沟通调整 UI，来回十几轮
4. **技术方案与设计脱节** — 架构设计不考虑 UI 约束，代码实现时才发现设计不合理
5. **vibe coding 工具缺乏上下文** — 把需求文档丢给 Claude Code，它仍然有很多设计决策需要自己猜

### 我们的解决思路

**问题的本质不是 AI 不够聪明，而是它缺少结构化的设计上下文。**

专业设计师有 Figma、有 Design System、有 Moodboard，而 AI 只有一句"做个好看的页面"。

所以我们把整个流程重新设计为：

```
模糊想法
  → 结构化 PRD（需求确认）
     → 7轮设计偏好对话（风格/色彩/字体/布局/交互）
        → 匹配71套品牌设计系统，生成精确的 DESIGN_SPEC
           → 用户一次性确认设计
              → 技术架构 + 任务规划
                 → 合并为 Build Spec 包
                    → 交付给 vibe coding 工具
```

**核心思想：在 AI 写第一行代码之前，把设计决策全部做完。**

---

## 🔧 工作原理

### 6 步 Pipeline

```
Step 1: 需求分析 ─────→ requirements.md
Step 2: 设计澄清 ─────→ design-brief.md（7轮结构化对话）
Step 3: 设计规范 ─────→ DESIGN_SPEC.md（参考71套品牌）
           ↓ 用户确认
Step 4: 架构设计 ─────→ architecture.md
Step 5: 任务规划 ─────→ tasks.md
Step 6: 合并输出 ─────→ specs/ 目录（Build Spec 包）
```

### Step 2: 设计澄清协议

这是 v2.0 的核心创新。我们用 Structured Q&A 取代开放式提问：

| 轮次 | 维度 | 问题示例 | 选项 |
|------|------|---------|------|
| 1 | 项目类型 | "Web/移动端/桌面？" | Web / iOS / Android / Desktop |
| 2 | 视觉风格 | "有喜欢的品牌风格吗？" | Stripe / Linear / Airbnb / Vercel / Apple / 自定义 |
| 3 | 色彩氛围 | "想要什么色调和感觉？" | 冷色/暖色/暗色/亮色。专业/温暖/科技感 |
| 4 | 排版 | "字体风格？" | Sans-serif / Serif / Mono |
| 5 | 交互 | "交互复杂度？" | 简约 / 标准 / 复杂 |
| 6 | 布局 | "页面结构？" | 单页 / 多页面 / 仪表盘 / 卡片网格 |
| 7 | 特殊需求 | "暗色模式/多语言？" | 暗色 / 国际化 / 无障碍 / 无 |

**每轮只问一个问题，用选项降低用户决策成本。**

### Step 3: 设计规范生成

基于用户在 Step 2 的选择，从 71 套品牌设计系统中匹配 2-3 个最接近的参考，然后生成包含以下 10 段的完整设计规范：

1. **Visual Theme** — 视觉氛围描述（AI 读这段理解设计意图）
2. **Color Palette** — 精确色板（hex + CSS 变量 + 使用场景）
3. **Typography** — 字体栈 + 字号体系表
4. **Components** — 按钮/卡片/输入框/导航/标签（精确 CSS 值）
5. **Layout** — 8px 网格 + 容器 + 响应式栅格
6. **Elevation** — 阴影层级表
7. **Do's & Don'ts** — 设计约束清单
8. **Responsive** — 断点和折叠策略
9. **Agent Prompt Guide** — 可直接粘贴给 Claude Code 的速查

### 品牌自动匹配

不同类型自动对应最佳参考品牌：

| 项目类型 | 自动匹配 |
|---------|---------|
| SaaS / B2B | Stripe + Linear + Vercel |
| 消费类 / 电商 | Airbnb + Shopify |
| 数据仪表盘 | PostHog + Stripe + ClickHouse |
| AI / LLM 工具 | Claude + Vercel + Cursor |
| 移动端 App | Airbnb + Uber + Linear |
| 金融 / Fintech | Stripe + Coinbase + Wise |
| 奢华 / 高端 | Apple + Tesla + BMW |

---

## 📦 安装方法

### 适用平台

| AI 工具 | 安装方式 | 状态 |
|---------|---------|------|
| **Hermes Agent** | 放入 `~/.hermes/skills/`，用 `/skill vibe-coding-universal` 激活 | ✅ 原生支持 |
| **Claude Code** | 放入 `.claude/skills/` 或直接在对话中粘贴 SKILL.md | ✅ 支持 |
| **OpenAI Codex** | 放入项目根目录的 `.agents/skills/` | ✅ 支持 |
| **Cursor** | 复制 SKILL.md 内容到 `.cursor/rules/` | ✅ 支持 |
| **GitHub Copilot** | 放入 `.github/copilot-instructions.md` 引用 | ✅ 支持 |
| **Gemini CLI** | 复制 SKILL.md 到项目根目录 | ✅ 支持 |
| **通义千问 / Kimi** | 直接粘贴 SKILL.md 内容到对话 | ✅ 支持 |

### 安装步骤

#### 方法 1: Git Clone（推荐，获得完整知识库）

```bash
# 克隆项目（包含 71 套品牌 DESIGN.md 参考）
git clone https://github.com/magicwe/vibe-coding-universal.git ~/.vibe-universal

# Hermes Agent 安装
ln -s ~/.vibe-universal ~/.hermes/skills/vibe-coding-universal

# 验证
hermes skills list | grep vibe
```

#### 方法 2: 仅 Skill 文件（最轻量）

```bash
# 下载 SKILL.md
curl -o ~/.hermes/skills/vibe-coding-universal/SKILL.md \
  https://raw.githubusercontent.com/magicwe/vibe-coding-universal/main/SKILL.md

# Claude Code: 复制到项目
cp SKILL.md .claude/skills/vibe-coding-universal.md
```

#### 方法 3: Hermes 技能市场安装

```bash
# 通过 Hermes 的技能市场搜索
hermes skills search vibe-coding-universal

# 安装
hermes skills install vibe-coding-universal
```

### 环境要求

- **Hermes Agent**: v1.0+ （需支持 skill_view 和 delegate_task）
- **Claude Code / Codex / Cursor**: 任意版本
- **依赖 Skill**: `requirements-agent`、`architect-agent`、`writing-plans`（Hermes 环境内自动可用）
- **额外依赖**: 无。不需要安装任何 npm/pip 包。整个工具是一组 SKILL.md 文件。

### 知识库下载（可选，增强设计规范生成）

```bash
# 下载 71 套品牌 DESIGN.md 参考库（67.8k Stars）
git clone --depth 1 https://github.com/VoltAgent/awesome-design-md.git \
  ~/.vibe-universal/awesome-design-md

# 下载 GitHub Spec Kit 模板（官方 spec/plan/tasks 标准格式）
git clone --depth 1 https://github.com/github/spec-kit.git \
  ~/.vibe-universal/spec-kit
```

---

## 🚀 使用方法

### 完整流程（从零开始一个项目）

```bash
# 在 Hermes Agent 中
/skill vibe-coding-universal

# 然后对 AI 说:
"我想做一个团队知识库产品，类似 Notion 但更轻量"
```

AI 将自动:
1. 调用 requirements-agent 生成 PRD
2. 启动 7 轮设计澄清对话
3. 匹配 Linear + Notion 的设计系统，生成 DESIGN_SPEC
4. 等你确认设计
5. 自动完成架构设计、任务规划
6. 输出完整的 Build Spec 包

### 快捷模式（跳过设计澄清）

如果你已经有明确的技术方案和设计想法:

```
"帮我做一个 React + Express 的待办事项应用。暗色主题，类似 Linear 风格。"
```

AI 将自动匹配品牌参考（Linear），跳过 7 轮对话，直接生成完整 Build Spec。

### 只做设计规范（已有 PRD）

```
"我已有 PRD（在 docs/requirements.md），帮我生成设计规范。"
```

AI 将跳过 Step 1，直接进入 Step 2-3 的设计澄清和规范生成。

### 输出交付

完成后，你会得到一个 `specs/` 目录:

```
specs/
├── BUILD_SPEC.md           ← 主入口。可直接粘贴给 vibe coding 工具
├── design/DESIGN_SPEC.md   ← 完整设计系统（CSS token 就绪）
├── architecture/ARCHITECTURE.md  ← 技术方案+数据模型
├── tasks/TASKS.md          ← 可执行任务清单
└── constitution/CONSTITUTION.md  ← 项目约束和红线
```

然后：
```bash
# Claude Code
claude --project specs/ --instructions "Follow BUILD_SPEC.md"

# Codex
codex exec "Build according to specs/BUILD_SPEC.md"

# Cursor
# 打开项目，BUILD_SPEC.md 和 DESIGN_SPEC.md 自动作为上下文
```

---

## 🙏 致谢

本项目站在以下开源项目的肩膀上：

| 项目 | 贡献 |
|------|------|
| **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** (67.8k ⭐) | 71 套品牌 DESIGN.md，为设计规范生成提供精确参考 |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** (11.8k ⭐) | 129 套设计系统 + 31 个设计 Skill 模板，启发了 pipeline 架构 |
| **[github/spec-kit](https://github.com/github/spec-kit)** | Spec-Driven Development 方法论和标准模板 |
| **[EnzeD/vibe-coding](https://github.com/EnzeD/vibe-coding)** | Memory Bank 架构基础 |
| **[tukuaiai/vibe-coding-cn](https://github.com/tukuaiai/vibe-coding-cn)** | 四阶段方法论和中文本地化经验 |
| **[alexpate/awesome-design-systems](https://github.com/alexpate/awesome-design-systems)** | 企业级设计系统索引 |
| **[W3C Design Tokens Community Group](https://www.w3.org/community/design-tokens/)** | 设计令牌规范标准 |

---

## 📂 项目结构

```
vibe-coding-universal/
├── SKILL.md                     ← 核心文件（v2.0 统一入口）
├── README.md                    ← 本文件
├── CHANGELOG.md                 ← 版本更新记录
├── v1/                          ← 旧版归档（v2.0 及之前）
│   ├── SKILL.md                 # 旧版核心逻辑
│   ├── vibe_memory.py           # 旧版记忆管理工具
│   └── README_*.md              # 旧版文档
├── design-systems/              ← 设计系统知识库（可选下载）
│   └── (awesome-design-md 71套 DESIGN.md)
└── templates/                   ← Spec Kit 标准模板
    └── (spec-kit templates)
```

---

<p align="center">
  <em>Built with ❤️ for developers who are tired of generic AI-generated UI.</em>
</p>
