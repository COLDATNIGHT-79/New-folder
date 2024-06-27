#guess the number
import tkinter as tk
from PIL import ImageTk
import random
import urllib.request as urlopen

class Game:
    def __init__(self, master):
        self.master = master
        self.master.title("Guess the Number")
        self.master.geometry('800x200')
        self.master.minsize(200, 400)

        self.image_url = "https://cdn.memes.com/up/77021971602474177/i/1604138690995.jpg"
        self.data = self.load_image(self.image_url)
        self.image = ImageTk.PhotoImage(data=self.data.read())

        self.attempts = 10
        self.solution = random.randint(1, 100)

        self.create_widgets()

    def create_widgets(self):
        self.label = tk.Label(self.master, text="Guess the number between 1 to 99", font=20)
        self.label.grid(row=0, column=0, padx=20, pady=10, sticky=tk.N)
        self.entry = tk.Entry(self.master, font= 20)
        self.entry.grid(row=1, column=0, padx=50, pady=50, ipadx=100, ipady=5, sticky=tk.N)

        self.frame = tk.Frame(self.master)
        self.frame.grid()

        self.check_button = tk.Button(self.frame, text="CHECK", font= 20, height=4, width=9, command=self.check_guess)
        self.check_button.grid(row=3, column=1, ipadx=15, ipady=5, sticky=tk.N)

        self.quit_button = tk.Button(self.frame, text="QUIT", font= 20, height=700, width=900, command=self.quit_game)
        self.quit_button.grid(row=4, column=1, ipadx=15, ipady=5, sticky=tk.E)

        self.attempts_left_var = tk.StringVar()
        self.attempts_left_var.set("You have 10 attempts Remaining! Good luck!!")
        self.attempts_left = tk.Label(self.master, textvariable=self.attempts_left_var, font= 50)
        self.attempts_left.grid()

    def load_image(self, url):
        try:
            return urlopen.urlopen(url)
        except Exception as e:
            print(f"Error loading image: {e}")
            return None
        
    def check_guess(self):
        try:
            guess = int(self.entry.get())
            if self.attempts > 0:
                self.attempts -= 1 
                if guess == self.solution:
                    self.attempts_left_var.set("YOU WON CONGRATS!!")
                    self.check_button.pack_forget()
                elif guess < self.solution:
                    self.attempts_left_var.set(f"INCORRECT YOU HAVE {self.attempts} REMAINING GO HIGHER")
                else:
                    self.attempts_left_var.set(f"INCORRECT YOU HAVE {self.attempts} REMAINING GO LOWER")
            else:
                self.attempts_left_var.set(f"GAME OVER! YOU LOST. THE NUMBER WAS {self.solution}")
                self.check_button.pack_forget()
        except ValueError:
            self.attempts_left_var.set("Invalid input! Please enter a number.")

    def quit_game(self):
        self.quit_button.config(image=self.image)

root = tk.Tk()
my_game = Game(root)
root.mainloop()    
