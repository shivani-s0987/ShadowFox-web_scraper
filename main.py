from scraper import run_scraper
from scraper_points_table import scrape_points_table
# from ipl_analysis import analyze_data  # Keep it if you still want to run analysis

def main():
    print("📦 Running Web Scraper...")
    run_scraper()
    scrape_points_table()
    # analyze_data()  # optional — you can still keep your analysis

if __name__ == "__main__":
    main()
