import requests
import gui

serverUrl = "http://127.0.0.1:5000"

conneted_to_server = False

def get_game_list(): 
    response = requests.get(f"{serverUrl}/boardgames")
    return response.text

def get_game_info(name): 
    response = requests.get(f"{serverUrl}/info/{name}")
    return response.text

def add_game(name, maxplayer, gametime, age):
    new_game = {name: {"playercount": maxplayer, "gametime": gametime, "age": age, "gamecount": 9999}}

    response = requests.post(f"{serverUrl}/add", json=new_game)
    if response.status_code == 201:
        print("Game added successfully")
    else:
        print("Failed to add game")


def check_connection():
    global conneted_to_server

    try:
        response = requests.get(serverUrl)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get("status") == "ok":
                conneted_to_server = True
            else:
                conneted_to_server = False
        else:
            conneted_to_server = False
    except requests.RequestException:
        conneted_to_server = False
