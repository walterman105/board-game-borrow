import requests

serverUrl = "http://127.0.0.1:5000"

server_connected = False


def check_server_connection():
    global server_connected

    try:
        page = requests.get(serverUrl)
        print(page.status_code)
        server_connected = True

    except (requests.exceptions.HTTPError, requests.exceptions.ConnectionError):
        print("Error - Cannot connect to Server!")
        server_connected = False


def get_game_list():
    response = requests.get(f"{serverUrl}/boardgames")
    return response.json()

