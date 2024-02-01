import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="160790",
  database = "TMK"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT DISTINCT country FROM teams")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)