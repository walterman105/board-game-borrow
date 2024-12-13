import requests
import gloabls as g

def get_game_list(): 
    response = requests.get(f"{g.serverUrl}/boardgames")
    return response.text

def get_game_info(name): 
    response = requests.get(f"{g.serverUrl}/info/{name}")
    return response.text

def add_game(name, minplayer, maxplayer, gametime, age, owner):
    new_game = (name, minplayer, maxplayer, gametime, age, 1, owner)
    print(new_game)

    response = requests.post(f"{g.serverUrl}/add", json=new_game)
    if response.status_code == 201:
        print("Game added successfully")
    else:
        print("Failed to add game")

def add_user(email, password):
    new_user = (email, password)
    print(new_user)

    response = requests.post(f"{g.serverUrl}/adduser", json=new_user)
    if response.status_code == 201:
        print("User added successfully")
    else:
        print("Failed to add user")

def check_user(email, password):
    data = (email, password)
    print(data)

    response = requests.post(f"{g.serverUrl}/checkuser", json=data)
    if response.status_code == 201:
        print("Check User successfull")
        g.user_logged_in = True
    else:
        print("Check User failed")
        g.user_logged_in = False

def deletegame(email, name):
    data = (email, name)
    print(data)

    response = requests.post(f"{g.serverUrl}/delete", json=data)
    if response.status_code == 201:
        print("Game deleted successfully")
    # else:
    #     print("Failed to delete game")

def game_request(username, game):
    data = (username, game)
    print(data)

    response = requests.post(f"{g.serverUrl}/email_request", json=data)
    if response.status_code == 201:
        print("Request sent successfully")
    else:
        print("Failed to send request")

# def send_credentials(username, password):
#     credentials = {"username": username, "password": password}
#     response = requests.post(f"{g.serverUrl}/login", json=credentials)
#     if response.status_code == 200:
#         print("Login successful")
#         g.user_logged_in = True
#     else:
#         print("Login failed")
#         g.user_logged_in = False

def check_connection():

    try:
        response = requests.get(g.serverUrl)
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
    
