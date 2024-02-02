# Each team has multiple leagues
# I need a junction table in my DB that has a row per league a team is in
# So if team A is in leagues 1 and 2, I need to create two rows. One is A , 1 and the other A , 2
# And so on for all the teams in all the leagues I have


# The search all teams endpoint has all the data I need per league
# I need to: create a list of league names I can run in the query (replace " " with "_")
# Create a DB table with teamid, idleague through idleague7
# Run that query through the endpoint
# For each team in the response, go over idleague through idleague7
# Create a row per idleague per team, so each team can have multiple rows created

#Step 1: Create the list of league names I can run through the API - DONE
#Step 2: Create a loop that calls the API for each league
#Step 3: Create a loop that runs over each teams in the API response
#Step 4: Create a loop that runs over idleague to idleague7 within the team and prepares rows for insertion
#Step 5: Insert the rows one team at a time

import requests
import mysql.connector
import json
from tmkFunctions import DBconnect, DBquery, underscoredLeagues

mydb = DBconnect()
mycursor = mydb.cursor()
listofleagues = underscoredLeagues("SELECT leaguename FROM leagues WHERE leagueid IN (4483, 4511)")

for league in listofleagues:
    data_to_insert = []
    response = requests.get(f"https://www.thesportsdb.com/api/v1/json/60130162/search_all_teams.php?l={league}")
    data = response.json()
    entries = len(data.get("teams", []))

    for team in range(entries):
            teambelongsto = []
            currentTeam = response.json()["teams"][team]
            teamid = currentTeam["idTeam"]
            league1 = currentTeam["idLeague"]
            league2 = currentTeam["idLeague2"]
            league3 = currentTeam["idLeague3"]
            league4 = currentTeam["idLeague4"]
            league5 = currentTeam["idLeague5"]
            league6 = currentTeam["idLeague6"]
            league7 = currentTeam["idLeague7"]

            for x in range(1, 8):
                league_key = f"league{x}"
                if locals()[league_key] == None:
                    continue
                teambelongsto.append(locals()[league_key])

            for item in teambelongsto:
                data_to_insert.append((teamid, item))
            
    print(data_to_insert)
    # sql = "INSERT INTO teamsleagues (teamid, leagueid) VALUES (%s, %s)"
    # mycursor.executemany(sql, data_to_insert)
    # mydb.commit()
    # print("Done Successfully")


