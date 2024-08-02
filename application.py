# print(get_table_data("https://www.scrapethissite.com/pages/forms/?page_num=1"))
from web_scraping import get_all_tables

if __name__ == "__main__":
    total_pages = 24  # Replace with the total number of pages you want to scrape
    base_url = "https://www.scrapethissite.com/pages/forms/"

    records = get_all_tables(total_pages, base_url)
    print(records, len(records))
