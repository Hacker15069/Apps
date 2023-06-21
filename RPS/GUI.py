import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
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
        theme.add_radiobutton(label="Theme 2", command=print("Theme 2"), value=2)
        theme.add_radiobutton(label="Theme 3", command=print("Theme 3"), value=3)
        
        #menu --> History
        history = tk.Menu(menubar, tearoff=False)
        history.add_command(label="History", command=print("History"))

        #menu --> help
        help = tk.Menu(menubar, tearoff=False)
        help.add_command(label="About", command=print("About"))

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

#testing
if __name__ == "__main__":
    RPS()