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



def check_connection():
    global conneted_to_server

    try:
        response = requests.get(serverUrl)
        conneted_to_server = True
    except:
        conneted_to_server = False

    print(f"client.py {conneted_to_server}")


