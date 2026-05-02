# Changelog

## v3.0.0 (2026-05-02)

### Major Architecture Upgrade

The project underwent a complete architectural redesign, expanding from a 4-phase requirements survey tool to a **6-step full-stack pipeline** covering requirements → design → architecture → tasks → merge → delivery.

### Added

- **7-Round Design Clarification Protocol** (Step 2): Structured Q&A for visual preferences — project type, brand reference, color, typography, interaction, layout, special needs
- **Design Spec Generation** (Step 3): Auto-generates 10-section DESIGN_SPEC.md with exact CSS tokens, color palettes, typography scales, component stylings, and layout specifications
- **71 Brand Design Systems** knowledge base: Integrated [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) (67.8k ⭐) — Stripe, Linear, Airbnb, Apple, Tesla, and 66 more brands as precise design references
- **Auto Brand Matching**: Project type automatically maps to optimal brand design references (e.g., SaaS → Stripe+Linear)
- **Build Spec Merger** (Step 6): Combines PRD + DESIGN_SPEC + Architecture + Tasks into a single Build Spec package
- **GitHub Spec Kit Compatibility**: Output format aligns with [github/spec-kit](https://github.com/github/spec-kit) standard
- **CSS Token Output**: DESIGN_SPEC includes production-ready CSS variables and exact hex values
- **Agent Prompt Guide**: Each DESIGN_SPEC includes a copy-paste ready quick reference for vibe coding tools
- Comprehensive Chinese + English documentation with problem background, methodology, and usage guides

### Changed

- Pipeline expanded from 4 phases to 6 steps
- Design clarification now uses structured options (not open-ended questions)
- Output upgraded from single `guide.md` to multi-document `specs/` package
- `SKILL.md` consolidated from 4 separate skill files into one unified entry
- All v2.0 files archived to `v1/` directory

### Dependencies

- Knowledge bases: awesome-design-md, spec-kit (optional downloads)
- No new npm/pip dependencies

---

## v2.0.0 (2026-04-21)

### Initial Release

- 7-round requirement survey
- 4-phase workflow: Survey → Recall → Document → Confirm
- Memory system with cross-project client profiles
- Claude Code / Codex / Cursor / ChatGPT / Gemini / Qwen compatibility
- Non-invasive workspace (`.vibe/` directory)
- Based on EnzeD/vibe-coding + tukuaiai/vibe-coding-cn methodologies
