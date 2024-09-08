import tkinter as tk
import time
from random import *

azeit = 0
r = 0
f = 0

def start():
    lb2["text"] = "was ist " + str(zahl1) + "+" + str(zahl2)
    lb2.pack()
    azeit = time.time()

zahl1 = randint(0, 100)
zahl2 = randint(0, 100)

fenster = tk.Tk()
fenster.geometry("600x600")
fenster.title("Game")
fenster.config(bg="#292929")

lb1 = tk.Label(fenster, text="Additionsturnier", font=("Arial", 30, "bold"), bg="#292929", fg="cyan")
lb1.pack()

start = tk.Button(fenster, text="start", font=("Arial", 20, "bold"), bg="#292929", fg="cyan", activebackground="#292929", activeforeground="white", command = start)
start.pack()

lb2= tk.Label(fenster, text="was ist")

ezeit = azeit - time.time()

fenster.mainloop()