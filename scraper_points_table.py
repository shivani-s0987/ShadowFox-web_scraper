import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_points_table():
    url = "https://www.cricbuzz.com/cricket-series/7607/indian-premier-league-2024/points-table"
    headers = {"User-Agent": "Mozilla/5.0"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, "html.parser")

        table = soup.find("table", class_="table cb-srs-pnts")
        if not table:
            print("⚠️ Points table not found.")
            return

        teams = []
        for row in table.find_all("tr")[1:]:
            cols = row.find_all("td")
            if len(cols) < 8:
                continue
            teams.append({
                "Team": cols[0].text.strip(),
                "Matches": cols[1].text.strip(),
                "Wins": cols[2].text.strip(),
                "Losses": cols[3].text.strip(),
                "Ties": cols[4].text.strip(),
                "No Result": cols[5].text.strip(),
                "Points": cols[6].text.strip(),
                "NRR": cols[7].text.strip(),
            })

        df = pd.DataFrame(teams)
        df.to_csv("data/ipl_points_table.csv", index=False)
        print("✅ IPL Points Table saved to data/ipl_points_table.csv")

    except Exception as e:
        print(f"❌ Failed to scrape points table: {e}")
