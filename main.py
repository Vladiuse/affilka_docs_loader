import time
from collections import deque
from pathlib import Path, PurePosixPath
from urllib.parse import unquote, urlsplit, urlunsplit

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

START_URL: str = "https://wiki.affilka.net/en/home"
ALLOWED_DOMAIN: str = "wiki.affilka.net"
OUTPUT_DIR: Path = Path(__file__).parent / "site"
PAGE_LOAD_WAIT_SECONDS: float = 1.5
EXCLUDED_PATH_PREFIXES: tuple[str, ...] = ("/login", "/logout")

COOKIE_NAME: str = "jwt"
COOKIE_VALUE: str = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NiwiZW1haWwiOiJhZmZ3aWtpQHNvZnRzd2lzcy5jb20iLCJuYW1lIjoiQWZmIFdpa2kiLCJhdiI6bnVsbCwidHoiOiJFdXJvcGUvTW9zY293IiwibGMiOiJlbiIsImRmIjoiIiwiYXAiOiJsaWdodCIsInBlcm1pc3Npb25zIjpbInJlYWQ6cGFnZXMiLCJyZWFkOmFzc2V0cyJdLCJncm91cHMiOls1XSwiaWF0IjoxNzgzNjk2MDk4LCJleHAiOjE3ODM2OTc4OTgsImF1ZCI6InVybjp3aWtpLmpzIiwiaXNzIjoidXJuOndpa2kuanMifQ.pKGwEgPl2IAX-INwdPo0NpgSlVnOkev60louPccGq8wdyE_y6BKijYX4pWYEDFIgsTT0TTLU-9jpJ95PxlHfJm2pgjOv_dAYkxyPrjhWDCGI-akn4uCjFtl3MkMaao5HMv6dL1T8hLJh2saR_m031z8__a_-FIeAUFkaoe7QswyxirrX2zgjJ3UoedD0wNM78Y5mG4RYmX5ismssVPECShRSl0nHlnl7JKD-BQQxBdH8FZks2kN7DsEREY0AzSbGZxAErLHAgkj4B708uB5187IYSXXFgJ5-BIG-cNeiyZUR1N4rjvKy7vrK2HRk1V3w0qLe-MbHaNOyQ-avgcbGsQ"


def normalize_url(url: str) -> str:
    """Strip the fragment and trailing slash so equivalent URLs deduplicate."""
    parsed = urlsplit(url)
    path = parsed.path.rstrip("/") or "/"
    return urlunsplit((parsed.scheme, parsed.netloc, path, parsed.query, ""))


def url_to_file_path(url: str) -> Path:
    """Map a URL path to a local .html file, mirroring the path as folders."""
    path = urlsplit(url).path.strip("/")
    if not path:
        return OUTPUT_DIR / "index.html"
    segments = [unquote(segment) for segment in path.split("/")]
    return OUTPUT_DIR.joinpath(*segments[:-1], f"{segments[-1]}.html")


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
        file_path.write_text(driver.page_source, encoding="utf-8")
        print(f"[{len(visited)}] saved {url} -> {file_path}")

        for link in extract_links(driver):
            if link not in visited:
                queue.append(link)


def main() -> None:
    """Log in with the JWT cookie and crawl the whole wiki starting from START_URL."""
    driver: WebDriver = webdriver.Chrome()
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
