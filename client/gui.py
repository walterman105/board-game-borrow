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

    # def __str__(self):
    #     return "SidebarFrame"

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


        # updated part
        app.switch_frame(app.gamelist)
        # In the case of classes defined in different namespaces, you can use this:
        # self.master.master.switch_frame(self.master.master.scroll_frame.master.master)
        # end of updated part

    def requestGame(self):
        print("Request Game")
        app.switch_frame(app.login_frame)

    def addGame(self):
        print("Add Game")

    # def __str__(self):
    #     return "FunctionsSidebarFrame"

class LoginSidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=120, corner_radius=8)

        text = customtkinter.CTkLabel(self, text="Please Login", font=customtkinter.CTkFont(size=15, weight="bold"))                        #Title
        text.grid(row=0, column=0, padx=10, pady=10)

    # def login(self):
    #     print("Login")

    # def createAccount(self):
    #     print("Create Account")


class GameList(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        # updated part
        self.grid(row=0, column=1, rowspan=3, padx=(20,0), pady=(40,70), sticky="nsew")
        # end of updated part

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)

        self.label = customtkinter.CTkLabel(self, text="Game List", fg_color="#1d1e1e", corner_radius=30, font=customtkinter.CTkFont(size=18, weight="bold"))
        self.label.grid(row=0, column=0, padx=20, pady=(20,5), sticky="nw")


        gameList = ScrollFrame(self)
        # gameList = customtkinter.CTkTextbox(self)
        gameList.grid(row=1, column=0, padx=20, pady=(5,20), rowspan=3, columnspan=2, sticky="nsew")
        # gameList.insert("end", "Game List\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n hello")

        # games = client.getGameList()
        # gameList.insert("end", games)

    # def __str__(self):
    #     return "GameList"

class ScrollFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master):
        super().__init__(master)

        self.grid(row=0, column=1, rowspan=3, padx=(20,0), pady=(40,70), sticky="nsew")

        label = customtkinter.CTkLabel(self, text="Scroll Frame")
        label.grid(row=0, column=0, padx=20, pady=20)

        gamenamelist = []
        
        buttonlist = []

        jsonstring = client.getGameList()
        gamedict = json.loads(jsonstring)

        for keys in gamedict:
            x = keys
            print(x)
            gamenamelist.append(x)
            

        for i in range(len(gamenamelist)):

            x = gamenamelist[i]

            

            button = customtkinter.CTkButton(self, text=f"{x}", command=lambda x=x: showinfo(x))
            button.grid(row=i+1, column=0, padx=20, pady=20)
            buttonlist.append(button)
            print(buttonlist)

        def showinfo(x):
            print(gamedict[x])
            
        


            



                
class GeneralFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        # updated part
        self.grid(row=0, column=1, rowspan=3, padx=(20,0), pady=(40,70), sticky="nsew")
        # end of updated part

        label = customtkinter.CTkLabel(self, text="Login Frame")
        label.grid(row=0, column=0, padx=20, pady=20)

    # def __str__(self):
    #     return "LoginFrame"

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Board Game Borrow")
        self.geometry(f"{1100}x{580}")

        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=0)
        self.grid_rowconfigure((0, 1, 2), weight=1)

        self.sidebar_frame = SidebarFrame(self)                                                                                             #Call Sidebar Frame
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")

        # self.top_frame = TopFrame(self)                                                                                                     #Call Top Frame
        # self.top_frame.grid(row=0, column=1, columnspan=3, sticky="new")

        self.top_button1 = customtkinter.CTkButton(self, text="Create Account", width=15, height=10, command=self.create_account)                                                              #Top Button
        self.top_button1.grid(row=0, column=3, padx=(20, 80), pady=10, sticky="ne")

        self.top_button2 = customtkinter.CTkButton(self, text="Sign In", width=15, height=10, command=self.login)                                                 #Top Button
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

        # updated part
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
        # end of updated part

        button3 = customtkinter.CTkButton(self, text="Remove Frame", command=lambda: self.remove_frame())
        button3.grid(row=2, column=2, padx=20, pady=20, sticky="es")

    # updated part (Stackoverflow help)
    def switch_frame(self, frame):
        """
        :param frame: instance of customtkinter.CTkFrame
        """
        if self.current_frame is frame:
            return
        if self.current_frame is not None:
            self.current_frame.grid_remove()
        # display an existing object
        self.current_frame = frame
        self.current_frame.grid() # grid options are remembered
        print(self.current_frame)

    def remove_frame(self):
        if self.current_frame is None:
            return
        self.current_frame.grid_remove()
        self.current_frame = None
        print(self.current_frame)
        print(self.winfo_children())
    # end of updated part

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

    def __str__(self):
        return "App"

if __name__ == "__main__":
    app = App()
    app.mainloop()