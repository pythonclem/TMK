import mysql.connector
from Functions import DBconnect, DBquery, queryaslist1item
mydb = DBconnect()

    #DBquery("CREATE TABLE teamsleagues (teamid VARCHAR(255), leagueid VARCHAR(255))")
    #DBquery("SELECT DISTINCT leagueid FROM teamsleagues")
    #DBquery("SELECT leaguename FROM leagues")


result = queryaslist1item("SELECT DISTINCT leagueid FROM teamsleagues")
result2 = queryaslist1item("SELECT DISTINCT leagueid FROM teams")
naleagues = []
for item in result2:
    if item not in result:
        naleagues.append(item)
print(naleagues)