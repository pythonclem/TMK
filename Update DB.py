import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="admin",
  password="160790",
  database = "TMK"
)

mycursor = mydb.cursor()

update_query = "UPDATE teams SET sport = 'Football' WHERE leagueid IN (4394, 4395, 4399, 4400, 4401, 4406, 4356, 4358, 4359, 4354, 4355, 4339, 4340, 4344, 4346, 4347, 4350 ,4351, 4338, 4337, 4336, 4334, 4332, 4331, 4335, 4328, 4329, 4330);"
mycursor.execute(update_query)
print(f"Rows affected: {mycursor.rowcount}")

