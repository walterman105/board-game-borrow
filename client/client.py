import requests

serverUrl = "http://127.0.0.1:5000"


def get_game_list(): 
    response = requests.get(f"{serverUrl}/boardgames")
    return response.text

def get_game_info(name): 
    response = requests.get(f"{serverUrl}/info/{name}")
    return response.text

