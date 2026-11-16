"""MkDocs hook：
1. 给每页算「字数 / 约几分钟」，写进 page.meta（供 partials/source-file.html 使用）；
2. 在首页追加「最近更新」列表（按 git 最后一次提交时间排序）。

只在构建时运行，不改变任何笔记原文。
"""
from __future__ import annotations

import math
import re
import subprocess
from datetime import datetime
from pathlib import Path

CJK_RE = re.compile(r'[\u3400-\u4DBF\u4E00-\u9FFF\uF900-\uFAFF]')
WORD_RE = re.compile(r'[A-Za-z0-9_][A-Za-z0-9_\'-]*')
FENCE_RE = re.compile(r'^```.*?^```', re.M | re.S)
INLINE_CODE_RE = re.compile(r'`[^`\n]*`')
FRONT_MATTER_RE = re.compile(r'^---\n.*?\n---\n', re.S)
HEADING_RE = re.compile(r'^#\s+(.+)$', re.M)

SECTION_NAMES = {
    'course': '课程',
    'read': '读书',
    'tool': '工具',
    'collection': '收藏',
    'life': '生活',
}

RECENT_LIMIT = 6

_recent_md: str | None = None


def _repo_root(config) -> Path:
    return Path(config.config_file_path).resolve().parent


def _git_last_commit(root: Path, src_uri: str) -> int | None:
    try:
        out = subprocess.run(
            ['git', 'log', '-1', '--format=%ct', '--', f'docs/{src_uri}'],
            cwd=root, capture_output=True, text=True, timeout=10,
        )
    except (OSError, subprocess.SubprocessError):
        return None
    text = out.stdout.strip()
    return int(text) if text.isdigit() else None


def _page_title(path: Path) -> str:
    try:
        text = path.read_text(encoding='utf-8')
    except OSError:
        return path.stem
    m = HEADING_RE.search(text)
    if m:
        return m.group(1).strip()
    return path.stem


def _build_recent(root: Path, docs_dir: Path) -> str:
    """按 git 提交时间列出最近更新的笔记。"""
    items: list[tuple[int, str, str, str]] = []
    for md in docs_dir.rglob('*.md'):
        rel = md.relative_to(docs_dir).as_posix()
        if rel == 'index.md' or rel.endswith('/index.md'):
            continue
        ts = _git_last_commit(root, rel)
        if ts is None:
            continue
        section = SECTION_NAMES.get(rel.split('/')[0], '') if '/' in rel else ''
        items.append((ts, rel, _page_title(md), section))

    items.sort(reverse=True)
    lines = ['<div class="nb-recent" markdown>', '']
    for ts, rel, title, section in items[:RECENT_LIMIT]:
        date = datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
        meta = ' · '.join(x for x in (date, section) if x)
        lines.append(f'- [{title}]({rel}) <span class="nb-recent__meta">{meta}</span>')
    lines += ['', '</div>', '']
    return '\n'.join(lines)


def _count_words(markdown: str) -> tuple[int, int]:
    text = FRONT_MATTER_RE.sub('', markdown)
    text = FENCE_RE.sub('', text)
    text = INLINE_CODE_RE.sub('', text)
    cjk = len(CJK_RE.findall(text))
    words = len(WORD_RE.findall(text))
    total = cjk + words
    minutes = max(1, math.ceil(cjk / 400 + words / 220))
    return total, minutes


def on_page_markdown(markdown: str, page, config, files):
    global _recent_md

    page.meta = dict(page.meta or {})
    total, minutes = _count_words(markdown)
    if total >= 60:  # 索引页这类很短的不显示
        page.meta['nb_words'] = total
        page.meta['nb_minutes'] = minutes

    if page.file.src_uri == 'index.md':
        if _recent_md is None:
            root = _repo_root(config)
            docs_dir = Path(config.docs_dir)
            try:
                _recent_md = _build_recent(root, docs_dir)
            except Exception as exc:  # 构建不该因为这个小功能挂掉
                print(f'[recent_updates] 跳过最近更新：{exc}')
                _recent_md = ''
        if _recent_md:
            markdown = markdown.rstrip() + '\n\n## 最近更新\n\n' + _recent_md

    return markdown
