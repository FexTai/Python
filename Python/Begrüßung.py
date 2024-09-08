# import GUI
import tkinter as tk

# Funktionen
def ausgeben():
    lb2["text"] = "Begrüßung: " + auswahl.get()
def ende():
    fenster.destroy()

# Erstellung von Fenstern
fenster=tk.Tk()
fenster.title("Begrüßung")
fenster.geometry("600x600")

# Label 1
lb1 = tk.Label(fenster, text="In welcher Sprache möchtest du begrüßt werden?", font=("Arial", 15, "bold"))
lb1.pack()

# Label 2
lb2 = tk.Label(fenster, text="Begrüßung:", font=("Arial", 15, "bold"))
lb2.place(x=220, y=265)


auswahl = tk.StringVar()
auswahl.set("Hello")

eng = tk.Radiobutton(fenster, text="Englisch", variable=auswahl, value="Hello", font=("Arial", 15, "bold"))
eng.pack()

frz = tk.Radiobutton(fenster, text="Französisch", variable=auswahl, value="bonjour", font=("Arial", 15, "bold"))
frz.pack()

deu = tk.Radiobutton(fenster, text="Deutsch", variable=auswahl, value="Hallo", font=("Arial", 15, "bold"))
deu.pack()

ch = tk.Radiobutton(fenster, text="Chinesisch", variable=auswahl, value="你好", font=("Arial", 15, "bold"))
ch.pack()

bn1 = tk.Button(fenster, text="Begrüßen lassen", command=ausgeben, font=("Arial", 15, "bold"))
bn1.pack()

bn2 = tk.Button(fenster, text="Ende", command=ende, font=("Arial", 15, "bold"))
bn2.pack()

# Schleife
fenster.mainloop()

