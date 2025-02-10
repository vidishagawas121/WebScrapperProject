# Title and Price Scraper

This project is a **web scraper** that extracts **iPhone product titles and prices** from **Amazon India** using **Selenium and Python**. The extracted data is stored in a CSV file (`data1.csv`).

You can replace the site if you want with other websites

## Features
- **Extracts product titles and prices** from Amazon search results.
- Uses **headless Chrome browser** for automated scraping.
- **Stores the extracted data in a CSV file** for easy analysis.
- **Bypasses Amazon's basic bot detection** using user-agent modification.

## Requirements
Ensure you have the following dependencies installed:

```bash
pip install selenium webdriver-manager pandas
```

## Usage
1. **Run the script** using Python:

   ```bash
   python amazon_scraper.py
   ```

2. **Wait for the script to execute** (it will take a few seconds to load the page and extract the data).
3. **Check the output CSV file** (`data1.csv`) in the project directory.
4. Comments are added so that you can understand the code.
## How It Works
1. **Initializes Selenium WebDriver** with headless Chrome.
2. **Sends a request to Amazon's search results page** for iPhones.
3. **Finds product titles and prices** using CSS selectors.
4. **Saves the extracted data** into a CSV file.

## Notes
- Amazon employs **strict anti-scraping measures**. This script uses basic techniques to bypass detection, but frequent use may lead to CAPTCHA blocks.
- If Amazon blocks the script, consider using **proxies, rotating user-agents, or paid scraping APIs**.

## Disclaimer
This project is for **educational purposes only**. Scraping Amazon may violate its **terms of service**. Use at your own risk!

Screenshots:

![image](https://github.com/user-attachments/assets/124c4626-ce46-4f47-b458-9502848bf170)

![image](https://github.com/user-attachments/assets/2b5a4277-c69c-4962-8bfa-6548678ececf)




