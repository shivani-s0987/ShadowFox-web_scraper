import requests
from bs4 import BeautifulSoup
import pandas as pd

def run_scraper():
    url = "https://www.cricbuzz.com/cricket-news/latest-news"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        headlines = []
        for tag in soup.select(".cb-nws-hdln-ancr"):
            headlines.append(tag.get_text(strip=True))

        if headlines:
            df = pd.DataFrame({'IPL News Headlines': headlines})
            df.to_csv("data/scraped_data.csv", index=False)
            print("✅ IPL News saved to data/scraped_data.csv")
        else:
            print("⚠️ No headlines found.")

    except Exception as e:
        print(f"❌ Error during scraping: {e}")
