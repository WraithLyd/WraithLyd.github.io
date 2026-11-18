"""MkDocs hook：
1. 给每页算「字数 / 约几分钟」，写进 page.meta（供 partials/source-file.html 使用）；
2. 在首页追加「最近更新」列表（按 git 最后一次提交时间排序）；
3. 把首页里的 <!-- nb-stats --> 换成站点统计（篇数 / 字数 / 板块数）。

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
H2_RE = re.compile(r'^##\s+(.+)$', re.M)

SECTION_NAMES = {
    'course': '课程',
    'read': '读书',
    'tool': '工具',
    'collection': '收藏',
    'life': '生活',
}

RECENT_LIMIT = 6

STATS_PLACEHOLDER = '<!-- nb-stats -->'

_recent_md: str | None = None
_stats_html: str | None = None


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
        text = path.read_text(encoding='utf-8-sig')  # 去掉 BOM，否则第一行 # 匹配不到
    except OSError:
        return path.stem
    # 先去掉 front matter / 代码块 / HTML 注释，否则代码里的 "# <class 'str'>" 会被当成标题
    text = FRONT_MATTER_RE.sub('', text)
    text = FENCE_RE.sub('', text)
    text = re.sub(r'<!--.*?-->', '', text, flags=re.S)
    for pattern in (HEADING_RE, H2_RE):
        m = pattern.search(text)
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


def _build_stats(docs_dir: Path) -> str:
    """首页站点统计：正文笔记篇数、总字数、板块数。"""
    pages = 0
    words = 0
    for md in docs_dir.rglob('*.md'):
        rel = md.relative_to(docs_dir).as_posix()
        if rel == 'index.md' or rel.endswith('/index.md'):
            continue
        try:
            text = md.read_text(encoding='utf-8-sig')
        except OSError:
            continue
        pages += 1
        words += _count_words(text)[0]

    wan = words / 10000
    if wan >= 1:
        words_value, words_label = f'{wan:.1f}'.removesuffix('.0'), '万字'
    else:
        words_value, words_label = str(words), '字'
    items = [
        (str(pages), '篇笔记'),
        (words_value, words_label),
        (str(len(SECTION_NAMES)), '个板块'),
    ]
    values = ''.join(
        f'<div class="nb-stats__item">'
        f'<span class="nb-stats__value">{v}</span>'
        f'<span class="nb-stats__label">{label}</span></div>'
        for v, label in items
    )
    return f'<div class="nb-stats">{values}</div>\n'


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
    global _recent_md, _stats_html

    page.meta = dict(page.meta or {})
    total, minutes = _count_words(markdown)
    if total >= 60:  # 索引页这类很短的不显示
        page.meta['nb_words'] = total
        page.meta['nb_minutes'] = minutes

    if page.file.src_uri == 'index.md':
        if STATS_PLACEHOLDER in markdown:
            if _stats_html is None:
                try:
                    _stats_html = _build_stats(Path(config.docs_dir))
                except Exception as exc:  # 统计失败不影响首页
                    print(f'[recent_updates] 跳过站点统计：{exc}')
                    _stats_html = ''
            markdown = markdown.replace(STATS_PLACEHOLDER, _stats_html)

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
