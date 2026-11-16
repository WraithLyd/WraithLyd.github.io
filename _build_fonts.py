"""生成站内字体用的 woff2（按 GB2312 + 全站实际用到的字符做子集化）。

依赖：pip install fonttools brotli

源字体放在 fonts-src/（不进版本库，见 .gitignore）：
  - LXGWBright-Regular.ttf   https://github.com/lxgw/LxgwBright/releases（LXGWBright.7z 里）
  - JetBrainsMono.ttf        https://github.com/JetBrains/JetBrainsMono/releases

用法：venv\\Scripts\\python.exe _build_fonts.py
输出：docs/stylesheets/LXGWBright-Regular.woff2、docs/stylesheets/JetBrainsMono.woff2
"""
import pathlib
from fontTools.subset import Subsetter, Options
from fontTools.ttLib import TTFont

ROOT = pathlib.Path(__file__).parent
DOCS = ROOT / 'docs'

EXTRA_CHARS = '“”‘’—…·×÷°≤≥≠±∞√∑∏∫≈∈∉⊂⊃∪∩→←↑↓↔⇒⇔–—〈〉《》「」『』【】〔〕'


def used_chars() -> set[str]:
    chars: set[str] = set()
    chars.update(chr(c) for c in range(0x20, 0x7F))
    # GB2312 全部字符（含 6763 个汉字）
    for b1 in range(0xA1, 0xF8):
        for b2 in range(0xA1, 0xFF):
            try:
                chars.add(bytes([b1, b2]).decode('gb2312'))
            except UnicodeDecodeError:
                pass
    chars.update(EXTRA_CHARS)
    # 全站正文实际出现的字符，确保一个不漏
    for p in DOCS.rglob('*'):
        if p.suffix.lower() in {'.md', '.html', '.yml', '.yaml', '.js', '.py', '.css', '.txt'}:
            try:
                chars.update(p.read_text(encoding='utf-8'))
            except (UnicodeDecodeError, OSError):
                pass
    return {c for c in chars if ord(c) >= 0x20}


def build(src: pathlib.Path, dst: pathlib.Path, chars: set[str]) -> None:
    font = TTFont(str(src))
    cmap = font.getBestCmap()
    targets = [ord(c) for c in chars]
    missing = [c for c in chars if ord(c) not in cmap]
    opts = Options()
    opts.flavor = 'woff2'
    opts.notdef_outline = True
    subsetter = Subsetter(options=opts)
    subsetter.populate(unicodes=targets)
    subsetter.subset(font)
    font.flavor = 'woff2'
    font.save(str(dst))
    font.close()

    check = TTFont(str(dst))
    new_cmap = check.getBestCmap()
    uncovered = [c for c in chars if ord(c) in cmap and ord(c) not in new_cmap]
    check.close()

    print(f'{src.name} -> {dst.name}: {src.stat().st_size:,}B -> {dst.stat().st_size:,}B '
          f'({dst.stat().st_size / src.stat().st_size:.1%})，字形数={len(new_cmap)}，'
          f'源字体缺字={len(missing)}，子集漏字={len(uncovered)}')
    if missing:
        print('  源字体没有的字:', ''.join(sorted(missing))[:200])
    if uncovered:
        raise SystemExit('子集化后仍有字缺失，检查逻辑')


def main() -> None:
    chars = used_chars()
    print(f'需要覆盖的字符数：{len(chars):,}')
    build(ROOT / 'fonts-src' / 'LXGWBright-Regular.ttf',
          DOCS / 'stylesheets' / 'LXGWBright-Regular.woff2', chars)
    build(ROOT / 'fonts-src' / 'JetBrainsMono.ttf',
          DOCS / 'stylesheets' / 'JetBrainsMono.woff2', chars)


if __name__ == '__main__':
    main()
