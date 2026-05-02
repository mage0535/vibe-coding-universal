#!/usr/bin/env python3
"""
Vibe Memory Manager — 通用记忆管理工具
供任何 AI 助理调用，管理客户画像与历史项目。
零外部依赖（仅 stdlib），任何 Python 3.6+ 环境可用。
"""

import os
import sys
import json
import re
import difflib
from datetime import datetime
from pathlib import Path

VIBE_DIR = Path(".vibe")
HISTORY_DIR = VIBE_DIR / "history"
CLIENT_PROFILE = VIBE_DIR / "client-profile.md"
SESSION_LOG = VIBE_DIR / "session-log.md"


def ensure_vibe_dir():
    """确保 .vibe/ 目录结构存在"""
    VIBE_DIR.mkdir(exist_ok=True)
    HISTORY_DIR.mkdir(exist_ok=True)
    if not CLIENT_PROFILE.exists():
        CLIENT_PROFILE.write_text(
            "# 客户画像\n\n## 技术偏好\n- (待补充)\n\n"
            "## UI 偏好\n- (待补充)\n\n"
            "## 工作习惯\n- (待补充)\n\n"
            "## 历史统计\n- 完成项目数: 0\n- 常用技术: (待补充)\n",
            encoding="utf-8"
        )
        print("📋 客户画像已创建: .vibe/client-profile.md")


def save_session_log(survey_result: dict):
    """保存本次调研记录"""
    ensure_vibe_dir()
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [f"# 调研记录 — {timestamp}", ""]
    for key, val in survey_result.items():
        if isinstance(val, list):
            lines.append(f"## {key}")
            for item in val:
                lines.append(f"- {item}")
        else:
            lines.append(f"## {key}")
            lines.append(f"{val}")
        lines.append("")
    SESSION_LOG.write_text("\n".join(lines), encoding="utf-8")
    print(f"📝 调研记录已保存: .vibe/session-log.md")


def create_history_entry(project_name: str, guide_md: str):
    """将完成的项目归档到 history/"""
    ensure_vibe_dir()
    safe_name = re.sub(r'[^\w\u4e00-\u9fff_-]', '_', project_name)
    date_str = datetime.now().strftime("%Y-%m-%d")
    entry_dir = HISTORY_DIR / f"{date_str}_{safe_name}"
    entry_dir.mkdir(exist_ok=True)
    (entry_dir / "guide.md").write_text(guide_md, encoding="utf-8")
    print(f"📦 项目已归档: {entry_dir}")
    return entry_dir


def search_similar_projects(query: str, top_n: int = 3):
    """
    检索历史相似项目。
    使用纯 Python 实现，零依赖。
    """
    ensure_vibe_dir()
    if not HISTORY_DIR.exists() or not list(HISTORY_DIR.iterdir()):
        print("🔍 暂无历史项目记录。")
        return []

    projects = []
    query_tokens = set(re.findall(r'[a-zA-Z0-9]+|[\u4e00-\u9fa5]', query.lower()))

    for entry_dir in sorted(HISTORY_DIR.iterdir()):
        guide = entry_dir / "guide.md"
        if not guide.exists():
            continue
        content = guide.read_text(encoding="utf-8")
        content_tokens = set(re.findall(r'[a-zA-Z0-9]+|[\u4e00-\u9fa5]', content.lower()))

        if not query_tokens or not content_tokens:
            continue

        # Recall: query 中有多少比例的词出现在目标文档中
        intersection = query_tokens & content_tokens
        recall = len(intersection) / len(query_tokens)
        jaccard = len(intersection) / len(query_tokens | content_tokens)
        score = recall * 0.7 + jaccard * 0.3

        if score > 0.1:  # 低阈值，召回更多候选
            # 提取摘要
            first_300 = content[:300].replace('\n', ' ')
            projects.append({
                "name": entry_dir.name,
                "score": round(score, 3),
                "path": str(entry_dir),
                "summary": first_300
            })

    projects.sort(key=lambda x: x["score"], reverse=True)
    return projects[:top_n]


def update_client_profile(updates: dict):
    """增量更新客户画像"""
    ensure_vibe_dir()
    current = CLIENT_PROFILE.read_text(encoding="utf-8")

    for key, value in updates.items():
        if f"## {key}" in current:
            # 更新已有章节
            pattern = rf"(## {key}\n)(.*?)(?=\n## |\Z)"
            replacement = f"## {key}\n{value}\n"
            current = re.sub(pattern, replacement, current, flags=re.DOTALL)
        else:
            # 追加新章节
            current += f"\n## {key}\n{value}\n"

    # 更新项目统计
    if "完成项目数" in current:
        current = re.sub(
            r"完成项目数: (\d+)",
            lambda m: f"完成项目数: {int(m.group(1)) + 1}",
            current
        )

    CLIENT_PROFILE.write_text(current, encoding="utf-8")
    print("👤 客户画像已更新")




def export_for_claude(guide_md_path: str):
    """
    将 .vibe/guide.md 转换为 Claude Code / OpenCode 可读的标准格式：
    1. AGENTS.md (Claude Code / OpenCode 根指令)
    2. memory-bank/ 目录 (标准化文档)
    """
    guide_path = Path(guide_md_path)
    if not guide_path.exists():
        print(f"❌ 找不到文件: {guide_md_path}")
        return

    content = guide_path.read_text(encoding="utf-8")
    
    # 1. 生成 memory-bank/ 目录结构
    mb_dir = Path("memory-bank")
    mb_dir.mkdir(exist_ok=True)
    
    # 将 guide.md 内容拆分为 memory-bank 标准文件
    # (为保持简单，直接将完整内容作为 activeContext.md，后续 AI 会自动拆分)
    files_map = {
        "activeContext.md": "# 当前开发上下文\n\n> 本文档由 Vibe Analyzer 自动生成。\n> Claude Code / OpenCode 请优先读取此文件作为开发起点。\n\n",
        "productContext.md": "# 产品上下文\n\n",
        "systemPatterns.md": "# 系统架构模式\n\n",
        "progress.md": "# 开发进度\n\n- [ ] 初始化项目\n- [ ] 核心功能\n- [ ] 测试与部署\n\n",
    }
    
    for fname, header in files_map.items():
        (mb_dir / fname).write_text(header + content, encoding="utf-8")
        print(f"📝 已生成: memory-bank/{fname}")

    # 2. 生成 AGENTS.md (Claude Code / OpenCode 读取的入口文件)
    agents_md = Path("AGENTS.md")
    if not agents_md.exists():
        agents_content = """# AGENTS.md

> ⚠️ 本文件由 Vibe Analyzer 自动生成。请勿手动修改。
> Claude Code / OpenCode 启动时，请优先遵循以下规则。

## 核心规则
1. **唯一真理来源**: `memory-bank/` 目录。所有开发决策以此为准。
2. **分步执行**: 严格按照 `memory-bank/activeContext.md` 中的开发计划，每次只做一个小任务。
3. **验证先行**: 每个功能完成后，必须运行测试或手动验证，确认通过再继续。
4. **不要猜测**: 遇到不确定的需求，必须询问人类，禁止自行脑补。
5. **非侵入修改**: 除非必要，不要修改 `.vibe/` 目录之外的配置文件。

## 快速启动
1. 读取 `memory-bank/activeContext.md` 了解当前任务。
2. 检查 `memory-bank/productContext.md` 了解产品目标。
3. 按照开发计划分步实施。
"""
        agents_md.write_text(agents_content, encoding="utf-8")
        print("🤖 已生成: AGENTS.md (Claude Code / OpenCode 入口)")
    else:
        # 如果已存在，追加提示
        print("ℹ️ AGENTS.md 已存在，跳过生成。")

    print("\n✅ 导出完成！现在可以用 Claude Code / OpenCode 打开本项目开始编码。")


def main():
    if len(sys.argv) < 2:
        # ... existing print help ...
        return

        print("用法:")
        print("  python vibe_memory.py init                          # 初始化 .vibe/ 目录")
        print("  python vibe_memory.py search '关键词'                # 搜索相似历史项目")
        print("  python vibe_memory.py archive '项目名' guide.md      # 归档项目")
        print("  python vibe_memory.py update profile.json            # 更新客户画像")
        return

    cmd = sys.argv[1]

    if cmd == "init":
        ensure_vibe_dir()
        print("✅ .vibe/ 目录已初始化")

    elif cmd == "search":
        if len(sys.argv) < 3:
            print("❌ 请提供搜索关键词")
            return
        results = search_similar_projects(" ".join(sys.argv[2:]))
        if results:
            print(f"🔍 找到 {len(results)} 个相似项目:")
            for r in results:
                print(f"  [{r['score']:.0%}] {r['name']}")
                print(f"    路径: {r['path']}")
                print(f"    摘要: {r['summary'][:100]}...")
        else:
            print("🔍 未找到相似项目。")

    elif cmd == "archive":
        if len(sys.argv) < 4:
            print("❌ 用法: python vibe_memory.py archive '项目名' guide.md")
            return
        project_name = sys.argv[2]
        guide_path = sys.argv[3]
        if not os.path.exists(guide_path):
            print(f"❌ 文件不存在: {guide_path}")
            return
        guide_content = Path(guide_path).read_text(encoding="utf-8")
        entry = create_history_entry(project_name, guide_content)
        print(f"✅ 项目已归档到: {entry}")

    elif cmd == "update":
        if len(sys.argv) < 3:
            print("❌ 用法: python vibe_memory.py update profile.json")
            return
        profile_path = sys.argv[2]
        if not os.path.exists(profile_path):
            print(f"❌ 文件不存在: {profile_path}")
            return
        with open(profile_path, encoding="utf-8") as f:
            updates = json.load(f)
        update_client_profile(updates)

    elif cmd == "export-claude":
        if len(sys.argv) < 3:
            print("❌ 用法: python vibe_memory.py export-claude .vibe/guide.md")
            return
        export_for_claude(sys.argv[2])

    else:
        print(f"❌ 未知命令: {cmd}")


if __name__ == "__main__":
    main()
