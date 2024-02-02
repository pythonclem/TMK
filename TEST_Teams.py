import requests
import json
response = requests.get("https://www.thesportsdb.com/api/v1/json/3/all_leagues.php")
data = response.json()
entries = len(data.get("leagues", []))
leagues =[['English Premier League', 'English League Championship', 'Scottish Premier League', 'German Bundesliga', 'Italian Serie A', 'French Ligue 1', 'Spanish La Liga', 'Greek Superleague Greece', 'Dutch Eredivisie', 'Belgian First Division A', 'Turkish Super Lig', 'Danish Superliga', 'Portuguese Primeira Liga', 'American Major League Soccer', 'Swedish Allsvenskan', 'Mexican Primera League', 'Brazilian Serie A', 'Ukrainian Premier League', 'Russian Football Premier League', 'Australian A-League', 'Norwegian Eliteserien', 'Chinese Super League', '_No League', 'Formula 1', 'Formula E', 'BTCC', 'IndyCar Series', 'NHL', 'UK Elite Ice Hockey League', 'NBA', 'NBA G League', 'NFL', 'NASCAR Cup Series', 'Italian Serie B', 'Scottish Championship', 'English League 1', 'English League 2', 'Italian Serie C Girone C', 'German 2. Bundesliga', 'Spanish La Liga 2', 'French Ligue 2', 'Swedish Superettan', 'Brazilian Serie B', 'CFL', 'Argentinian Primera Division', 'MotoGP', 'Spanish Liga ACB', 'WRC', 'British GT Championship', 'WTCC']]
for x in range(entries):
    leaguename = response.json()['leagues'][x]['strLeague']
    leagues.append(leaguename)

print(leagues)