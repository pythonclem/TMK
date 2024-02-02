import requests
import json
import mysql.connector
from tmkFunctions import DBconnect, DBquery, AllLeagueIDs

print(AllLeagueIDs())



# DBconnect()
# #cantgetnumofgames =[4391 : '2022', '4370':'2023', '4371' : '2023',]
# leagueids = ['4335', '4328', '4329', '4330', '4331', '4332', '4334', '4336', '4337', '4338', '4339', '4340', '4344', '4346', '4347', '4350', '4351', '4354', '4355', '4356', '4358', '4359']
# year = ['2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2023', '2023', '2022-2023', '2022', '2022-2023', '2022-2023', '2022-2023', '2023', '2022']
# gamesinseason =['38', '38', '46', '33', '34', '38', '38', '26', '34', '34', '36', '22', '34', '34', '30', '17', '38', '30', '30', '26', '30', '34']

# for league, season in zip(leagueids, year):
#     season_str = str(season)
#     try:
#         response = requests.get(f"https://www.thesportsdb.com/api/v1/json/3/lookuptable.php?l={league}&s={season_str}")
#     # Check if the request was successful
#         if response.status_code == 200:
#             data = response.json()
#             numgames = data['table'][0].get('intPlayed', 'N/A')
#             gamesinseason.append(numgames)
#             print(f"League {league}, Season {season_str}: {numgames} games")
#         else:
#             print(f"Error for League {league}, Season {season_str}. Status code: {response.status_code}")
#     except:
#         gamesinseason.append('FAIL')

# print(gamesinseason)

#use the season to find out how many games were played here: https://www.thesportsdb.com/api/v1/json/3/lookuptable.php?l=4351&s=2023

#use those two data points to call add matches mega loop

# league id pairs and years to check tomorrow
#  '4373', '4380', '4387', '4393', '4394', '4395', '4399', '4400', '4401', '4405', '4406', '4407', '4441', '4475', '4423', '4408', '4478', '5121', '4474', '4433', '4452', '4424'
#  '2023', '2022-2023', '2023', '2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022', '2023', '2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2022-2023', '2023']







#strings = [idEvent , strEvent, strLeague, idLeague, intRound, strHomeTeam, strAwayTeam, intHomeScore, intAwayScore, intRound, dateEvent, strTime, idHomeTeam, idAwayTeam, strVenue, strSquare]
