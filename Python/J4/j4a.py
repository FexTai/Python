guthaben = 2000
zinssatz = 1.03

while True:
    try:
        dauer = int(input("Wie lange soll die Verzinsung dauern? (In Jahren):\n"))
        for i in range(0, dauer):
            i += 1
            guthaben *= zinssatz
            if i == 1:
                print(f"Guthaben nach {i} Jahr: {round(guthaben, 2)} €")
            elif i > 1:
                print(f"Guthaben nach {i} Jahren: {round(guthaben, 2)} €")
        break
    except:
        print("Falsche Eingabe, versuche es erneut! \n")