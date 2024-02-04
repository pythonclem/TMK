import requests
import mysql.connector
import json
from tmkFunctions import DBconnect, DBquery, AllLeagueIDs

mydb = DBconnect()
mycursor = mydb.cursor()

leaguesToAdd = ['4483', '4511', '4480', '4505', '4569', '4481', '5071', '4512', '4482', '4570', '4571', '4503', '4847', '4723', '4888', '4485', '4903', '4506', '4507', '4484', '4901', '4902', '4960', '5184', '4509', '4510', '5199', '4721', '5281', '4756', '4725', '4501', '4724', '5404', '5193', '5180', '4804', '4719', '4874', '4848', '5399', '5187', '4500', '4546', '4548', '4547', '5380', '5381', '4832', '4833', '4477', '5409', '5408'] #AllLeagueIDs()
for league in leaguesToAdd:
    response = requests.get(f"https://www.thesportsdb.com/api/v1/json/60130162/lookupleague.php?id={league}")
    data = response.json()
    currentTeam = response.json()['leagues'][0]
    leagueid = currentTeam['idLeague']
    leaguename = currentTeam['strLeague']
    altname = currentTeam['strLeagueAlternate']
    leaguecountry = currentTeam['strCountry']
    seasonformat = currentTeam['strCurrentSeason']
    sport = currentTeam['strSport']
    if sport == 'Soccer':
        sport = 'Football'
    leaguebadge = currentTeam['strBadge']

    sql = "INSERT INTO leagues (leagueid, leaguename, altname, leaguecountry, seasonformat, sport, leaguebadge) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    val = (leagueid, leaguename, altname, leaguecountry, seasonformat, sport, leaguebadge)
    mycursor.execute(sql, val)
    mydb.commit()
    print(f"Inserted League {leaguename}")
