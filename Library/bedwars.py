import requests
import json

#API Key
headers = {"API-Key": "6e534e10-e088-4462-8b09-5b89e7d0398e"}

#Find the Amount of Coins
def coin(username):
    url = f"https://api.hypixel.net/player?name={username}"
    response = requests.get(url, headers=headers)
    text = response.text
    dictionary = json.loads(text)
    if dictionary["success"] == False:
        print(dictionary["cause"])
    else:
        player = dictionary["player"]
        stats = player["stats"]
        bedwars = stats["Bedwars"]
        coins = bedwars["coins"]
        return coins

    return False

#Number of Wins
def wins(username):
    url = f"https://api.hypixel.net/player?name={username}"
    response = requests.get(url, headers=headers)
    text = response.text
    dictionary = json.loads(text)
    if dictionary["success"] == False:
        print(dictionary["cause"])
    else:
        player = dictionary["player"]
        stats = player["stats"]
        bedwars = stats["Bedwars"]
        wins = bedwars["wins_bedwars"]
        return wins

    return False
    
#Number of Losses
def losses(username):
    url = f"https://api.hypixel.net/player?name={username}"
    response = requests.get(url, headers=headers)
    text = response.text
    dictionary = json.loads(text)
    if dictionary["success"] == False:
        print(dictionary["cause"])
    else:
        player = dictionary["player"]
        stats = player["stats"]
        bedwars = stats["Bedwars"]
        lose = bedwars["losses_bedwars"]
        return lose
    return False