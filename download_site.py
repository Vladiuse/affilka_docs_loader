import os
import time
from collections import deque
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit, urlunsplit

from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from config import SITE_DIR

load_dotenv()

START_URL: str = "/en/home"
ALLOWED_DOMAIN: str = "wiki.affilka.net"
PAGE_LOAD_WAIT_SECONDS: float = 0.2
EXCLUDED_PATH_PREFIXES: tuple[str, ...] = ("/login", "/logout")

COOKIE_NAME: str = "jwt"
COOKIE_VALUE: str = os.environ["COOKIE_VALUE"]

SITE_ORIGIN: str = f"https://{ALLOWED_DOMAIN}/"


def rewrite_absolute_links(html: str) -> str:
    """Rewrite absolute links to the crawled domain into root-relative paths."""
    return html.replace(SITE_ORIGIN, "/")


def normalize_url(url: str) -> str:
    """Strip the fragment, trailing slash, and .html suffix so equivalent URLs deduplicate."""
    parsed = urlsplit(url)
    path = parsed.path.rstrip("/") or "/"
    if path.endswith(".html"):
        path = path[: -len(".html")]
    return urlunsplit((parsed.scheme, parsed.netloc, path, parsed.query, ""))


def url_to_file_path(url: str) -> Path:
    """Map a URL path to a local index.html file, mirroring the path as folders."""
    path = urlsplit(url).path.strip("/")
    if not path:
        return SITE_DIR / "index.html"
    segments = [unquote(segment) for segment in path.split("/")]
    return SITE_DIR.joinpath(*segments, "index.html")


def is_crawlable(url: str) -> bool:
    """Check that a URL stays on the allowed domain and is a page, not an asset."""
    parsed = urlsplit(url)
    if parsed.scheme not in ("http", "https") or parsed.netloc != ALLOWED_DOMAIN:
        return False
    if parsed.path.startswith(EXCLUDED_PATH_PREFIXES):
        return False
    suffix = PurePosixPath(parsed.path).suffix
    return suffix in ("", ".html")


def extract_links(driver: WebDriver) -> list[str]:
    """Collect normalized, crawlable links from all anchors on the current page."""
    links: list[str] = []
    for element in driver.find_elements(By.TAG_NAME, "a"):
        href = element.get_attribute("href")
        if href is None or not is_crawlable(href):
            continue
        links.append(normalize_url(href))
    return links


def crawl(driver: WebDriver, start_url: str) -> None:
    """Breadth-first crawl from start_url, saving each page's HTML to disk."""
    visited: set[str] = set()
    queue: deque[str] = deque([normalize_url(start_url)])

    while queue:
        url = queue.popleft()
        if url in visited:
            continue
        visited.add(url)

        driver.get(url)
        time.sleep(PAGE_LOAD_WAIT_SECONDS)

        file_path = url_to_file_path(url)
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(rewrite_absolute_links(driver.page_source), encoding="utf-8")
        print(f"[{len(visited)}] saved {url} -> {file_path}")

        for link in extract_links(driver):
            if link not in visited:
                queue.append(link)


def main() -> None:
    """Log in with the JWT cookie and crawl the whole wiki starting from START_URL."""
    options = Options()
    options.add_argument("--start-maximized")
    options.add_experimental_option(
        "prefs",
        {"profile.managed_default_content_settings.images": 2},
    )

    driver: WebDriver = webdriver.Chrome(options=options)
    try:
        driver.get(f"https://{ALLOWED_DOMAIN}")
        driver.add_cookie(
            {
                "name": COOKIE_NAME,
                "value": COOKIE_VALUE,
                "domain": ALLOWED_DOMAIN,
            }
        )
        driver.get(f"https://{ALLOWED_DOMAIN}")
        time.sleep(1)
        crawl(driver, START_URL)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
