import tkinter
import tkinter.messagebox
import json
import customtkinter
import client

class SidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, corner_radius=0)
        self.grid_rowconfigure(4, weight=1)

        self.logo_label = customtkinter.CTkLabel(self, text="Board Game\nBorrow", font=customtkinter.CTkFont(size=20, weight="bold"))       #Title
        self.logo_label.grid(row=0, column=0, padx=30, pady=(20, 10))

        self.functionsframe = FunctionsSidebarFrame(self)                                                                                 #Call Functions Frame
        self.functionsframe.grid(row=1, column=0, padx=10, pady=10)
        self.functions_remove()                                                                                                           #Hide Functions Frame

        self.loginframe = LoginSidebarFrame(self)                                                                                         #Call Login Frame
        self.loginframe.grid(row=1, column=0, padx=10, pady=10)

        self.sidebar_button_1 = customtkinter.CTkButton(self, text="Login", command=self.login)
        self.sidebar_button_1.grid(row=2, column=0, padx=10, pady=10)

    def login_remove(self):
        self.loginframe.grid_remove()

    def login_show(self):
        self.loginframe.grid()

    def functions_remove(self):
        self.functionsframe.grid_remove()

    def functions_show(self):
        self.functionsframe.grid()

    def login(self):
        if self.loginframe.winfo_ismapped():
            self.login_remove()
            self.functions_show()
        elif not self.loginframe.winfo_ismapped():
            self.login_show()
            self.functions_remove()


class FunctionsSidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=120, corner_radius=8)
        self.grid_rowconfigure(4, weight=1)

        self.sidebar_button_1 = customtkinter.CTkButton(self, text="Veiw Game List", command=self.viewGames)                                #Side Button 1 (View Game List)
        self.sidebar_button_1.grid(row=1, column=0, padx=10, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self, text="Request Game", command=self.requestGame)                                #Side Button 2 (Request Game)
        self.sidebar_button_2.grid(row=2, column=0, padx=10, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self, text="Add Game", command=self.addGame)                                        #Side Button 3 (Add Game)
        self.sidebar_button_3.grid(row=3, column=0, padx=10, pady=10)

    def viewGames(self):
        app.switch_frame(app.gamelist)
                                                                                                                                            # In the case of classes defined in different namespaces, you can use this:
                                                                                                                                            # self.master.master.switch_frame(self.master.master.scroll_frame.master.master)
    
    def addGame(self):
        print("Add Game")
        app.open_toplevel()
        app.toplevel_window.focus() 

    def requestGame(self):
        print("Request Game")
        app.switch_frame(app.login_frame)

class AddGame(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Add Game")
        self.geometry(f"{400}x{400}")

        # self.grid_columnconfigure(0, weight=1)
        # self.grid_rowconfigure(0, weight=1)

        self.label = customtkinter.CTkLabel(self, text="Add Game", fg_color="#1d1e1e", corner_radius=30, font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=(20,5), sticky="nw")

        self.name_label = customtkinter.CTkLabel(self, text="Game Name", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.name_label.grid(row=1, column=0, padx=20, pady=5, sticky="nw")

        self.name_entry = customtkinter.CTkEntry(self, width=200)
        self.name_entry.grid(row=2, column=0, padx=20, pady=5, sticky="nw")
        

        self.age_label = customtkinter.CTkLabel(self, text="Age", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.age_label.grid(row=3, column=0, padx=20, pady=5, sticky="nw")

        self.age_entry = customtkinter.CTkEntry(self, width=200)
        self.age_entry.grid(row=4, column=0, padx=20, pady=5, sticky="nw")
        

        # self.minplayercount_label = customtkinter.CTkLabel(self, text="Min Player Count", font=customtkinter.CTkFont(size=15, weight="bold"))
        # self.minplayercount_label.grid(row=5, column=0, padx=20, pady=5, sticky="nw")
        

        # self.minplayercount_entry = customtkinter.CTkEntry(self, width=200)
        # self.minplayercount_entry.grid(row=6, column=0, padx=20, pady=5, sticky="nw")
        # minplayercount = self.minplayercount_entry.get()
        

        self.maxplayercount_label = customtkinter.CTkLabel(self, text="Max Player Count", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.maxplayercount_label.grid(row=7, column=0, padx=20, pady=5, sticky="nw")

        self.maxplayercount_entry = customtkinter.CTkEntry(self, width=200)
        self.maxplayercount_entry.grid(row=8, column=0, padx=20, pady=5, sticky="nw")
        

        self.gametime_label = customtkinter.CTkLabel(self, text="Game Time", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.gametime_label.grid(row=9, column=0, padx=20, pady=5, sticky="nw")

        self.gametime_entry = customtkinter.CTkEntry(self, width=200)
        self.gametime_entry.grid(row=10, column=0, padx=20, pady=5, sticky="nw")


        self.add_button = customtkinter.CTkButton(self, text="Add Game", command=lambda: self.game())
        self.add_button.grid(row=11, column=0, padx=20, pady=5, sticky="nw")

    def game(self): 
        name = self.name_entry.get()
        age = self.age_entry.get()
        maxplayercount = self.maxplayercount_entry.get()
        gametime = self.gametime_entry.get()
        
        gamedict = {
        "name": name,
        "age": age,
        "maxplayercount": maxplayercount,
        "gametime": gametime
        }
        print(gamedict)
        print("add game")
        client.add_game(name, maxplayercount, gametime, age)  
        print(name, age, maxplayercount, gametime)
        app.toplevel_window.after(500, self.destroy)
        


class LoginSidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=120, corner_radius=8)

        text = customtkinter.CTkLabel(self, text="Please Login", font=customtkinter.CTkFont(size=15, weight="bold"))                        #Title
        text.grid(row=0, column=0, padx=10, pady=10)

class GameList(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=1, rowspan=3, padx=(20,0), pady=(40,70), sticky="nsew")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.label = customtkinter.CTkLabel(self, text="Game List", fg_color="#1d1e1e", corner_radius=30, font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=(20,5), sticky="nw")

        gameList = ScrollFrame(self)
        gameList.grid(row=1, column=0, padx=20, pady=(5,20), rowspan=3, columnspan=2, sticky="nsew")

class ScrollFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

        self.columnconfigure(0, weight=1)

        if client.conneted_to_server == False:
            label = customtkinter.CTkLabel(self, text="Could not connect to server", font=customtkinter.CTkFont(size=15, weight="bold"))
            label.grid(row=0, column=0, padx=20, pady=20)
        else:
            gamenamelist = []
            jsonstring = client.get_game_list()
            gamenamelist = json.loads(jsonstring)
                
            for i in range(len(gamenamelist)):
                x = gamenamelist[i]

                button = customtkinter.CTkButton(self, width=200, text=f"{x}", command=lambda x=x: showinfo(x))
                button.grid(row=i+1, column=0, padx=5, pady=5)

            def showinfo(x):
                app.textbox.delete("1.0", "end")
                game_info = client.get_game_info(x)
                game_info_dict = json.loads(game_info)  # Assuming the response is a JSON string
                formatted_info = (
                    f"Game: {x}\n"
                    f"Age: {game_info_dict['age']}\n"
                    f"Player Count: {game_info_dict['playercount']}\n"
                    f"Game Time: {game_info_dict['gametime']}\n"
                    f"Number of available games: {game_info_dict['gamecount']}\n"
                )
                app.textbox.insert("end", formatted_info)
            

class GeneralFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        self.grid(row=0, column=1, rowspan=3, padx=(20,0), pady=(40,70), sticky="nsew")

        label = customtkinter.CTkLabel(self, text="Login Frame")
        label.grid(row=0, column=0, padx=20, pady=20)

class LoginTopLevel(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Login")
        self.geometry(f"{400}x{400}")

        self.label = customtkinter.CTkLabel(self, text="Login", fg_color="#1d1e1e", corner_radius=30, font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=(20,5), sticky="nw")

        self.username_label = customtkinter.CTkLabel(self, text="Username", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.username_label.grid(row=1, column=0, padx=20, pady=5, sticky="nw")

        self.username_entry = customtkinter.CTkEntry(self, width=200)
        self.username_entry.grid(row=2, column=0, padx=20, pady=5, sticky="nw")

        self.password_label = customtkinter.CTkLabel(self, text="Password", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.password_label.grid(row=3, column=0, padx=20, pady=5, sticky="nw")

        self.password_entry = customtkinter.CTkEntry(self, width=200)
        self.password_entry.grid(row=4, column=0, padx=20, pady=5, sticky="nw")

        self.login_button = customtkinter.CTkButton(self, text="Login", command=self.login)
        self.login_button.grid(row=5, column=0, padx=20, pady=5, sticky="nw")

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(username, password)
        app.toplevel_window.after(500, self.destroy)



class CreateAccountTopLevel(customtkinter.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)

        self.title("Create Account")
        self.geometry(f"{400}x{400}")

        self.label = customtkinter.CTkLabel(self, text="Create Account", fg_color="#1d1e1e", corner_radius=30, font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=(20,5), sticky="nw")

        self.username_label = customtkinter.CTkLabel(self, text="Username", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.username_label.grid(row=1, column=0, padx=20, pady=5, sticky="nw")

        self.username_entry = customtkinter.CTkEntry(self, width=200)
        self.username_entry.grid(row=2, column=0, padx=20, pady=5, sticky="nw")

        self.email_label = customtkinter.CTkLabel(self, text="Email", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.email_label.grid(row=3, column=0, padx=20, pady=5, sticky="nw")

        self.email_entry = customtkinter.CTkEntry(self, width=200)
        self.email_entry.grid(row=4, column=0, padx=20, pady=5, sticky="nw")

        self.password_label = customtkinter.CTkLabel(self, text="Password", font=customtkinter.CTkFont(size=15, weight="bold"))
        self.password_label.grid(row=5, column=0, padx=20, pady=5, sticky="nw")

        self.password_entry = customtkinter.CTkEntry(self, width=200)
        self.password_entry.grid(row=6, column=0, padx=20, pady=5, sticky="nw")

        self.login_button = customtkinter.CTkButton(self, text="Create", command=self.login)
        self.login_button.grid(row=7, column=0, padx=20, pady=5, sticky="nw")

    def login(self):
        username = self.username_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        print(username, email, password)
        app.toplevel_window.after(500, self.destroy)


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Board Game Borrow")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.toplevel_window = None

        self.sidebar_frame = SidebarFrame(self)                                                                                             #Call Sidebar Frame
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        self.top_button1 = customtkinter.CTkButton(self, text="Create Account", width=15, height=10, command=self.open_toplevel_create_account)                                                              #Top Button
        self.top_button1.grid(row=0, column=3, padx=(20, 80), pady=10, sticky="ne")

        self.top_button2 = customtkinter.CTkButton(self, text="Login", width=15, height=10, command=self.open_toplevel_login)                                                 #Top Button
        self.top_button2.grid(row=0, column=3, padx=20, pady=10, sticky="ne")

        self.checkbox = customtkinter.CTkCheckBox(self, text="Sidebar", command=self.sidebar)                                               #Call Checkbox
        self.checkbox.grid(row=2, column=1, padx=20, pady=20, sticky="ws")
        self.checkbox.select()

        self.textbox = customtkinter.CTkTextbox(self, width=100)                                                                            #Call Textbox
        self.textbox.grid(row=0, column=2, padx=20, pady=(40,70), sticky="nsew", rowspan=3, columnspan=2)
        self.textbox.insert("end", "Welcome to Board Game Borrow\n\n")

        self.exit = customtkinter.CTkButton(self, text="Exit", command=self.quit)                                                           #Exit Button
        self.exit.grid(row=2, column=3, padx=20, pady=20, sticky="es")

        self.current_frame = None

        client.check_connection()

        # create objects:
        # <__main__.GeneralFrame object .!generalframe>
        # <customtkinter.windows.widgets.ctk_frame.CTkFrame object .!ctkframe>
        
        self.login_frame = GeneralFrame(self)
        self.login_frame.grid_remove()

        self.gamelist = GameList(self)
        # print(self.scroll_frame) # .!ctkframe.!canvas.!scrollframe
        self.gamelist.grid_remove() # hide parent .!ctkframe
        # print(self.scroll_frame.master.master) # .!ctkframe

        button1 = customtkinter.CTkButton(self, text="Switch to Scroll Frame", command=lambda: self.switch_frame(self.gamelist))
        button1.grid(row=2, column=1, padx=20, pady=20, sticky="es")

        button2 = customtkinter.CTkButton(self, text="Switch to Login Frame", command=lambda: self.switch_frame(self.login_frame))
        button2.grid(row=2, column=1, padx=180, pady=20, sticky="es")

        button3 = customtkinter.CTkButton(self, text="Remove Frame", command=lambda: self.remove_frame())
        button3.grid(row=2, column=2, padx=20, pady=20, sticky="es")

    def switch_frame(self, frame):
        # param frame: instance of customtkinter.CTkFrame
        if self.current_frame is frame:
            return
        if self.current_frame is not None:
            self.current_frame.grid_remove()
        # display an existing object
        self.current_frame = frame
        self.current_frame.grid()
        print(self.current_frame)

    def remove_frame(self):
        if self.current_frame is None:
            return
        self.current_frame.grid_remove()
        self.current_frame = None
        print(self.current_frame)
        print(self.winfo_children())

    def sidebar_button_event(self):
        print("sidebar_button click")

    def sidebar(self):
        if self.sidebar_frame.winfo_ismapped():
            self.hide_sidebar()
        elif not self.sidebar_frame.winfo_ismapped():
            self.show_sidebar()
    
    def hide_sidebar(self):
        self.sidebar_frame.grid_remove()

    def show_sidebar(self):
        self.sidebar_frame.grid()

    def open_toplevel(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = AddGame(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def open_toplevel_login(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = LoginTopLevel(self)  # create window if its None or destroyed
        else:
            self.toplevel_window.focus()  # if window exists focus it

    def open_toplevel_create_account(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = CreateAccountTopLevel(self)
        else:
            self.toplevel_window.focus()

    def create_account(self):
        username = customtkinter.CTkInputDialog(text="Enter usernsme", title="Login")
        text1 = username.get_input()  # waits for input
        password = customtkinter.CTkInputDialog(text="Enter password", title="Login")
        text2 = password.get_input() # waits for input
        # Add code to add username(text1) and password(text2) to a new user in the database

    def login(self):
        username = customtkinter.CTkInputDialog(text="Enter usernsme", title="Login")
        text = username.get_input()  # waits for input
        password = customtkinter.CTkInputDialog(text="Enter password", title="Login")
        text2 = password.get_input() # waits for input
        if text == "admin" and text2 == "admin":
            self.top_button2.grid_remove()
            self.top_button2 = customtkinter.CTkButton(self, text="Sign Out", width=15, height=10)
            self.top_button2.grid(row=0, column=3, padx=20, pady=10, sticky="ne")
            self.sidebar_frame.login()


if __name__ == "__main__":
    app = App()
    app.mainloop()