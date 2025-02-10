from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

# Configure Selenium WebDriver options
options = Options()
options.add_argument("--headless")  # Run in headless mode (no GUI)
options.add_argument("--disable-blink-features=AutomationControlled")  # Prevent bot detection
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Set up the Chrome WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

# Dictionary to store scraped data
data = {'title': [], 'price': []}

# Open the Amazon page with iPhone search results
driver.get("https://www.amazon.in/s?k=iphone+price+on+amazon&adgrpid=60434440285&ext_vrnc=hi&hvadid=590652618376&hvdev=c&hvlocphy=9146291&hvnetw=g&hvqmt=e&hvrand=2144679526699416694&hvtargid=kwd-842477304627&hydadcr=24540_2265408&tag=googinhydr1-21&ref=pd_sl_3l345bybuu_e")

# Allow time for the page to fully load
time.sleep(5)

# Locate all product titles and prices
titles = driver.find_elements(By.CSS_SELECTOR, ".a-link-normal.s-line-clamp-2")
prices = driver.find_elements(By.CSS_SELECTOR, ".a-price-whole")

# Extract and store product titles
for title in titles:
    print(title.text)
    data["title"].append(title.text)

# Extract and store product prices
for price in prices:
    print(price.text)  # Print price
    data["price"].append(price.text)

# Convert the data dictionary to a Pandas DataFrame
df = pd.DataFrame.from_dict(data)

# Save the extracted data to a CSV file
df.to_csv("data1.csv", index=False)

# Close the WebDriver
driver.quit()
