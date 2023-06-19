import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tbstrap
from PIL import Image, ImageTk

class RPS(ctk.CTk):
    def __init__(self):
        super().__init__()

        #placing the window at the very center
        width = 600
        height = 400
        center = [
            int(self.winfo_screenwidth() / 2 - width / 2), 
            int(self.winfo_screenheight() / 2 - height / 2)
        ]
        
        self.geometry(f"{width}x{height}+{center[0]}+{center[1]}")
        self.title("Rock, Paper, Scissors")
        self.minsize(600, 400)
        self.resizable(False, False)
        self._set_appearance_mode("Light")

        self.menubar()
        self.startup()

        self.mainloop()

    def menubar(self):
        menubar = tk.Menu(self)

        #menu --> Theme
        theme = tk.Menu(menubar, tearoff=False)
        theme.add_radiobutton(label="Theme 1", command=print("Theme 1: Default"), value=1)
        theme.add_radiobutton(label="Theme 1", command=print("Theme 2"), value=2)
        theme.add_radiobutton(label="Theme 1", command=print("Theme 3"), value=3)
        
        #menu --> History
        history = tk.Menu(menubar, tearoff=False)
        history.add_command(label="History", command=print("History"))

        #menu --> help
        help = tk.Menu(menubar, tearoff=False)
        history.add_command(label="About", command=print("About"))

        menubar.add_cascade(label="Theme", menu=theme)
        menubar.add_cascade(label="History", menu=history)
        menubar.add_cascade(label="Help", menu=help)

        self.configure(menu=menubar)

    #startup image
    def startup(self):

        #creating an image
        image = Image.open("Pictures\Theme1\StartUp.jpeg")
        startup_image = ctk.CTkImage(image, size=(600, 400))

        #placing the picture through a label
        self.label = ctk.CTkLabel(self, text="", image=startup_image)
        self.label.pack(expand=True, fill="both")

        #displaying the next page(self.rounds)
        self.after(2000, self.rounds)
    
    def rounds(self):
        
        #clearing the previous page for the next one
        self.label.pack_forget()

        #a frame for the entire window
        frame = ctk.CTkFrame(self, fg_color="lightblue")
        frame.pack(expand=True, fill="both")

        #intro label. This is also used when the player enter a value that is outside the 
        # range of 1 - 30
        label = ctk.CTkLabel(frame, text="How many rounds do you wish to play", font=("Calibri",24,"bold"), text_color="green", bg_color="lightblue")
        label.place(relx=0.5, rely=0.3, anchor="center")

        #this is the entry widget that allows the user to enter a value for the amount of 
        #rounds they want to play
        roundVar = tk.IntVar(value=1)
        rounds = ttk.Scale(frame, from_=1, to=30, variable=roundVar, orient="horizontal")
        rounds.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.2, anchor="center")

        #this function below checks if the value if valid. If so it move on to the next page
        def exceeded(event):
            if roundVar.get() not in tuple(range(1,31)):
                label.configure(text="Value must be between 1 to 30")
            else:
                #clearing the window for the next page(self.main_game_page)
                frame.pack_forget()
                label.place_forget()
                rounds.place_forget()

                self.main_game_page()
            
        #next button
        next = ctk.CTkButton(frame, text="Next", command=exceeded)
        next.place(x=470, y=30, relwidth=0.2, relheight=0.1)
    
    def main_game_page(self):
        pass

RPS()