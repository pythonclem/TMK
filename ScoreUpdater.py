# I have all the games of the season in the DB, including future ones
# But, because they're in the future, the scores are 'null' fields
# I want to have a daily(?) script that runs and updates the scores for the games that ended
                       
# Step 1: Find the leagues that have games on a specific day (today)
# Step 2: Loop API calls to the eventsonaday endpoint with the leagueids
# Step 3: Extract the eventids and the scores
# Step 4: Update the score in the DB based on the eventid

from tmkFunctions import DBconnect, DBquery
import json
import mysql.connector
from datetime import datetime, timedelta
import requests

mydb = DBconnect()
mycursor = mydb.cursor()

six_days_from_now = datetime.now() + timedelta(days=-1)
formatted_date = six_days_from_now.strftime('%Y-%m-%d')

leaguestoupdate = DBquery(f"SELECT DISTINCT leagueid FROM matches WHERE date = '{formatted_date}';")
leaguelist = []
for league in leaguestoupdate:
    leaguelist.append(league[0])

for league in leaguelist:
    response = requests.get(f"https://www.thesportsdb.com/api/v1/json/60130162/eventsday.php?d={formatted_date}&l={league}")
    data = response.json()
    entries = len(data.get("events", []))
    data_to_insert =[]

    for x in range(entries):
        currentTeam = response.json()['events'][x]
        eventid = currentTeam['idEvent']
        homescore = currentTeam['intHomeScore']
        awayscore = currentTeam['intAwayScore']
        print(eventid, homescore, awayscore)
        data_to_insert.append((homescore, awayscore, eventid))
    
    sql = "UPDATE matches SET homescore = %s, awayscore = %s WHERE matchid = %s"

    mycursor.executemany(sql, data_to_insert)
    mydb.commit()
    print(f"{entries} match(es) of {league} successfully updated")
                     
