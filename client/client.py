import customtkinter

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()  # create CTk window like you do with the Tk window
app.geometry("400x240")
app.title("Board Game Borrow")

def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
button = customtkinter.CTkButton(master=app, text="CTkButton", command=button_function)
button.place(relx=0.5, rely=0.5, anchor=customtkinter.CENTER)

app.mainloop()

myStudents = {}
while 1:
    print("1. Add")
    print("2. Remove")
    print("4. Display")
    print("5. Exit")
    option = input()

    if option == "1":

    # elif option == "2":

    # elif option == "3":

    # elif option == "4":

    # elif option == "5":
        exit()

    else:
        print("Enter a valid option")
