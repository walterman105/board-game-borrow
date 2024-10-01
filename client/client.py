import requests

serverUrl = "http://10.129.42.22:5000"

boardGames = {}


def addBoardGame():
    name = input("Enter the name of the board game: ")

    response = requests.get(f"{serverUrl}/checkname/{name}")
    print(f"response: {response.json()}")

    if response.json()['message'] == 'Game already exists':
        print("Would you like to increase the number of copies of the game? (y/n)")
        choice = input()
        if choice == "y":
            newGameCount = int(input("Enter the number of extra game copies you are adding: "))
            boardGames[name]["gamecount"] + newGameCount
        return

    playercount = input("Enter the number of players: ")
    gametime = input("Enter the time it takes to play the game: ")
    age = input("Enter the minimum age to play the game: ")
    gamecount = int(input("Enter the number of game copies: "))
    boardGames[name] = {"playercount": playercount, "gametime": gametime, "age": age, "gamecount": gamecount}
    
    response = requests.post(f"{serverUrl}/addgame, json={boardGames[name]}")
    if response.status_code == 201:
        print("Game added successfully")
    else:
        print("Failed to add game")

def removeBoardGame():

    name = input("Enter the name of the board game: ")
    response = requests.get(f"{serverUrl}/delete/{name}")
    print(f"response: {response.json()}")
    
    
    del boardGames[name]

def displayBoardGames():
    response = requests.get(f"{serverUrl}/display")
    print(f"Games: {response.json()}")

    # for game in boardGames:
    #     print(game)
    #     print("Player count: " + boardGames[game]["playercount"])
    #     print("Game time: " + boardGames[game]["gametime"])
    #     print("Age: " + boardGames[game]["age"])

def requestGame():
    name = input("Enter the name of the board game: ")
    if name in boardGames:
        print("There are " + str(boardGames[name]["gamecount"]) + " copies of the game available")
        request = input("Would you like to request the game? (y/n)")
        if request == "y":
            boardGames[name]["gamecount"] = boardGames[name]["gamecount"] - 1
            print("Game has been requested")
        else:
            print("Game has not been requested")
    else:
        print("Game is not available")

while 1:
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("4. Request Game")
    print("0. Exit")
    option = input("Enter an option: ")

    if option == "1":
        addBoardGame()
    elif option == "2":
        removeBoardGame()
    elif option == "3":
        displayBoardGames()
    elif option == "4":
        requestGame()
    elif option == "0":
        exit()

    else:
        print("Enter a valid option")
