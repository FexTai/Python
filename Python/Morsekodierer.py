# Einweihung ins Programm
print("")
print("Willkommen beim Morse kodierer!")
print("Hinweis: Die einzelnen Buchstaben werden durch Leerzeichen und ganze Wörter durch einen Strich │ getrennt")
print("")

# Initialisierung
wort = input("Bitte gib eine Nachrit ein, die in Morse chiffriert werden soll: ")
lae = len(wort) - 1  # die eigentlcihe Anzahl der Strings, da len bei 0 beginnt
anz = len(wort)  # Anzahl 1 höher als der eigentliche Wert für den for x in range Befehl
print("")
print(wort)
wort = wort.lower()

# Morse Alphabet (Buchstaben)
a = "°-"
b = "-°°° "
c = "-°-° "
d = "-°° "
e = "° "
f = "°°-° "
g = "--° "
h = "°°°° "
i = "°° "
j = "°--- "
k = "-°- "
l = "°-°° "
m = "-- "
n = "-° "
o = "--- "
p = "°--° "
q = "--°- "
r = "°-° "
s = "°°° "
t = "- "
u = "°°- "
v = "°°°- "
w = "°-- "
x = "-°°- "
y = "-°-- "
z = "--°° "

ae = "°-°- "
oe = "---° "
ue = "°°-- "

# Morse Alphabet (Zahlen)
ei = "°---- "
zw = "°°--- "
dr = "°°°-- "
vr = "°°°°- "
fue = "°°°°° "
se = "-°°°° "
si = "--°°° "
ac = "---°° "
ne = "----° "
nu = " -----"

# Leerzeichen
leer = "│ "

# Übersetzung in den Morse Code
lae = -1

for x in range(0, anz):  # if Verkettung als Datenbank
    lae += 1
    if wort[lae] == "a":
        print(a, "", end="")
    elif wort[lae] == "b":
        print(b, "", end="")
    elif wort[lae] == "c":
        print(c, "", end="")
    elif wort[lae] == "d":
        print(d, "", end="")
    elif wort[lae] == "e":
        print(e, "", end="")
    elif wort[lae] == "f":
        print(f, "", end="")
    elif wort[lae] == "g":
        print(g, "", end="")
    elif wort[lae] == "h":
        print(h, "", end="")
    elif wort[lae] == "i":
        print(i, "", end="")
    elif wort[lae] == "j":
        print(j, "", end="")
    elif wort[lae] == "k":
        print(k, "", end="")
    elif wort[lae] == "l":
        print(l, "", end="")
    elif wort[lae] == "m":
        print(m, "", end="")
    elif wort[lae] == "n":
        print(n, "", end="")
    elif wort[lae] == "o":
        print(o, "", end="")
    elif wort[lae] == "p":
        print(p, "", end="")
    elif wort[lae] == "q":
        print(q, "", end="")
    elif wort[lae] == "r":
        print(r, "", end="")
    elif wort[lae] == "s":
        print(s, "", end="")
    elif wort[lae] == "t":
        print(t, "", end="")
    elif wort[lae] == "u":
        print(u, "", end="")
    elif wort[lae] == "v":
        print(v, "", end="")
    elif wort[lae] == "w":
        print(w, "", end="")
    elif wort[lae] == "x":
        print(x, "", end="")
    elif wort[lae] == "y":
        print(y, "", end="")
    elif wort[lae] == "z":
        print(z, "", end="")
    elif wort[lae] == "ä":
        print(ae, "", end="")
    elif wort[lae] == "ö":
        print(oe, "", end="")
    elif wort[lae] == "ü":
        print(ue, "", end="")
    elif wort[lae] == "1":
        print(ei, "", end="")
    elif wort[lae] == "2":
        print(zw, "", end="")
    elif wort[lae] == "3":
        print(dr, "", end="")
    elif wort[lae] == "4":
        print(vr, "", end="")
    elif wort[lae] == "5":
        print(fue, "", end="")
    elif wort[lae] == "6":
        print(se, "", end="")
    elif wort[lae] == "7":
        print(si, "", end="")
    elif wort[lae] == "8":
        print(ac, "", end="")
    elif wort[lae] == "9":
        print(ne, "", end="")
    elif wort[lae] == "0":
        print(nu, "", end="")
    elif wort[lae] == " ":
        print(leer, end="")

