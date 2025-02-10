from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
import pandas as pd

options = Options()
options.add_argument("--headless")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-extensions")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=options)

data = {'title': [], 'price': []}

driver.get("https://www.amazon.in/s?k=iphone+price+on+amazon&adgrpid=60434440285&ext_vrnc=hi&hvadid=590652618376&hvdev=c&hvlocphy=9146291&hvnetw=g&hvqmt=e&hvrand=2144679526699416694&hvtargid=kwd-842477304627&hydadcr=24540_2265408&tag=googinhydr1-21&ref=pd_sl_3l345bybuu_e")

time.sleep(5)

titles = driver.find_elements(By.CSS_SELECTOR, ".a-link-normal.s-line-clamp-2")
prices = driver.find_elements(By.CSS_SELECTOR, ".a-price-whole")

for title in titles:
    print(title.text)
    data["title"].append(title.text)

for price in prices:
    print(price.text)  # Fixed: Changed from prices.get_text to price.text
    data["price"].append(price.text)

df= pd.DataFrame.from_dict(data)
df.to_csv("data.csv", index=False)

driver.quit()
