from pathlib import Path

import trafilatura
from bs4 import BeautifulSoup, Tag

from config import SITE_DIR, TEXT_DIR

CONTENT_CLASS_NAME: str = "contents"


def html_file_to_md_name(html_file: Path) -> str:
    """Build a flat .md name from a site/ path, e.g. some1/some2/index.html -> some1_some2.md."""
    relative_path = html_file.relative_to(SITE_DIR)
    parts = list(relative_path.parts)
    stem = Path(parts[-1]).stem
    dirs = parts[:-1]
    segments = list(dirs) if stem == "index" else [*dirs, stem]
    return f"{'__'.join(segments)}.md" if segments else "index.md"


def find_content_element(soup: BeautifulSoup) -> Tag | None:
    """Find the div that marks the page's article content block."""
    return soup.select_one(f"div.{CONTENT_CLASS_NAME}")


def html_to_markdown(html: str) -> str | None:
    """Extract the article content block, if found, and convert it to markdown."""
    soup = BeautifulSoup(html, "lxml")
    content_element = find_content_element(soup)
    source_html = html if content_element is None else f"<html><body>{content_element}</body></html>"
    return trafilatura.extract(source_html, output_format="markdown", favor_recall=True)


def extract_site_text() -> None:
    """Convert every downloaded HTML page under SITE_DIR into markdown under TEXT_DIR."""
    TEXT_DIR.mkdir(parents=True, exist_ok=True)
    html_files = sorted(SITE_DIR.rglob("*.html"))
    total_html_chars = 0
    total_md_chars = 0
    converted_count = 0
    failed_count = 0

    for index, html_file in enumerate(html_files, start=1):
        html = html_file.read_text(encoding="utf-8")
        total_html_chars += len(html)
        markdown = html_to_markdown(html)
        if markdown is None:
            failed_count += 1
            print(f"[{index}/{len(html_files)}] skipped (no content block found): {html_file}")
            continue

        md_file = TEXT_DIR / html_file_to_md_name(html_file)
        md_file.write_text(markdown, encoding="utf-8")
        converted_count += 1
        total_md_chars += len(markdown)
        print(
            f"[{index}/{len(html_files)}] {html_file} ({len(html)} chars) "
            f"-> {md_file} ({len(markdown)} chars)"
        )

    print(
        f"total: {converted_count} files, {failed_count} failed, "
        f"{total_html_chars} html chars, {total_md_chars} md chars"
    )


if __name__ == "__main__":
    extract_site_text()
