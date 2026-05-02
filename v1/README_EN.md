# 📘 Vibe Coding Universal Analyzer (English Guide)

> **Target Audience**: Developers, Product Managers, and Creators who want to use AI for coding efficiently.
> **Core Philosophy**: **Planning is everything.** Do not let the AI guess; tell it exactly what to do.

---

## 🤔 Why do you need this tool?

In the era of AI coding (Vibe Coding), the biggest bottleneck isn't the AI's ability to write code — **it's the AI's ability to understand your requirements.**

Common pain points:
1.  **Hallucinated Requirements**: You say "Make a Todo App", and the AI adds features you didn't ask for.
2.  **Spaghetti Code**: Without a plan, the code structure becomes a mess after a few iterations.
3.  **No Memory**: You have to repeat the same constraints to the AI every session.

**Our Solution**:
We encapsulated **Professional Requirement Engineering** into a simple **Dialogue Flow**.
By answering just 7 questions, AI generates a standardized **Blueprint (`guide.md`)**.
This blueprint can then be fed directly into Claude Code, OpenAI Codex, or Cursor to ensure high-quality code generation.

---

## 🏗️ Layered Architecture

We designed this tool to be **Lightweight, Safe, and Universal** through a layered approach:

### Layer 1: Cognitive Layer (`SKILL.md`) — 🧠 The Brain
This is the core. It requires **no code execution environment**.
It contains:
-   **7-Round Survey Logic**: Defines exactly what the AI should ask.
-   **Documentation Templates**: Standardized formats for output.
-   **Non-Invasive Rules**: Ensures the AI never messes up your existing files.

### Layer 2: Memory Layer (`vibe_memory.py`) — 💾 The Memory
A **Zero-Dependency Python Script** (Standard Library only).
It handles:
-   **Archiving**: Saves completed projects to `.vibe/history/`.
-   **Retrieval**: Automatically finds similar past projects to reuse lessons.
-   **Exporting**: Converts `guide.md` into `memory-bank/` format specifically for Claude Code / Codex.

### Layer 3: Execution Layer (`AGENTS.md` / `memory-bank/`) — 🤖 The Hands
Files specifically designed for the coding agents (Claude Code, Codex, etc.).
-   They don't care about the survey process.
-   They only care about the instructions in `AGENTS.md` and the plan in `memory-bank/`.

---

## 🛠️ Installation & Usage

### Scenario A: I am using ChatGPT / Gemini / Qwen (Chat Interface)

1.  **Copy**: Open `SKILL.md` from this repo and **Copy All**.
2.  **Paste**: Paste it into your AI chat.
3.  **Trigger**: Say: "**Load this skill. I want to build a [Project Name]. Start the survey.**"
4.  **Survey**: Answer the AI's 7 questions.
5.  **Build**: Once the `guide.md` is generated, review it and start coding.

### Scenario B: I am using Claude Code / Cursor / Codex CLI (CLI Interface)

1.  **Setup**: In your project root, run:
    ```bash
    mkdir -p .vibe
    # Put SKILL.md and vibe_memory.py here
    ```
2.  **Init**: Run the memory tool:
    ```bash
    python3 vibe_memory.py init
    ```
3.  **Survey**: Open your terminal (`claude`), and ask it to read `SKILL.md`.
4.  **Export**: After the survey is done, run:
    ```bash
    python3 vibe_memory.py export-claude .vibe/guide.md
    ```
5.  **Code**: The tool will generate `AGENTS.md` and `memory-bank/`.
    Your AI coder will automatically pick these up and follow the plan.

---

## 📄 Output Example

After running, you will get a professional blueprint like this:

```markdown
# 📋 Expense Tracker App Development Guide

## 1. Requirements
- One-liner: Minimal personal finance Web App.
- Target: Freelancers who hate Excel.

## 2. Tech Stack
- Frontend: React + Tailwind
- Backend: Supabase (No-ops)

## 3. Implementation Plan
- [ ] Phase 1: Init Project (npm create)
- [ ] Phase 2: Core Features (Form + List)
- [ ] Phase 3: Charts (Recharts)
- [ ] Phase 4: Deploy to Vercel
```

---

## 🙏 Acknowledgements & Inspiration

This project stands on the shoulders of giants. We deeply appreciate the following open-source projects:

### 1. Architecture & Standards
- **[EnzeD/vibe-coding](https://github.com/EnzeD/vibe-coding)**: 
  - **Contribution**: Provided the foundational concept of Memory Bank and the AGENTS.md pattern.
  - **Thanks**: To Nicolas Zullo for defining the Vibe Coding workflow.

### 2. Methodology & Localization
- **[tukuaiai/vibe-coding-cn](https://github.com/tukuaiai/vibe-coding-cn)**:
  - **Contribution**: Provided the excellent "4-Stage x 12-Principle" methodology and practical pitfall guides.
  - **Thanks**: To the developer for their dedication to the Chinese Vibe Coding community.

### 3. Unique Optimizations (What we added)
Based on these inspirations, we added:
- ✅ **Universality**: Removed IDE-specific dependencies. Now it's a pure text `SKILL.md` that works everywhere.
- ✅ **Zero-Dependency Memory**: Created `vibe_memory.py` using only Python stdlib. No `pip install` needed.
- ✅ **Automated Export**: Added `export-claude` to bridge the gap between "Requirements" and "Code Generation".

---

**Ready to Vibe Code better?** 🚀
