#!/usr/bin/env python3
"""
Static site generator for CWE Hardware Security Documentation.

Usage:
    python3 build.py

Output: ./site/

Edit style.css and script.js in this directory, then re-run to update the site.
"""

import os
import re
import json
import shutil
from pathlib import Path

ROOT = Path(__file__).parent
SITE = ROOT / "site"


# ── Inline Markdown → HTML ─────────────────────────────────────────────────────

def inline_md(text):
    """Convert inline markdown (bold, links, italic, code) to HTML."""
    # Bold: **text**
    text = re.sub(r'\*\*([^*\n]+?)\*\*', r'<strong>\1</strong>', text)
    # Links: [label](url) — .md links become .html (internal), others open new tab
    def replace_link(m):
        label, href = m.group(1), m.group(2)
        if href.endswith('.md'):
            return f'<a href="{href[:-3]}.html">{label}</a>'
        return f'<a href="{href}" target="_blank" rel="noopener noreferrer">{label}</a>'
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace_link, text)
    # Italic: *text* (single asterisk, not **)
    text = re.sub(r'(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', text)
    # Inline code: `text`
    text = re.sub(r'`([^`\n]+)`', r'<code>\1</code>', text)
    return text


# ── Badge Detection ────────────────────────────────────────────────────────────

# Words that should be rendered as colored badges in table cells
BADGE_WORDS = {'critical', 'high', 'medium', 'low'}

def maybe_badge(cell_text):
    """Wrap known priority/severity words in a badge span."""
    stripped = cell_text.strip()
    if stripped.lower() in BADGE_WORDS:
        cls = f'badge-{stripped.lower()}'
        return f'<span class="badge {cls}">{stripped}</span>'
    return inline_md(cell_text)


# ── Table Renderer ─────────────────────────────────────────────────────────────

def render_table(table_lines):
    """Convert a list of markdown table lines into an HTML <table>."""
    rows = []
    for line in table_lines:
        # Split on | and strip outer empties (from leading/trailing |)
        parts = line.split('|')
        cells = [c.strip() for c in parts[1:-1]] if len(parts) >= 3 else []
        if cells:
            rows.append(cells)

    # Need at least header row + separator row
    if len(rows) < 2:
        return ''

    html = ['<div class="table-wrapper"><table>']

    # Header row
    html.append('<thead><tr>')
    for cell in rows[0]:
        html.append(f'<th>{inline_md(cell)}</th>')
    html.append('</tr></thead>')

    # Body rows (rows[1] is the --- separator, skip it)
    html.append('<tbody>')
    for row in rows[2:]:
        if not any(c for c in row):
            continue
        html.append('<tr>')
        for cell in row:
            html.append(f'<td>{maybe_badge(cell)}</td>')
        html.append('</tr>')
    html.append('</tbody>')

    html.append('</table></div>')
    return '\n'.join(html)


# ── Block Markdown → HTML ──────────────────────────────────────────────────────

def md_to_html(text):
    """
    Convert a subset of Markdown to HTML.
    Handles: headings (H1–H3), tables, horizontal rules, paragraphs,
             inline bold/italic/links/code.
    """
    lines = text.split('\n')
    out = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # ── Blank line ─────────────────────────────────────────────────────────
        if not line.strip():
            i += 1
            continue

        # ── Horizontal rule (--- not part of a table) ──────────────────────────
        if re.match(r'^---+\s*$', line) and not (
            i + 1 < len(lines) and '|' in lines[i + 1]
        ):
            out.append('<hr>')
            i += 1
            continue

        # ── Heading ────────────────────────────────────────────────────────────
        m = re.match(r'^(#{1,6})\s+(.+)', line)
        if m:
            level = len(m.group(1))
            content = m.group(2).strip()
            # Generate a clean anchor id from the heading text
            anchor = re.sub(r'[^\w\s-]', '', content.lower())
            anchor = re.sub(r'\s+', '-', anchor).strip('-')
            out.append(f'<h{level} id="{anchor}">{inline_md(content)}</h{level}>')
            i += 1
            continue

        # ── Table ──────────────────────────────────────────────────────────────
        # Detect: current line has | AND next line has | and is a separator row
        if ('|' in line
                and i + 1 < len(lines)
                and '|' in lines[i + 1]
                and re.match(r'^[\|\s\-:]+$', lines[i + 1].strip())):
            table_lines = [line]
            j = i + 1
            while j < len(lines) and '|' in lines[j]:
                table_lines.append(lines[j])
                j += 1
            out.append(render_table(table_lines))
            i = j
            continue

        # ── Paragraph (collect consecutive non-special lines) ─────────────────
        para = []
        while i < len(lines):
            l = lines[i]
            if not l.strip():
                break
            if re.match(r'^#{1,6}\s', l):
                break
            if re.match(r'^---+\s*$', l):
                break
            if ('|' in l
                    and i + 1 < len(lines)
                    and '|' in lines[i + 1]
                    and re.match(r'^[\|\s\-:]+$', lines[i + 1].strip())):
                break
            para.append(inline_md(l))
            i += 1
        if para:
            out.append(f'<p>{"<br>".join(para)}</p>')

    return '\n'.join(out)


# ── Index Parser ───────────────────────────────────────────────────────────────

def parse_index(index_path):
    """
    Parse index.md and return a list of category dicts:
      [{ 'id': '1195', 'label': '1195 - ...', 'cwes': [...] }, ...]

    Each CWE entry:
      { 'id': '1059', 'path': 'rel/cwe-1059.md', 'title': '...', 'status': '...', 'is_ref': bool }

    'is_ref' is True when the status contains '↗' (the CWE is primarily in another category).
    """
    content = index_path.read_text()
    categories = []

    # Split content on H2 headings; sections[0] is the preamble before first ##
    sections = re.split(r'^## ', content, flags=re.MULTILINE)

    for section in sections[1:]:
        lines = section.strip().split('\n')
        heading = lines[0].strip()

        m = re.match(r'^(\d+)', heading)
        if not m:
            continue
        cat_id = m.group(1)

        cwes = []
        for line in lines:
            # Match: | [CWE-NNNN](path) | Title | Status |
            m2 = re.match(
                r'^\|\s*\[CWE-(\d+)\]\(([^)]+)\)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|',
                line
            )
            if m2:
                cwes.append({
                    'id':     m2.group(1),
                    'path':   m2.group(2).strip(),
                    'title':  m2.group(3).strip(),
                    'status': m2.group(4).strip(),
                    'is_ref': '↗' in m2.group(4),
                })

        if cwes:
            categories.append({'id': cat_id, 'label': heading, 'cwes': cwes})

    return categories


# ── Navigation HTML Builder ────────────────────────────────────────────────────

def build_nav(categories, active_cwe_id=None, active_cat_id=None, depth=1):
    """
    Build the sidebar <nav> HTML.

    depth=0 → root (index.html), links need no prefix
    depth=1 → one level deep (category subdir), prefix with '../'
    """
    prefix = '../' * depth
    lines = [
        f'<a href="{prefix}index.html" class="nav-home">'
        f'<span class="nav-home-icon">&#8962;</span> Hardware Security CWE</a>',
        '<nav class="sidebar-nav">',
    ]

    for cat in categories:
        is_active = cat['id'] == active_cat_id
        open_attr = ' open' if is_active else ''
        lines += [
            f'<details{open_attr}>',
            f'  <summary>',
            f'    <span class="cat-id">{cat["id"]}</span>',
            f'    <span class="cat-name">{cat["label"].split(" - ", 1)[-1]}</span>',
            f'    <span class="cat-count">{len(cat["cwes"])}</span>',
            f'  </summary>',
            f'  <ul class="cwe-list">',
        ]
        for cwe in cat['cwes']:
            href = prefix + cwe['path'].replace('.md', '.html')
            active_cls = ' class="active"' if cwe['id'] == active_cwe_id else ''
            ref_html = (' <span class="ref-marker" title="Defined in another category">↗</span>'
                        if cwe['is_ref'] else '')
            lines.append(
                f'    <li{active_cls}>'
                f'<a href="{href}">'
                f'<span class="cwe-num">CWE-{cwe["id"]}</span>'
                f'<span class="cwe-title">{cwe["title"]}</span>'
                f'</a>{ref_html}</li>'
            )
        lines += ['  </ul>', '</details>']

    lines.append('</nav>')
    return '\n'.join(lines)


# ── Page Template ──────────────────────────────────────────────────────────────

FOOTER_TEXT = (
    "Some content of this website was produced by AI; "
    "however, everything was human-checked and reviewed. "
    "Source data from <a href=\"https://cwe.mitre.org/\" "
    "target=\"_blank\" rel=\"noopener noreferrer\">MITRE CWE</a>."
)

def render_page(title, content_html, nav_html, depth=1, description=''):
    prefix = '../' * depth
    desc = description or title
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta name="description" content="{desc}">
  <title>{title} — Hardware Security CWE</title>
  <link rel="stylesheet" href="{prefix}style.css">
</head>
<body>

<div class="layout">

  <!-- ═══ SIDEBAR ══════════════════════════════════════════════════════════ -->
  <aside class="sidebar">
    <div class="sidebar-header">
      <input
        type="search"
        id="cwe-search"
        placeholder="Search CWEs… (press /)"
        aria-label="Search CWEs"
        autocomplete="off"
      >
    </div>
    {nav_html}
  </aside>

  <!-- ═══ MAIN CONTENT ═════════════════════════════════════════════════════ -->
  <div class="content-wrapper">
    <main class="content">
      <!-- EDITABLE CONTENT START -->
      <article>
        {content_html}
      </article>
      <!-- EDITABLE CONTENT END -->
    </main>

    <footer>
      {FOOTER_TEXT}
    </footer>
  </div>

</div><!-- /.layout -->

<script src="{prefix}script.js"></script>
</body>
</html>
"""


# ── Index Page Content Builder ─────────────────────────────────────────────────

def build_index_content(categories):
    """Build the HTML body content for the home/index page."""
    # Count unique CWEs (non-ref) and categories
    total_cwes = sum(1 for cat in categories for c in cat['cwes'] if not c['is_ref'])
    total_cats = len(categories)

    parts = [
        '<div class="index-header">',
        '  <h1>Hardware Security CWE Documentation</h1>',
        '  <p class="subtitle">MITRE CWE View 1194 — Hardware Design Security Weaknesses</p>',
        '  <div class="index-stats">',
        f'    <div class="stat-item"><span class="stat-value">{total_cwes}</span>'
        f'<span class="stat-label">CWEs</span></div>',
        f'    <div class="stat-item"><span class="stat-value">{total_cats}</span>'
        f'<span class="stat-label">Categories</span></div>',
        '  </div>',
        '</div>',
        '<div class="category-grid">',
    ]

    for cat in categories:
        unique_cwes = [c for c in cat['cwes'] if not c['is_ref']]
        done = sum(1 for c in unique_cwes if 'Done' in c['status'])

        parts += [
            '<div class="cat-card">',
            '  <div class="cat-card-header">',
            f'    <span class="cat-card-id">{cat["id"]}</span>',
            f'    <h2 class="cat-card-title">{cat["label"].split(" - ", 1)[-1]}</h2>',
            f'    <span class="cat-card-count">{done}/{len(unique_cwes)}</span>',
            '  </div>',
            '  <ul class="cat-card-cwes">',
        ]
        for cwe in unique_cwes:
            href = cwe['path'].replace('.md', '.html')
            parts.append(
                f'  <li><a href="{href}">'
                f'<span class="cwe-id-badge">CWE-{cwe["id"]}</span>'
                f'<span class="cwe-item-title">{cwe["title"]}</span>'
                f'</a></li>'
            )
        parts += ['  </ul>', '</div>']

    parts.append('</div>')  # .category-grid
    return '\n'.join(parts)


# ── Main Build ─────────────────────────────────────────────────────────────────

def main():
    print(f'Building site in: {SITE}')

    # Clean and recreate site/ directory
    if SITE.exists():
        shutil.rmtree(SITE)
    SITE.mkdir()

    # Copy static assets from project root
    for asset in ('style.css', 'script.js'):
        src = ROOT / asset
        if src.exists():
            shutil.copy(src, SITE / asset)
            print(f'  Copied: {asset}')
        else:
            print(f'  WARNING: {asset} not found, skipping')

    # Parse index.md to get all categories and CWE entries
    categories = parse_index(ROOT / 'index.md')
    print(f'  Parsed {len(categories)} categories from index.md')

    # ── Build index.html ───────────────────────────────────────────────────────
    index_content = build_index_content(categories)
    index_nav     = build_nav(categories, depth=0)
    index_html    = render_page(
        title='Hardware Security CWE Documentation',
        content_html=index_content,
        nav_html=index_nav,
        depth=0,
        description='Hardware design security weaknesses (MITRE CWE View 1194)',
    )
    (SITE / 'index.html').write_text(index_html, encoding='utf-8')
    print('  Built: index.html')

    # ── Build individual CWE pages ─────────────────────────────────────────────
    built = set()   # track which html_rel paths we've already generated
    skipped = 0

    for cat in categories:
        for cwe in cat['cwes']:
            html_rel = cwe['path'].replace('.md', '.html')

            # Skip duplicates (refs that point to a file already built)
            if html_rel in built:
                continue
            built.add(html_rel)

            md_path = ROOT / cwe['path']

            # Follow symlinks (symlinked .md files resolve to their real path)
            real_md = md_path.resolve() if md_path.exists() else md_path

            if not real_md.exists():
                print(f'  SKIP  (file not found): {cwe["path"]}')
                skipped += 1
                continue

            # Determine the category from the path prefix (e.g. "1201-core-compute")
            dir_name = cwe['path'].split('/')[0]
            actual_cat_id = dir_name.split('-')[0]

            md_text      = real_md.read_text(encoding='utf-8')
            content_html = md_to_html(md_text)
            nav_html     = build_nav(
                categories,
                active_cwe_id=cwe['id'],
                active_cat_id=actual_cat_id,
                depth=1,
            )
            page_html = render_page(
                title=f'CWE-{cwe["id"]} — {cwe["title"]}',
                content_html=content_html,
                nav_html=nav_html,
                depth=1,
            )

            out_path = SITE / html_rel
            out_path.parent.mkdir(parents=True, exist_ok=True)
            out_path.write_text(page_html, encoding='utf-8')

    print(f'\nDone — {len(built)} pages built, {skipped} skipped.')
    print(f'Open: {SITE / "index.html"}')


if __name__ == '__main__':
    main()
