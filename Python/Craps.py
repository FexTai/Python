# Importierung
from random import randint, seed
seed()

# Initialisierung
anz = int(input("Wie oft soll gewürfelt werden?:"))
w = 0
l = 0

# Schleife
for i in range(0, anz):
    w1 = randint(1, 6)
    w2 = randint(1, 6)
    az = w1 + w2
    print(az)
    if az == 2 or az == 3 or az == 12:
        print("Du hast verloren!")
        l += 1
    elif az == 7 or az == 11:
        print("Du hast gewonnen!")
        w += 1
    else:
        w1 = randint(1, 6)
        w2 = randint(1, 6)
        az1 = w1 + w2
if az1 == az:
    print("Du hast gewonnen!")
    w += 1
elif az1 == 7:
            print("Du hast verloren!")
            l += 1
else:
    gew = 0
    ver = 1
    while gew < 1 or ver < 2:
        anz +=1
        w1 = randint(1, 6)
        w2 = randint(1, 6)
        az1 = w1 + w2
        print(az1, az)
        if az1 == az:
            print("Du hast gewonnen!")
            gew += 1
        elif az1 == 7:
            print("Du hast verloren!")
            ver += 1
        
print("gewonnen:", w, "verloren:", l)
print(anz)
    
    