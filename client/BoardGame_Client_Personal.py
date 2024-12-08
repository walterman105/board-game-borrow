import requests

serverUrl = "http://127.0.0.1:5000"

conneted_to_server = False

def get_game_list(): 
    response = requests.get(f"{serverUrl}/boardgames")
    return response.text

def get_game_info(name): 
    response = requests.get(f"{serverUrl}/info/{name}")
    return response.text

def add_game(name, minplayer, maxplayer, gametime, age, owner):
    new_game = (name, minplayer, maxplayer, gametime, age, 1, owner)
    print(new_game)

    response = requests.post(f"{serverUrl}/add", json=new_game)
    if response.status_code == 201:
        print("Game added successfully")
    else:
        print("Failed to add game")

def add_user(username, email, password):
    new_user = (username, email, password, 1)
    print(new_user)

    response = requests.post(f"{serverUrl}/adduser", json=new_user)
    if response.status_code == 201:
        print("User added successfully")
    else:
        print("Failed to add user")

def game_request(username, game):
    user = (username)
    print(user)

    response = requests.post(f"{serverUrl}/email/request", json=user)
    if response.status_code == 201:
        print("Request sent successfully")
    else:
        print("Failed to send request")


def check_user(username):
    response = requests.get(f"{serverUrl}/checkuser/{username}")
    return response.text


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
    
