import tkinter as tk
from random import *

d = open("Highscore.txt", "w")
r = 0
f = 0
sec = -1
min = 0
erg = 0
runden = 0
score = 0
nick = ""

#Timer
def zeit():
    global sec, min
    sec += 1
    if sec == 60:
        sec = 0
        min += 1
    zae["text"] = str(min) + ":" + str(sec)
    zae.after(1000, zeit)


#Spielstart
def start():
    lb2["text"] = "was ist " + str(zahl1) + "+" + str(zahl2)
    lb2.pack()
    ent.pack()
    bt2.place(x=250, y=250)
    zeit()

def ende():
    fenster.destroy()

#lb3 verstecken
def dlb3():
    lb3.place_forget()
#lb4 verstecken
def dlb4():
    lb4.place_forget()

#Ergebnissüberprüfung
def check():
    global erg, zahl1, zahl2, f, r, runden, score, sec, min, d
    erg = ent.get()
    runden += 1
    print(zahl1+zahl2)
    try:
        erg = int(erg)
        if erg == zahl1 + zahl2:
            lb4.place(x=265, y=290)
            lb4.after(1000, dlb4)
            r += 1
        else:
            lb3.config(text="Falsch!")
            lb3.place(x=265, y=290)
            lb3.after(1000, dlb3)
            f += 1
    except:
        lb3.config(text="Eine Zahl eingeben!")
        lb3.place(x=200, y=290)
        lb3.after(1500, dlb3)
        f += 1
    if runden == 10:
        ent.destroy()
        start1.destroy()
        bt2.destroy()
        lb2.destroy()
        zae.destroy()
        lb6["text"] = "Du hast nur " + str(min) + "m " + "und " + str(sec) + "s " + " gebraucht!"
        lb6.pack()
        score = 1000 * r - 3 * sec - 180 * min
        if score < 0:
            score = 0
            lb5["text"] = "score: " + str(score)
            lb5.pack()
        elif score > 0:
            lb5["text"] = "score: " + str(score)
            lb5.pack()
        d.write("Dein Endergebnis:\n\n")
        d.write(str(r))
        d.write(" von 10 richtig gerechnet!\n\n")
        d.write(str(score))
        d.write(" Punkte erreicht!")
        d.close()
    wechsel()

#Aufgabenwechsel
def wechsel():
    global zahl1, zahl2, lb2
    zahl1 = randint(0, 100)
    zahl2 = randint(0, 100)
    lb2["text"] = "was ist " + str(zahl1) + "+" + str(zahl2)
    lb2.pack()

#Zufallszahlen
zahl1 = randint(0, 100)
zahl2 = randint(0, 100)

#Fensterkonfiguration
fenster = tk.Tk()
fenster.geometry("600x600")
fenster.title("Game")
fenster.config(bg="#292929")
fenster.resizable(False, False)


lb1 = tk.Label(fenster, text="Additionsspiel", font=("Arial", 30, "bold"), bg="#292929", fg="cyan")
lb1.pack()

lbname = tk.Label(fenster, text="gib deinen Namen ein: ", font=("arial", 15, "bold"), bg="#292929",  fg="cyan").pack()

namet = tk.Entry(fenster, width=13, bg="#292929", fg="cyan", font=("arial", 15, "bold")).pack()

start1 = tk.Button(fenster, text="start", font=("Arial", 20, "bold"), bg="#292929", fg="cyan", activebackground="#292929", activeforeground="white", command=start)
start1.pack()

ende = tk.Button(fenster, text="Beenden", font=("Arial", 15, "bold"), bg="#292929", fg="cyan", activebackground="#292929", activeforeground="white", command=ende)
ende.place(x=0, y=0)

lb2 = tk.Label(fenster, text="was ist", font=("arial", 20, "bold"), bg="#292929",  fg="cyan")

zae = tk.Label(fenster, text="", font=("arial", 15, "bold"), bg="#292929",  fg="cyan")
zae.pack()

ent = tk.Entry(fenster, width=5, bg="#292929", fg="cyan")
bt2 = tk.Button(fenster, text="überprüfen", bg="#292929", fg="cyan", activebackground="#292929", activeforeground="white", command=check)

lb3 = tk.Label(fenster, text="Falsch!", font=("Arial", 15, "bold"), bg="#292929", fg="cyan")
lb4 = tk.Label(fenster, text="Richtig!", font=("Arial", 15, "bold"), bg="#292929", fg="cyan")
lb5 = tk.Label(fenster, text="Score: ", font=("Arial", 15, "bold"), bg="#292929", fg="cyan")
lb6 = tk.Label(fenster, text="", font=("Arial", 15, "bold"), bg="#292929", fg="cyan")

fenster.mainloop()
