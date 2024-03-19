import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def scrape_twitter_accounts(accounts, stock_symbol, interval_minutes):
    driver_path = 'chromedriver/chromedriver.exe'
    service = Service(driver_path)
    service.start()
    
    options = Options()
    options.add_argument("--headless")
    
    driver = webdriver.Remote(service.service_url, options=options)

    while True:
        counter = 0
        for account_url in accounts:
            driver.get(account_url)
            time.sleep(5)

            mentions = driver.find_elements(By.XPATH, f"//span/a[contains(text(), '{stock_symbol}')]")
            counter+= 1

        print(stock_symbol,"was mentioned",counter,"times in the last",interval_minutes,"minutes")
        time.sleep(interval_minutes * 60)

    driver.quit()

# List of Twitter accounts to scrape
twitter_accounts = [
    'https://twitter.com/Mr_Derivatives',
    'https://twitter.com/warrior_0719',
    'https://twitter.com/ChartingProdigy',
    'https://twitter.com/allstarcharts',
    'https://twitter.com/yuriymatso',
    'https://twitter.com/TriggerTrades',
    'https://twitter.com/AdamMancini4',
    'https://twitter.com/CordovaTrades',
    'https://twitter.com/Barchart',
    'https://twitter.com/RoyLMattox'
]

# Stock symbol to search for
stock_symbol = '$SPX'

# Time interval in minutes
scraping_interval_minutes = 5

scrape_twitter_accounts(twitter_accounts, stock_symbol, scraping_interval_minutes)