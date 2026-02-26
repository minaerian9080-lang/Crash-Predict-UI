# fetch.py
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options

def fetch_and_display_html(url):
    browser = None  # Define the variable before try to avoid UnboundLocalError
    try:
        options = Options()
        options.headless = True  # Run browser in headless mode
        service = Service(executable_path="./geckodriver")  # Change path if geckodriver is elsewhere
        browser = webdriver.Firefox(service=service, options=options)
        
        browser.get(url)
        html_source = browser.page_source
        return html_source

    except Exception as e:
        print("Error fetching HTML:", e)
        return None

    finally:
        if browser is not None:
            browser.quit()


def main():
    url = "https://duelbets.com/crash"  # Change to the actual game URL
    html_source = fetch_and_display_html(url)
    
    if html_source:
        # Here you can parse the HTML if needed
        # Example: extracting game data from HTML
        game_data = {
            "payout": 0,
            "ticket": 0,
            "startedAt": "",
            "numberOfBets": 0,
            "serverSeed": "",
            "id": "",
            "endTime": ""
        }
        # Replace this example with actual data extraction logic
        return game_data
    else:
        return None
