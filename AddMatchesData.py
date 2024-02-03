# I want to add all the matches I don't have in the DB
# I want to add matches for all the leagues I have in the leagues table
# I want to add all the matches of this season and one previous season (for now)

# Step 1: Create a list of leagueids I want to add matches for
# Step 2: Create a list of seasons I want to add matches for - ATTENTION TO FORMAT
# Step 3: Create an API call that returns the matches I want
# Step 4: Go over the response and filter the data I want to keep
# Step 5: Insert the data I want to keep to the DB, one season at a time

# NOTE: 4569 crashes(really big, Friendlies), 4507 doesn't have 2023 (supercoppa, unclear), 4874 is iracing (delete it), 4848 another shit racing

import requests
import json
from tmkFunctions import DBconnect, AllLeagueIDs
import time

DBconnect()

mydb = DBconnect()
mycursor = mydb.cursor()
season1 = "2023-2024"
season2 = "2023"
leagueids = [4569]
progress = 0
for league in leagueids:
    progress += 1
    time.sleep(2)
    print(f"Starting {league}")
    try:
        response = requests.get(f"https://www.thesportsdb.com/api/v1/json/60130162/eventsseason.php?id={league}&s={season1}")
        if response.json() == {'events': None}:
            raise ValueError("API response is empty")   
         
    except ValueError:
            print(f"Except triggered for {league}")
            time.sleep(1)
            response = requests.get(f"https://www.thesportsdb.com/api/v1/json/60130162/eventsseason.php?id={league}&s={season2}")
    data = response.json()
    entries = len(data.get("events", []))
    data_to_insert =[]
    for x in range(entries):
        currentMatch = response.json()['events'][x]
        idEvent = currentMatch['idEvent']
        strEvent = currentMatch['strEvent']
        strLeague = currentMatch['strLeague']
        idLeague = currentMatch['idLeague']
        intRound = currentMatch['intRound']
        strHomeTeam = currentMatch['strHomeTeam']
        strAwayTeam = currentMatch['strAwayTeam']
        intHomeScore = currentMatch['intHomeScore']
        intAwayScore = currentMatch['intAwayScore']
        strSeason = currentMatch['strSeason']
        dateEvent = currentMatch['dateEvent']
        strTime = currentMatch['strTime']
        idHomeTeam = currentMatch['idHomeTeam']
        idAwayTeam = currentMatch['idAwayTeam']
        strVenue = currentMatch['strVenue']
        strSquare = currentMatch['strSquare']
        strVideo = currentMatch['strVideo']
        data_to_insert.append((idEvent, strEvent, strLeague, idLeague, intRound, strHomeTeam, strAwayTeam, intHomeScore, intAwayScore, strSeason, dateEvent, strTime, idHomeTeam, idAwayTeam, strVenue, strSquare, strVideo))
    print(f"{league} soon in DB")
    sql = "INSERT INTO matches (matchid, matchteams, league, leagueid, round, hometeam, awayteam, homescore, awayscore, season, date, time, hometeamid, awayteamid, venue, badge, video) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    mycursor.executemany(sql, data_to_insert)
    mydb.commit()
    print(f"Matches from {league} Successfully in DB")
    print(f"Completed {progress} of {len(leagueids)}")