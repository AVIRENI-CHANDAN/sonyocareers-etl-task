from web_scraping import get_all_tables

if __name__ == "__main__":
    # Fetch the data from the website
    total_pages = 24
    base_url = "https://www.scrapethissite.com/pages/forms/"

    records = get_all_tables(total_pages, base_url)

    print(records, len(records))
