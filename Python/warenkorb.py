import sys

try:
    d = open("Warenkorb.txt", "w")
except:
    print("Fehler beim Zugriff")
    sys.exit()

# Begrüßung
print("Willkommen zu deinem persönlichem Warenkorb!")
print("Hier kannst du alles reinlegen, was du möchtest.")
print("mit dem Stichwort:  ende  kannst du deinen Einkauf beenden.")
print("Am Ende kannst du Gegenstände aus deinem Warenkorb rausnehmen.")
print("")

# Warenkorb
warenkorb = []
x = input("was möchtest du in deinen warenkorb legen?:").lower()
warenkorb.append(x)

while x != "ende":
    x = input("Was noch?:").lower()
    warenkorb.append(x)
warenkorb.remove("ende")

x = input("möchtest du etwas aus deinem Warenkorb rausnehmen?:").lower()
if x == "ja":
    x = input("was möchtest du rausnehmen?:").lower()
    warenkorb.remove(x)

    while x != "nein":
        warenkorb.append("nein")
        x = input("noch etwas?:").lower()
        warenkorb.remove(x)

elif x == "nein":
    print("Dein Einkauf wird beendet")
else:
    print()

print("Dein Warenkorb wurde in einer Textdatei abgespeichert.")

f = len(warenkorb)
t = -1
d.write("Dein Warenkorb:\n\n")

for i in range(0, f):
    t += 1
    d.write(str(warenkorb[t]) + "\n")

d.close()
