from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
import time

def fetch_and_display_html(url):
    browser = None  # Ensure browser is always defined
    try:
        options = Options()
        options.add_argument("--headless")
        browser = webdriver.Firefox(options=options)
        browser.get(url)
        time.sleep(2)
        html_source = browser.page_source
        return html_source
    except Exception as e:
        print(f"Error fetching HTML: {e}")
        return ""
    finally:
        if browser is not None:
            browser.quit()

def main():
    url = "https://example.com"  # Replace with your target URL
    html_source = fetch_and_display_html(url)
    
    # Dummy return structure similar to your original code
    return {
        "payout": 0,
        "ticket": 0,
        "numberOfBets": 0,
        "serverSeed": "",
        "id": 0,
        "startedAt": "",
        "endTime": ""
    }

if __name__ == "__main__":
    print(main())
