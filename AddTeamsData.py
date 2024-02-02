# I want to add Leagues I dont have and their teams, but only if their teams arent in the DB already.
# I already have a list of leagues I dont have, so thats good.
# I need to get all the teams that participate in those leagues and check their teamid against teamids already in the DB
# If the teamid is not in DB, create a row for it. Otherwise move on to the next.

# Step 0: Create a list of all teamid in the DB
# Step 1: Create a loop that calls all the teams in a specific leagueid
# Step 2: Create a loop that goes over each teams in the API response
# Step 3: Check if teamid in the response is in the list of DB teamid. If yes, skip to next team
# Step 4: Create a tuple for each team not in DB
# Step 5: Create a list of tuples for insertion into the DB
# Step 6: Insert the list of tuples into the DB, move on the next league

import requests
import mysql.connector
import json
from tmkFunctions import DBconnect, DBquery, queryaslist1item, underscoredLeagues

mydb = DBconnect()
mycursor = mydb.cursor()

allteamids = queryaslist1item("SELECT DISTINCT id FROM teams")
leaguenames = underscoredLeagues("SELECT leaguename FROM leagues WHERE leagueid IN (4483, 4511, 4480, 4505, 4569, 4481, 5071, 4512, 4482, 4570, 4571, 4503, 4847, 4723, 4888, 4485, 4903, 4506, 4507, 4484, 4901, 4902, 4960, 5184, 4509, 4510, 5199, 4721, 5281, 4756, 4725, 4501, 4724, 5404, 5193, 5180, 4804, 4719, 4874, 4848, 5399, 5187, 4500, 4546, 4548, 4547, 5380, 5381, 4832, 4833, 4477, 5409, 5408)")

for league in leaguenames:
    response = requests.get(f"https://www.thesportsdb.com/api/v1/json/3/search_all_teams.php?l={league}")
    data = response.json()
    entries = len(data.get("teams", []))
    data_to_insert = []

    for x in range(entries):
        currentTeam = response.json()['teams'][x]
        teamid = currentTeam['idTeam']
        name = currentTeam['strTeam']
        if teamid in allteamids:
            print(f"{name} already in DB")
            continue
        altname = currentTeam['strAlternate']
        teamleague = currentTeam['strLeague']
        teamcountry = currentTeam['strCountry']
        teambadge = currentTeam['strTeamBadge']
        leagueid = currentTeam['idLeague']
        teamsport = currentTeam['strSport']
        data_to_insert.append((teamid, name, altname, teamleague,teamcountry, teambadge, leagueid, teamsport))

    print(data_to_insert)
    sql = "INSERT INTO teams (id, name, altname, league, country, badge, leagueid, sport) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.executemany(sql, data_to_insert)
    mydb.commit()
    print(f"Missing teams from {league} added to DB")