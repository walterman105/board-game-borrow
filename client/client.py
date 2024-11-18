import requests

serverUrl = "http://127.0.0.1:5000"

# def addBoardGame():
#     name = input("Enter the name of the board game: ")

#     # Check if game exists on the server
#     response = requests.get(f"{serverUrl}/check/{name}")
#     print(f"response: {response.json()}")

#     if response.json()['message'] == 'Game already exists':
#         print("Would you like to increase the number of copies of the game? (y/n)")
#         choice = input()
#         if choice == "y":
#             newGameCount = int(input("Enter the number of extra game copies you are adding: "))
#             #boardGames[name]["gamecount"] += newGameCount
#         return

#     # Collect game details
#     playercount = input("Enter the number of players: ")
#     gametime = input("Enter the time it takes to play the game: ")
#     age = input("Enter the minimum age to play the game: ")
#     gamecount = int(input("Enter the number of game copies: "))
#     new_game = {name: {"playercount": playercount, "gametime": gametime, "age": age, "gamecount": gamecount}}

#     # Send the game data to the server
#     response = requests.post(f"{serverUrl}/add", json=new_game)
#     if response.status_code == 201:
#         print("Game added successfully")
#     else:
#         print("Failed to add game")

# def removeBoardGame():
#     name = input("Enter the name of the board game: ")
#     response = requests.delete(f"{serverUrl}/delete/{name}")
#     print(f"response: {response.json()}")
    
#     if response.status_code == 200:
#         print(f"Game '{name}' deleted successfully.")
#     else:
#         print(f"Game '{name}' could not be deleted.")



# def displayBoardGames():
#     response = requests.get(f"{serverUrl}/boardgames")
#     print(f"Games: {response.json()}")

# def requestGame():
#     name = input("Enter the name of the board game: ")
#     if name in boardGames:
#         print(f"There are {boardGames[name]['gamecount']} copies of the game available")
#         request = input("Would you like to request the game? (y/n)")
#         if request == "y":
#             boardGames[name]["gamecount"] -= 1
#             print("Game has been requested")
#         else:
#             print("Game has not been requested")
#     else:
#         print("Game is not available")

# # Main loop
# while True:
#     print("1. Add")
#     print("2. Remove")
#     print("3. Display")
#     print("4. Request Game")
#     print("0. Exit")
#     option = input("Enter an option: ")

#     if option == "1":
#         addBoardGame()
#     elif option == "2":
#         removeBoardGame()
#     elif option == "3":
#         displayBoardGames()
#     elif option == "4":
#         requestGame()
#     elif option == "0":
#         exit()
#     else:
#         print("Enter a valid option")



def getGameList(): 
    response = requests.get(f"{serverUrl}/boardgames")
    print("GETTING DATA FR")
    return response.json

