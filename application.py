from collections import defaultdict

from web_scraping import get_all_tables


def calculate_winner_looser(data):
    # Group teams by year
    teams_by_year = defaultdict(list)
    for team in data:
        teams_by_year[team["Year"]].append(team)

    # Find teams with max and min wins for each year
    results = {}
    for year, teams in teams_by_year.items():
        max_team = max(teams, key=lambda x: x["Wins"])
        min_team = min(teams, key=lambda x: x["Wins"])
        results[year] = {"max": max_team, "min": min_team}

    return results


if __name__ == "__main__":
    # Fetch the data from the website
    total_pages = 24
    base_url = "https://www.scrapethissite.com/pages/forms/"

    records = get_all_tables(total_pages, base_url)

    print(records, file=open("file_content.txt", "w"))

    results = calculate_winner_looser(records)
    print(results, file=open("output.txt", "w"))
