import mysql.connector


# Connect to DB:
def DBconnect():
    global mydb
    mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="160790",
            database="TMK"
        )
    return mydb

# Run a query as argument:

def DBquery(query:str):
    mydb
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)
    return myresult

# Return all league IDs

def AllLeagueIDs():
    if mydb:
        leagueids = DBquery("SELECT DISTINCT leagueid FROM leagues")
        league_ids_list = [item[0] for item in leagueids]
    return league_ids_list

def underscoredLeagues(query):
    if mydb:
        rawleaguename = DBquery(query)
        first_values = [row[0] for row in rawleaguename]
        underscored = [item.replace(" ", "_") for item in first_values]
        return(underscored)

def queryaslist1item(query:str):
    ogquery = DBquery(query)
    listedquery = [row[0] for row in ogquery]
    return listedquery