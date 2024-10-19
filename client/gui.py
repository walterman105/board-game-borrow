import tkinter
import tkinter.messagebox
import customtkinter

login = False

class TopFrame(customtkinter.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs, height=30, corner_radius=3)
        self.grid_columnconfigure((3), weight=2)

        self.topbar_button_1 = customtkinter.CTkButton(self, text="Create Account", width=15, height=10)                                    #Top Button 1 (Create Account)
        self.topbar_button_1.grid(row=0, column=3, sticky="e", pady=5)

        self.topbar_button_2 = customtkinter.CTkButton(self, text="Sign In", width=15, height=10, command=self.sign_in)   #Top Button 2 (Sign In)
        self.topbar_button_2.grid(row=0, column=4, sticky="e", padx=20, pady=5)

        self.topbar_button_3 = customtkinter.CTkButton(self, text="Sign Out", width=15, height=10) #Top Button 3 (Sign Out)
        self.topbar_button_3.grid(row=0, column=4, sticky="e", padx=20, pady=5)
        self.sign_out_remove()

    def sign_out_remove(self):
        self.topbar_button_3.grid_remove()

    def sign_out_show(self):
        self.topbar_button_3.grid()

    def sign_in_remove(self):
        self.topbar_button_2.grid_remove()

    def sign_in_show(self):
        self.topbar_button_2.grid()

    def sign_in(self):
        self.sign_in_remove()
        self.sign_out_show()
        SidebarFrame.login
        
    def __str__(self):
        return "TopFrame"

class SidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=140, corner_radius=0)

        self.logo_label = customtkinter.CTkLabel(self, text="Board Game\nBorrow", font=customtkinter.CTkFont(size=20, weight="bold"))       #Title
        self.logo_label.grid(row=0, column=0, padx=20, pady=(20, 10))

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


    # def switch_frame(self, frame_class):
    #     print(self)
    #     new_frame = frame_class(self)
    #     if self.current_frame is not None:
    #         self.current_frame.grid_remove()
    #     self.current_frame = new_frame
    #     self.current_frame.grid(row=1, column=0, columnspan=2)
    #     print(self.current_frame)
        
    # def set_login():
    #     global login 
    #     login = True
    #     print(login)
    #     if login == True:
    #         SidebarFrame.switch_frame(SidebarFrame, FunctionsSidebarFrame)
    #     else:
    #         SidebarFrame.switch_frame(SidebarFrame, LoginSidebarFrame)

    def __str__(self):
        return "SidebarFrame"


class FunctionsSidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=120, corner_radius=8)
        

        self.sidebar_button_1 = customtkinter.CTkButton(self, text="Veiw Game List", command=self.viewGames)                                #Side Button 1 (View Game List)
        self.sidebar_button_1.grid(row=1, column=0, padx=10, pady=10)

        self.sidebar_button_2 = customtkinter.CTkButton(self, text="Request Game", command=self.requestGame)                                #Side Button 2 (Request Game)
        self.sidebar_button_2.grid(row=2, column=0, padx=10, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self, text="Add Game", command=self.addGame)                                        #Side Button 3 (Add Game)
        self.sidebar_button_3.grid(row=3, column=0, padx=10, pady=10)

        self.sidebar_button_3 = customtkinter.CTkButton(self, text="Add Game", command=self.addGame)                                        #Side Button 3 (Add Game)
        self.sidebar_button_3.grid(row=4, column=0, padx=10, pady=10)

    def viewGames(self):
        print("View Games")

    def requestGame(self):
        print("Request Game")

    def addGame(self):
        print("Add Game")

    def __str__(self):
        return "FunctionsSidebarFrame"

class LoginSidebarFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master, width=120, corner_radius=8)

        text = customtkinter.CTkLabel(self, text="Please Login", font=customtkinter.CTkFont(size=15, weight="bold"))                        #Title
        text.grid(row=0, column=0, padx=10, pady=10)

    def login(self):
        print("Login")

    def createAccount(self):
        print("Create Account")

    def __str__(self):
        return "LoginSidebarFrame"

class ScrollFrame(customtkinter.CTkScrollableFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self._parent_frame.grid(row=0, column=0, columnspan=2, rowspan=3, padx=(200,0), pady=(50,70), sticky="nsew")

        self.label = customtkinter.CTkLabel(self)
        self.label.grid(row=0, column=0, padx=20)
        # Add Game List here

    def __str__(self):
        return "ScrollFrame"

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        
        label = customtkinter.CTkLabel(self, text="Login Frame")
        label.grid(row=0, column=0, padx=20, pady=20)

    def __str__(self):
        return "LoginFrame"

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

        self.top_frame = TopFrame(self)                                                                                                     #Call Top Frame
        self.top_frame.grid(row=0, column=1, columnspan=3, sticky="new")

        self.checkbox = customtkinter.CTkCheckBox(self, text="Sidebar", command=self.sidebar)                                               #Call Checkbox
        self.checkbox.grid(row=2, column=1, padx=20, pady=20, sticky="ws")

        self.textbox = customtkinter.CTkTextbox(self, width=100)                                                                            #Call Textbox
        self.textbox.grid(row=0, column=2, padx=20, pady=(40,65), sticky="nsew", rowspan=3, columnspan=2)
        self.textbox.insert("end", "Welcome to Board Game Borrow\n\n")

        self.exit = customtkinter.CTkButton(self, text="Exit", command=self.quit)                                                           #Exit Button
        self.exit.grid(row=2, column=3, padx=20, pady=20, sticky="es")

        self.current_frame = None

        button = customtkinter.CTkButton(self, text="Switch to Scroll Frame", command=lambda: self.switch_frame(ScrollFrame))
        button.grid(row=2, column=1, padx=20, pady=20, sticky="es")

        button = customtkinter.CTkButton(self, text="Switch to Login Frame", command=lambda: self.switch_frame(LoginFrame))
        button.grid(row=2, column=1, padx=180, pady=20, sticky="es")

        button = customtkinter.CTkButton(self, text="Remove Frame", command=lambda: self.remove_frame())
        button.grid(row=2, column=2, padx=20, pady=20, sticky="es")

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.grid_remove()
        self.current_frame = new_frame
        self.current_frame.grid(row=0, column=0, columnspan=2)
        print(self.current_frame)

    def remove_frame(self):
        self.current_frame.grid_remove()
        self.current_frame = None
        print(self.current_frame)

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

    def __str__(self):
        return "App"

if __name__ == "__main__":
    app = App()
    app.mainloop()