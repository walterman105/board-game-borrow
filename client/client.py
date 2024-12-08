import requests
import gui
import globals as g

serverUrl = "http://127.0.0.1:5000"



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

def send_credentials(username, password):
    credentials = {"username": username, "password": password}
    response = requests.post(f"{serverUrl}/login", json=credentials)
    if response.status_code == 200:
        print("Login successful")
        g.user_logged_in = True
    else:
        print("Login failed")
        g.user_logged_in = False


def check_connection():
    #global conneted_to_server

    try:
        response = requests.get(serverUrl)
        if response.status_code == 200:
            response_json = response.json()
            if response_json.get("status") == "ok":
                g.conneted_to_server = True
            else:
                g.conneted_to_server = False
        else:
            g.conneted_to_server = False
    except requests.RequestException:
        g.conneted_to_server = False
