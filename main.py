import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver

TARGET_URL: str = "https://wiki.affilka.net/en/home"
COOKIE_DOMAIN: str = "wiki.affilka.net"

COOKIE_NAME: str = "jwt"
COOKIE_VALUE: str = "eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6NiwiZW1haWwiOiJhZmZ3aWtpQHNvZnRzd2lzcy5jb20iLCJuYW1lIjoiQWZmIFdpa2kiLCJhdiI6bnVsbCwidHoiOiJFdXJvcGUvTW9zY293IiwibGMiOiJlbiIsImRmIjoiIiwiYXAiOiJsaWdodCIsInBlcm1pc3Npb25zIjpbInJlYWQ6cGFnZXMiLCJyZWFkOmFzc2V0cyJdLCJncm91cHMiOls1XSwiaWF0IjoxNzgzNjk2MDk4LCJleHAiOjE3ODM2OTc4OTgsImF1ZCI6InVybjp3aWtpLmpzIiwiaXNzIjoidXJuOndpa2kuanMifQ.pKGwEgPl2IAX-INwdPo0NpgSlVnOkev60louPccGq8wdyE_y6BKijYX4pWYEDFIgsTT0TTLU-9jpJ95PxlHfJm2pgjOv_dAYkxyPrjhWDCGI-akn4uCjFtl3MkMaao5HMv6dL1T8hLJh2saR_m031z8__a_-FIeAUFkaoe7QswyxirrX2zgjJ3UoedD0wNM78Y5mG4RYmX5ismssVPECShRSl0nHlnl7JKD-BQQxBdH8FZks2kN7DsEREY0AzSbGZxAErLHAgkj4B708uB5187IYSXXFgJ5-BIG-cNeiyZUR1N4rjvKy7vrK2HRk1V3w0qLe-MbHaNOyQ-avgcbGsQ"


def main() -> None:
    options = Options()

    driver: WebDriver = webdriver.Chrome(options=options)
    try:
        driver.get(f"https://{COOKIE_DOMAIN}")
        driver.add_cookie(
            {
                "name": COOKIE_NAME,
                "value": COOKIE_VALUE,
                "domain": COOKIE_DOMAIN,
            }
        )

        driver.get(TARGET_URL)
        time.sleep(10)
    finally:
        driver.quit()


if __name__ == "__main__":
    main()