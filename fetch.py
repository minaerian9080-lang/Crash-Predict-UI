from selenium import webdriver
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
from bs4 import BeautifulSoup
import time

def fetch_and_display_html(url):
    browser = None  # initialize
    try:
        options = Options()
        options.add_argument("--headless")
        service = FirefoxService(GeckoDriverManager().install())
        browser = webdriver.Firefox(service=service, options=options)
        browser.get(url)
        time.sleep(3)  # wait for page to load
        
        html_source = browser.page_source
        soup = BeautifulSoup(html_source, "html.parser")
        
        # Dummy data (replace with real parsing)
        payout = 1000
        ticket = 250
        numberOfBets = 12
        return {"payout": payout, "ticket": ticket, "numberOfBets": numberOfBets}
    except Exception as e:
        print("Error fetching page:", e)
        return {"payout": "N/A", "ticket": "N/A", "numberOfBets": "N/A"}
    finally:
        if browser is not None:
            browser.quit()

def main():
    url = "https://duelbets.com"  # replace with real game URL
    data = fetch_and_display_html(url)
    return data
