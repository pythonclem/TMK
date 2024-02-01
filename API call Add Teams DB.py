import requests
import mysql.connector
import json

mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="160790",
  database = "TMK"
)
mycursor = mydb.cursor()

leagues = ['MLB']
for league in leagues:
  response = requests.get(f"https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l={league}")
  data = response.json()
  entries = len(data.get("teams", []))

  for x in range(entries):
        currentTeam = response.json()['teams'][x]
        teamid = currentTeam['idTeam']
        name = currentTeam['strTeam']
        altname = currentTeam['strAlternate']
        teamleague = currentTeam['strLeague']
        teamcountry = currentTeam['strCountry']
        teambadge = currentTeam['strTeamBadge']
        leagueid = currentTeam['idLeague']
        teamsport = currentTeam['strSport']



        print(f"{name} successfully in DB")