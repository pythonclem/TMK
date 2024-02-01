import requests
import json
response = requests.get("https://www.thesportsdb.com/api/v1/json/3/all_leagues.php")
data = response.json()
entries = len(data.get("leagues", []))
leagues =[]
for x in range(entries):
    leaguename = response.json()['leagues'][x]['strLeague']
    leagues.append(leaguename)

print(leagues)