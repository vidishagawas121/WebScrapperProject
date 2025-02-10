import requests

def fetchAndSaveTofile(url, path):
    r = requests.get(url)
    with open(path, "w", encoding="utf-8") as f:  # Specify UTF-8 encoding
        f.write(r.text)

url = "https://timesofindia.indiatimes.com/city/delhi"
fetchAndSaveTofile(url, "data/times.html")
