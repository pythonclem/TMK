import mysql.connector
from tmkFunctions import DBconnect, DBquery, queryaslist1item
mydb = DBconnect()

DBquery("CREATE TABLE userteams (userid VARCHAR(255), teamid VARCHAR(255))")
    #DBquery("SELECT DISTINCT leagueid FROM teamsleagues")
    #DBquery("SELECT leaguename FROM leagues")







