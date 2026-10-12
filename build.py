#!/usr/bin/env python3
"""
Bundle the kotoSay pitch deck into ONE self-contained index.html.

    python build.py           build once
    python build.py --watch   rebuild whenever a file in src/ changes

Only the Python standard library is used. Nothing is fetched from the
network, so the deck works offline (handy on competition Wi-Fi).
"""
from __future__ import annotations

import base64
import mimetypes
import re
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
OUT = ROOT / "index.html"

# Order matters: tokens → base → deck chrome → per-slide styles.
STYLES = ["tokens.css", "base.css", "deck.css", "slides.css"]
SCRIPTS = ["spring.js", "deck.js"]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def inline_assets(html: str) -> str:
    """Turn src="assets/..." and poster="assets/..." into data: URIs,
    so index.html stays one self-contained file (images and video included)."""
    def to_data_uri(match: re.Match) -> str:
        attr, rel = match.group(1), match.group(2)
        path = SRC / rel
        if not path.is_file():
            raise SystemExit(f"Missing asset: src/{rel}")
        mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
        data = base64.b64encode(path.read_bytes()).decode("ascii")
        return f'{attr}="data:{mime};base64,{data}"'

    return re.sub(r'\b(src|poster)="(assets/[^"]+)"', to_data_uri, html)


def build() -> None:
    template = read(SRC / "template.html")

    css = "\n".join(read(SRC / "styles" / name).rstrip() for name in STYLES)

    slide_files = sorted((SRC / "slides").glob("*.html"))   # 01-…, 02-…, deck order
    if not slide_files:
        raise SystemExit("No slides found in src/slides/")
    slides = inline_assets("\n\n".join(read(f).strip() for f in slide_files))

    js = "\n".join(read(SRC / "scripts" / name).rstrip() for name in SCRIPTS)
    if "</script" in js.lower():
        raise SystemExit("A script contains '</script' which would break inlining.")

    html = (
        template.replace("/*@STYLES@*/", css)
        .replace("<!--@SLIDES@-->", slides)
        .replace("/*@SCRIPTS@*/", js)
    )
    with open(OUT, "w", encoding="utf-8", newline="\n") as f:  # same output on Windows and macOS
        f.write(html)
    size_kb = OUT.stat().st_size / 1024
    print(f"Built {OUT.name}: {len(slide_files)} slides, {size_kb:.0f} KB")


def snapshot() -> dict[Path, float]:
    return {p: p.stat().st_mtime for p in SRC.rglob("*") if p.is_file()}


def watch() -> None:
    print("Watching src/ for changes. Press Ctrl+C to stop.")
    before = snapshot()
    build()
    try:
        while True:
            time.sleep(0.4)
            now = snapshot()
            if now != before:
                before = now
                try:
                    build()
                except Exception as exc:  # keep watching after a bad save
                    print(f"Build failed: {exc}")
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    watch() if "--watch" in sys.argv[1:] else build()
