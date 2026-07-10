from pathlib import Path

import trafilatura

from config import SITE_DIR, TEXT_DIR


def html_file_to_text_path(html_file: Path) -> Path:
    """Map a saved index.html path under SITE_DIR to its .txt path under TEXT_DIR."""
    relative_path = html_file.relative_to(SITE_DIR)
    return TEXT_DIR / relative_path.with_suffix(".txt")


def extract_site_text() -> None:
    """Convert every downloaded HTML page under SITE_DIR into plain text under TEXT_DIR."""
    html_files = sorted(SITE_DIR.rglob("index.html"))
    for index, html_file in enumerate(html_files, start=1):
        html = html_file.read_text(encoding="utf-8")
        text = trafilatura.extract(html)
        if text is None:
            print(f"[{index}/{len(html_files)}] skipped (no content): {html_file}")
            continue

        text_file = html_file_to_text_path(html_file)
        text_file.parent.mkdir(parents=True, exist_ok=True)
        text_file.write_text(text, encoding="utf-8")
        print(f"[{index}/{len(html_files)}] saved {html_file} -> {text_file}")


if __name__ == "__main__":
    extract_site_text()
