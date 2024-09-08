import tkinter as tk

# Funktionen
def umrechnen():
    try:
        wert = float(ein.get())
        wert2 = float(Masse.get())
        erg = round(wert2 * wert, 6)
        zahl = float(wert)
        lbe["text"] = "Ergebnis in Kg: " + str(erg)
    except:
        lb1["text"] = "Bitte eine Zahl eingeben"

#Fenster
fen = tk.Tk()
fen.geometry("600x600")
fen.title("Massen Umwandeln")

# Label
lb1 = tk.Label(fen, text ="Gib die Masse an und wähle die Einheit:" )
lb1.pack()

# Entry
ein = tk.Entry(fen)
ein.pack()

#Button
b = tk.Button(fen, text= "Umrechnen", command= umrechnen)
b.pack()

lb2 = tk.Label(fen, text = "Deine ausgewählte Masse wird dann in kg Umgewandelt")
lb2.pack()

# Radiobuttons

Masse = tk.DoubleVar()

t = tk.Radiobutton(fen, text = "Tonnen", variable = Masse, value = 1000)
t.pack()

p = tk.Radiobutton(fen, text = "Pfund", variable = Masse, value = 0.45359237)
p.pack()

g = tk.Radiobutton(fen, text = "Gramm", variable = Masse, value = 0.001)
g.pack()

mg = tk.Radiobutton(fen, text = "Milligramm", variable = Masse, value = 0.000001)
mg.pack()

# Ergebnislabel
lbe = tk.Label(fen, text = "Ergebnis in Kg: ")
lbe.pack()

fen.mainloop()