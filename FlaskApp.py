from flask import Flask, Response, request, jsonify
import mysql.connector
import json
from tmkFunctions import DBconnect, DBquery

mydb = DBconnect()
app = Flask(__name__)

@app.route("/teams", methods=["GET"])
def getteams():
    mycursor = mydb.cursor()
    mycursor.execute("SELECT id, name, altname, sport, leagueid FROM teams")
    teams = mycursor.fetchall()
    team_list = [{"id": team[0], "name": team[1], "altname": team[2], "sport": team[3], "leagueid": team[4]} for team in teams]
    mycursor.close()    
    response_data = json.dumps({"teams": team_list}, ensure_ascii=False)
    response = Response(response_data, content_type='application/json; charset=utf-8')
    return response

@app.route("/adduser", methods=["POST"])
def adduser():
    mycursor = mydb.cursor()
    data = request.get_json()
    username = data.get("userName")
    useremail = data.get("userEmail")
    sql = "INSERT INTO users (userfname, useremail) VALUES (%s, %s)"
    val = (username, useremail)
    mycursor.execute(sql, val)
    mydb.commit()
    userid = mycursor.lastrowid
    entries = len(data.get("selectedTeams", []))
    teamsToInsert = []
    for x in range(entries):
        teamid = data['selectedTeams'][x]
        teamsToInsert.append((userid, teamid))
    sql = "INSERT INTO userteams (userid, teamid) VALUES (%s, %s)"
    mycursor.executemany(sql, teamsToInsert)
    mydb.commit()
    return jsonify({"message": f"User and teams added successfully {userid}"}), 201

        

if __name__ == '__main__':
    with app.test_client() as client:
        json_data = {
            "userName": "John Doe",
            "userEmail": "john@example.com",
            "selectedTeams": [
                "w5er4gt6er8g",
                "weg5rwe4w6",
                "4rwe7gwerwf",
                "w5rt47w5e8w",
                "er5g774gR555T7d"
            ]
        }
        response = client.post('/adduser', json=json_data, content_type='application/json')
        print(response.get_json())


