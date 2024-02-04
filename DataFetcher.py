# I need to build a program that creates a list of users, and gets the relevant match data for them
# 
#
#
#
# Step 1: Query DB for all users
# Step 2: Query DB for each users preferred teams
# Step 3: Go fetch the matches in the coming 6 days for each team/league
# Step 4: Separate them into variables that can be used in an email

from tmkFunctions import DBconnect, DBquery
import json
import mysql.connector
from datetime import datetime, timedelta

mydb = DBconnect()
mycursor = mydb.cursor()
results = DBquery("SELECT userid, GROUP_CONCAT(teamid) AS team_ids FROM userteams GROUP BY userid")

for row in results:
    userid = row[0]
    team_ids = row[1].split(',') 

    team_ids_str = ', '.join(map(str, team_ids))
    print(team_ids_str)

    six_days_from_now = datetime.now() + timedelta(days=6)
    formatted_date = six_days_from_now.strftime('%Y-%m-%d')

    matches = DBquery(f"SELECT matchteams, date, time, league, venue FROM matches WHERE (hometeamid IN ({team_ids_str}) OR awayteamid IN ({team_ids_str})) AND date BETWEEN CURRENT_DATE AND '{formatted_date}';")

    for x in range(len(matches)):
        print(f"{matches[x][0]} , {matches[x][1]}, {matches[x][2]}, {matches[x][3]}, {matches[x][4]}")