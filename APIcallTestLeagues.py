import requests
import json

countries = ['Spain']
leagues = []
for country in countries:
    response = requests.get(f"https://www.thesportsdb.com/api/v1/json/3/search_all_leagues.php?c={country}")
    data = response.json()
    entries = len(data.get("countries", []))
    for x in range(entries):
        leaguename = response.json()['countries'][x]['strLeague']
        leaguecountry = response.json()['countries'][x]['strCountry']
        leaguesport = response.json()['countries'][x]['strSport']
        leaguetuple = (leaguename, leaguecountry, leaguesport)
        leagues.append(leaguetuple)

print(leagues)




