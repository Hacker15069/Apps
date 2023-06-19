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
        label = ttk.Label(frame, text="How many rounds do you wish to play", font=("Calibri",24,"bold"), background="lightblue")
        label.place(relx=0.5, rely=0.3, anchor="center")

        #this is the entry widget that allows the user to enter a value for the amount of 
        #rounds they want to play
        roundVar = tk.IntVar(value=1)
        rounds = ttk.Spinbox(frame, from_=1, to=30, textvariable=roundVar, font=("Calibri",24,"bold"), background="lightblue")
        rounds.place(relx=0.5, rely=0.5, relwidth=0.2, relheight=0.1, anchor="center")

        #this function below checks if the value if valid. If so it move on to the next page
        def exceeded():
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
        
        #frame for the window
        frame = ctk.CTkFrame(self, fg_color='#26b8dc')
        frame.pack(expand=True, fill="both")

        #label for the round
        ttk.Label(frame, text="nth Round", font=("Calibri", 24, "bold"), background="#26b8dc").place(x=300, y=10)
        
        #Score label, actual score, option choosen(this values are for the computer only)
        ttk.Label(frame, text="My Score:", font=("Calibri", 24, "bold"), background="#26b8dc").place(x=30, y=50)
        ttk.Label(frame, text="0", font=("Calibri", 48, "bold"), background="#26b8dc").place(x=30, y=100)
        ttk.Label(frame, text="Rock", font=("Calibri", 36, "bold"), background="#26b8dc").place(x=30, y=200)

        #Score label, actual score, option choosen(this values are for the player only)
        ttk.Label(frame, text="Your Score:", font=("Calibri", 24, "bold"), background="#26b8dc").place(x=590, y=50)
        ttk.Label(frame, text="0", font=("Calibri", 48, "bold"), background="#26b8dc").place(x=590, y=100)
        ttk.Label(frame, text="Rock", font=("Calibri", 36, "bold"), background="#26b8dc").place(x=590, y=200)

        #creating pictures for the rock, paper, scissors button respectively
        rock = Image.open("Pictures\Theme1\Rock.jpeg")
        paper = Image.open("Pictures\Theme1\Paper.jpeg")
        scissors = Image.open("Pictures\Theme1\Scissors.jpeg")
        imagetk1 = ctk.CTkImage(rock,size=(90,90))
        imagetk2 = ctk.CTkImage(paper,size=(90,90))
        imagetk3 = ctk.CTkImage(scissors,size=(90,90))

        #displaying the picture
        rock_pic = ctk.CTkLabel(frame, text="", image=imagetk1)
        paper_pic = ctk.CTkLabel(frame, text="", image=imagetk2)
        scissors_pic = ctk.CTkLabel(frame, text="", image=imagetk3)

        rock_pic.place(x=130, y=250, anchor='ne')
        paper_pic.place(x=330, y=250, anchor="ne")
        scissors_pic.place(x=530, y=250, anchor="ne")

        #button that chooses the player options
        ctk.CTkButton(frame, text="Rock").place(x=150, y=350, anchor='ne')
        ctk.CTkButton(frame, text="Paper").place(x=350, y=350,anchor="ne")
        ctk.CTkButton(frame, text="Scissors").place(x=550, y=350, anchor="ne")

        #this function displays the result as a frame in the window
        def result():
            result_frame = ctk.CTkFrame(self, width=270, height=200)
            
            #pictures that show a win, lose, and draw in the game
            draw = Image.open("Pictures\Draw.jpeg")
            win = Image.open("Pictures\Win.jpg")
            lose = Image.open("Pictures\Lose.jpeg")
            imagetk1 = ctk.CTkImage(draw,size=(270,200))
            imagetk2 = ctk.CTkImage(win,size=(270,200))
            imagetk3 = ctk.CTkImage(lose,size=(270,200))

            draw_pic = ctk.CTkLabel(result_frame, text="", image=imagetk1)
            win_pic = ctk.CTkLabel(result_frame, text="", image=imagetk2)
            lose_pic = ctk.CTkLabel(result_frame, text="", image=imagetk3)

            #dislaying the picture
            draw_pic.pack(expand=True, fill="both")

            result_frame.place(x=150, y=40, anchor="nw")
        result()

RPS()