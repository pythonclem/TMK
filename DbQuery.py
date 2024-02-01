import mysql.connector
from tmkFunctions import DBconnect, DBquery

mydb = DBconnect()
        
if mydb:
    DBquery("SELECT DISTINCT leagueid FROM teams")