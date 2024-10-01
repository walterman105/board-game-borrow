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
    playercount = input("Enter the number of players: ")
    gametime = input("Enter the time it takes to play the game: ")
    age = input("Enter the minimum age to play the game: ")
    boardGames[name] = {"playercount": playercount, "gametime": gametime, "age": age}

def removeBoardGame():
    name = input("Enter the name of the board game: ")
    del boardGames[name]

def displayBoardGames():
    for game in boardGames:
        print(game)
        print("Player count: " + boardGames[game]["playercount"])
        print("Game time: " + boardGames[game]["gametime"])
        print("Age: " + boardGames[game]["age"])

while 1:
    print("1. Add")
    print("2. Remove")
    print("3. Display")
    print("0. Exit")
    option = input()

    if option == "1":
        addBoardGame()
    elif option == "2":
        removeBoardGame()
    elif option == "3":
        displayBoardGames()
    elif option == "0":
        exit()

    else:
        print("Enter a valid option")
