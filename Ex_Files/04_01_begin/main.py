import requests

response = requests.get(
    "http://api.worldbank.org/v2/countries/AUS/indicators/SP.POP.TOTL?per_page=5000&format=json")

last_twenty_years = response.json()[1][:20]

for year in last_twenty_years:
    display_width = year["value"] // 1_000_000
    print(f'{year["date"]}: {year["value"]}', "=" * display_width)
