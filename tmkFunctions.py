import mysql.connector

def DBconnect():
    global mydb
    mydb = mysql.connector.connect(
            host="localhost",
            user="admin",
            password="160790",
            database="TMK"
        )
    return mydb

def DBquery(query:str):
    mydb
    mycursor = mydb.cursor()
    mycursor.execute(query)
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)

