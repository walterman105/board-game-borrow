
import customtkinter

class LoginFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        button = customtkinter.CTkButton(self, text="Username", command=button_callback)
        button.grid(row=0, column=0, padx=20, pady=20)

        button = customtkinter.CTkButton(self, text="Password", command=button_callback)
        button.grid(row=1, column=0, padx=20, pady=20)

class FunctionFrame(customtkinter.CTkFrame):
    def __init__(self, master):
        super().__init__(master)

        button = customtkinter.CTkButton(self, text="Add", command=button_callback)
        button.grid(row=0, column=0, padx=20, pady=20)

        button = customtkinter.CTkButton(self, text="Remove", command=button_callback)
        button.grid(row=1, column=0, padx=20, pady=20)

        button = customtkinter.CTkButton(self, text="Display", command=button_callback)
        button.grid(row=2, column=0, padx=20, pady=20)

        button = customtkinter.CTkButton(self, text="Request", command=button_callback)
        button.grid(row=3, column=0, padx=20, pady=20)

class UserFunctions(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.title("Board Game Borrowing")
        self.geometry("400x600")
        self.grid_columnconfigure((1, 2), weight=1)
        self.grid_rowconfigure((1, 2), weight=1)

        self.current_frame = None
        self.switch_frame(LoginFrame)
        
        button = customtkinter.CTkButton(self, text="Switch to Function Frame", command=lambda: self.switch_frame(FunctionFrame))
        button.grid(row=2, column=1, padx=20, pady=20, sticky="sw")

        button = customtkinter.CTkButton(self, text="Exit", command=self.quit)
        button.grid(row=2, column=2, padx=20, pady=20, sticky="es")

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.grid(row=1, column=1, padx=10, pady=(10, 0), columnspan=2)

def button_callback():
    print("button pressed")

app = UserFunctions()
app.mainloop()