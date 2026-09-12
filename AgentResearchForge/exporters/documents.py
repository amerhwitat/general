from pathlib import Path
from html import escape


def export_markdown(path: str, title: str, body: str, sources: list[dict] | None = None) -> str:
    target = Path(path); target.parent.mkdir(parents=True, exist_ok=True)
    text = f'# {title}\n\n{body}\n'
    if sources:
        text += '\n## Sources\n' + '\n'.join(f'- {s.get("title") or s.get("url")} — {s.get("url", "")}' for s in sources)
    target.write_text(text, encoding='utf-8')
    return str(target)


def export_html(path: str, title: str, body: str, sources: list[dict] | None = None) -> str:
    target = Path(path); target.parent.mkdir(parents=True, exist_ok=True)
    links = ''.join(f'<li><a href="{escape(s.get("url", ""))}">{escape(s.get("title") or s.get("url", "source"))}</a></li>' for s in (sources or []))
    html = f'<!doctype html><html><head><meta charset="utf-8"><title>{escape(title)}</title></head><body><h1>{escape(title)}</h1><p>{escape(body)}</p><h2>Sources</h2><ul>{links}</ul></body></html>'
    target.write_text(html, encoding='utf-8')
    return str(target)


def export_text(path: str, title: str, body: str) -> str:
    target = Path(path); target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(f'{title}\n\n{body}\n', encoding='utf-8')
    return str(target)
