<p align="center">
  <img src="https://img.shields.io/badge/Version-2.0.0-blue?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge">
  <img src="https://img.shields.io/badge/License-MIT-orange?style=for-the-badge">
</p>

<h1 align="center">🚀 Vibe Coding Universal v2.0</h1>

<p align="center">
  <strong>From vague idea → precise design spec → executable build plan.<br>
  A complete pipeline that feeds directly into vibe coding tools.</strong>
</p>

<p align="center">
  <a href="README_CN.md">中文文档</a> •
  <a href="#-whats-new-in-v30">What's New</a> •
  <a href="#-why-this-exists">Why</a> •
  <a href="#-how-it-works">How</a> •
  <a href="#-installation">Install</a> •
  <a href="#-usage">Use</a>
</p>

---

## ✨ What's New in v2.0

v2.0 handled requirements survey and a basic guide. v2.0 is an **architecture-level upgrade**:

| v2.0 (old) | v2.0 (new) |
|-----------|-----------|
| 7 requirement questions | 7 requirement questions + **7 design preference questions** |
| No design spec | **Full DESIGN_SPEC.md** (10 sections: colors, typography, components, layout, shadows, responsive) |
| Single guide.md | **Multi-doc Build Spec package** (PRD + Design + Architecture + Tasks + Constitution) |
| No references | **71 brand design systems** (Stripe, Linear, Airbnb, Apple…) |
| Manual styling | **Precise CSS token output** – vibe coding tools can use directly |
| — | **GitHub Spec Kit compatible** output format |

---

## 💡 Why This Exists

### The Problems We Faced

Using AI for development (Vibe Coding), we hit these recurring pain points:

1. **AI-generated designs look generic** — Every output is "blue button + white card + Inter font", zero visual personality
2. **Requirements get lost in translation** — User says "make it look nice", AI's interpretation is miles off
3. **Design iteration hell** — User rejects first version, 10+ rounds of back-and-forth tweaking UI
4. **Architecture ignores design constraints** — Tech decisions made without UI context, rework discovered at implementation
5. **Vibe coding tools lack context** — Dumping a requirements doc on Claude Code still leaves too many design decisions to guess

### Our Approach

**The root problem isn't AI intelligence — it's missing structured design context.**

Professional designers have Figma, Design Systems, and Moodboards. AI gets "make it pretty."

So we redesigned the entire workflow:

```
Vague idea
  → Structured PRD (confirmed requirements)
     → 7-round design dialogue (style, color, typography, layout, interaction)
        → Match against 71 brand design systems → generate precise DESIGN_SPEC
           → User confirms design ONCE
              → Tech architecture + task planning
                 → Merge into Build Spec package
                    → Feed to vibe coding tools
```

**Core insight: Make all design decisions BEFORE the first line of code.**

---

## 🔧 How It Works

### 6-Step Pipeline

```
Step 1: Requirements   ──→ requirements.md
Step 2: Design Clarify ──→ design-brief.md (7-round structured dialogue)
Step 3: Design Specs   ──→ DESIGN_SPEC.md (matched against 71 brands)
           ↓ User confirms
Step 4: Architecture   ──→ architecture.md
Step 5: Task Planning  ──→ tasks.md
Step 6: Merge & Output ──→ specs/ directory (Build Spec package)
```

### Step 2: Design Clarification Protocol

v2.0's core innovation. Structured Q&A replaces open-ended questions:

| Round | Dimension | Example | Options |
|-------|-----------|---------|---------|
| 1 | Project type | "Web, mobile, or desktop?" | Web / iOS / Android / Desktop |
| 2 | Visual style | "Any brand styles you like?" | Stripe / Linear / Airbnb / Vercel / Apple / Custom |
| 3 | Color & mood | "What tone and feel?" | Cool/Warm/Neutral. Professional/Warm/Tech |
| 4 | Typography | "Font preference?" | Sans-serif / Serif / Mono |
| 5 | Interaction | "How complex?" | Simple / Standard / Complex |
| 6 | Layout | "Page structure?" | Single-page / Multi-page / Dashboard / Card grid |
| 7 | Special needs | "Dark mode? i18n?" | Dark / i18n / Accessibility / None |

**One question per round. Options reduce decision fatigue.**

### Step 3: Design Spec Generation

Based on user's Step 2 choices, match 2-3 closest brand design systems, then generate a 10-section design specification:

1. **Visual Theme** — AI reads this to understand design intent
2. **Color Palette** — hex codes + CSS variables + usage mapping
3. **Typography** — font stack + complete type scale table
4. **Components** — buttons, cards, inputs, nav, tags (exact CSS values)
5. **Layout** — 8px grid, container widths, responsive grid
6. **Elevation** — shadow level hierarchy table
7. **Do's & Don'ts** — design constraint checklist
8. **Responsive** — breakpoints and collapse strategy
9. **Agent Prompt Guide** — copy-paste ready quick reference for Claude Code

### Auto-Matched Brand References

| Project Type | Auto-Matched Brands |
|-------------|-------------------|
| SaaS / B2B | Stripe + Linear + Vercel |
| Consumer / E-commerce | Airbnb + Shopify |
| Dashboards | PostHog + Stripe + ClickHouse |
| AI / LLM tools | Claude + Vercel + Cursor |
| Mobile apps | Airbnb + Uber + Linear |
| Fintech | Stripe + Coinbase + Wise |
| Luxury / Premium | Apple + Tesla + BMW |

---

## 📦 Installation

### Supported Platforms

| AI Tool | Installation | Status |
|---------|-------------|--------|
| **Hermes Agent** | Place in `~/.hermes/skills/`, activate with `/skill vibe-coding-universal` | ✅ Native |
| **Claude Code** | Place in `.claude/skills/` or paste SKILL.md into conversation | ✅ Supported |
| **OpenAI Codex** | Place in `.agents/skills/` in project root | ✅ Supported |
| **Cursor** | Copy SKILL.md to `.cursor/rules/` | ✅ Supported |
| **GitHub Copilot** | Reference in `.github/copilot-instructions.md` | ✅ Supported |
| **Gemini CLI** | Copy SKILL.md to project root | ✅ Supported |
| **Any AI assistant** | Paste SKILL.md content directly into conversation | ✅ Universal |

### Option 1: Git Clone (Recommended — Full Knowledge Base)

```bash
git clone https://github.com/magicwe/vibe-coding-universal.git ~/.vibe-universal

# For Hermes Agent
ln -s ~/.vibe-universal ~/.hermes/skills/vibe-coding-universal

# Verify
hermes skills list | grep vibe
```

### Option 2: Skill File Only (Lightweight)

```bash
# Download SKILL.md
curl -o ~/.hermes/skills/vibe-coding-universal/SKILL.md \
  https://raw.githubusercontent.com/magicwe/vibe-coding-universal/main/SKILL.md

# For Claude Code, copy to project
cp SKILL.md .claude/skills/vibe-coding-universal.md
```

### Option 3: Hermes Skill Market

```bash
hermes skills search vibe-coding-universal
hermes skills install vibe-coding-universal
```

### Requirements

- **Hermes Agent**: v1.0+ (supports skill_view and delegate_task)
- **Claude Code / Codex / Cursor**: any version
- **Dependencies**: `requirements-agent`, `architect-agent`, `writing-plans` (auto-available in Hermes)
- **Zero npm/pip dependencies** — the entire tool is SKILL.md files.

### Optional: Download Design Knowledge Base

```bash
# 71 brand DESIGN.md references (67.8k Stars)
git clone --depth 1 https://github.com/VoltAgent/awesome-design-md.git \
  ~/.vibe-universal/awesome-design-md

# GitHub Spec Kit templates (official spec/plan/tasks format)
git clone --depth 1 https://github.com/github/spec-kit.git \
  ~/.vibe-universal/spec-kit
```

---

## 🚀 Usage

### Full Pipeline (Start From Scratch)

```bash
# In Hermes Agent
/skill vibe-coding-universal

# Then tell AI:
"I want to build a team knowledge base product, like Notion but lighter"
```

The AI will automatically:
1. Call requirements-agent to produce PRD
2. Launch 7-round design clarification dialogue
3. Match Linear + Notion design systems, generate DESIGN_SPEC
4. Wait for your design confirmation
5. Auto-complete architecture + task planning
6. Output complete Build Spec package

### Quick Mode (Skip Design Clarification)

If you already have clear ideas:

```
"Build me a React + Express todo app. Dark theme, Linear-style."
```

AI auto-matches brand refs (Linear), skips the 7-round dialogue, generates everything directly.

### Design-Only Mode (PRD Already Exists)

```
"I have a PRD at docs/requirements.md. Generate design specs."
```

AI skips Step 1, goes directly to Steps 2-3 for design specs.

### Output

You'll get a `specs/` directory:

```
specs/
├── BUILD_SPEC.md           ← Main entry (paste directly to vibe coding tools)
├── design/DESIGN_SPEC.md   ← Full design system (CSS token ready)
├── architecture/ARCHITECTURE.md
├── tasks/TASKS.md
└── constitution/CONSTITUTION.md
```

Then feed to your vibe coding tool:

```bash
# Claude Code
claude --project specs/ --instructions "Follow BUILD_SPEC.md"

# Codex
codex exec "Build according to specs/BUILD_SPEC.md"

# Cursor
# Open the project — BUILD_SPEC.md and DESIGN_SPEC.md are auto-detected as context
```

---

## 🙏 Acknowledgements

This project stands on the shoulders of these open-source giants:

| Project | Contribution |
|---------|-------------|
| **[VoltAgent/awesome-design-md](https://github.com/VoltAgent/awesome-design-md)** (67.8k ⭐) | 71 brand DESIGN.md files for precise design reference |
| **[nexu-io/open-design](https://github.com/nexu-io/open-design)** (11.8k ⭐) | 129 design systems + 31 skill templates, inspired pipeline architecture |
| **[github/spec-kit](https://github.com/github/spec-kit)** | Spec-Driven Development methodology and templates |
| **[EnzeD/vibe-coding](https://github.com/EnzeD/vibe-coding)** | Memory Bank architecture foundation |
| **[tukuaiai/vibe-coding-cn](https://github.com/tukuaiai/vibe-coding-cn)** | Four-phase methodology and Chinese localization |
| **[alexpate/awesome-design-systems](https://github.com/alexpate/awesome-design-systems)** | Enterprise design system index |
| **[W3C Design Tokens CG](https://www.w3.org/community/design-tokens/)** | Design token specification standard |

---

## 📂 Project Structure

```
vibe-coding-universal/
├── SKILL.md                     ← Core file (v2.0 unified entry)
├── README.md                    ← This file
├── CHANGELOG.md                 ← Version history
├── v1/                          ← Archived old versions (v2.0 and earlier)
│   ├── SKILL.md                 # Old core logic
│   ├── vibe_memory.py           # Old memory manager
│   └── README_*.md              # Old docs
├── design-systems/              ← Design system knowledge base (optional)
│   └── (awesome-design-md: 71 DESIGN.md files)
└── templates/                   ← Spec Kit standard templates
    └── (spec-kit templates)
```

---

<p align="center">
  <em>Built for developers tired of generic AI-generated UI.</em>
</p>
