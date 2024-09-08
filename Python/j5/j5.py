laenge_m = 0
umrechnung = 0

while True:
    try:
        laenge_m = float(input("\n Gib die Länge in m an (0 um das Programm zu beenden): \n"))
        if laenge_m == 0:
            break
        umrechnung = int(input("Umrechnungsart? \n 1: mm, 2: cm, 3: dm, 4: km, 5: Meilen, 6: Zoll, 7: Fuß \n"))
    except:
        print("Ungültige Eingabe!")
        continue

    if umrechnung == 1:
        print(laenge_m, " m = ", laenge_m * 1000, " mm\n")
        continue
    elif umrechnung == 2:
        print(laenge_m, " m = ", laenge_m * 100 ," cm\n")
    elif umrechnung == 3:
        print(laenge_m, " m = ", laenge_m * 10, " dm\n")
    elif umrechnung == 4:
        print(laenge_m, " m = ", laenge_m / 1000, " km\n")
    elif umrechnung == 5:
        print(laenge_m, " m = ", laenge_m / 1609, " mi\n")
    elif umrechnung == 6:
        print(laenge_m, " m = ", laenge_m / 39.37, " Zoll\n")
    elif umrechnung == 7:
        print(laenge_m, " m = ", laenge_m * 3.281, " ft\n")