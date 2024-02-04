import requests
import json
import mysql.connector
from tmkFunctions import DBconnect, DBquery, AllLeagueIDs
from datetime import datetime, timedelta

mydb = DBconnect()
mycursor = mydb.cursor()

six_days_from_now = datetime.now() + timedelta(days=14)
formatted_date = six_days_from_now.strftime('%Y-%m-%d')

print(formatted_date)