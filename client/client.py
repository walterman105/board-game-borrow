# import customtkinter

# customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

# app = customtkinter.CTk()  # create CTk window like you do with the Tk window
# app.geometry("400x240")
# app.title("Board Game Borrow")

# def button_function():
    # print("button pressed")

# Use CTkButton instead of tkinter Button
# button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

# app.mainloop()



boardGames = {}

def addBoardGame():
    name = input("Enter the name of the board game: ")
    if name in boardGames:
        print("Would you like to increase the number of copies of the game? (y/n)")
        choice = input()
        if choice == "y":
            newgamecount = int(input("Enter the number of extra game copies you are adding: "))
            boardGames[name]["gamecount"] = gamecount + newgamecount
        return
    playercount = input("Enter the number of players: ")
    gametime = input("Enter the time it takes to play the game: ")
    age = input("Enter the minimum age to play the game: ")
    gamecount = int(input("Enter the number of game copies: "))
    boardGames[name] = {"playercount": playercount, "gametime": gametime, "age": age, "gamecount": gamecount}

def removeBoardGame():
    name = input("Enter the name of the board game: ")
    del boardGames[name]

def displayBoardGames():
    for game in boardGames:
        print(game)
        print("Player count: " + boardGames[game]["playercount"])
        print("Game time: " + boardGames[game]["gametime"])
        print("Age: " + boardGames[game]["age"])

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
