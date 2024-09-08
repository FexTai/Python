while True:
    try:
        guthaben = float(input("Gib dein Startguthaben an: \n"))
        zielguthaben = 2 * guthaben
        zinssatz = float(input("Gib den Zinssatz in % an: \n")) / 100 + 1
        if zinssatz == 1:
            print("Zinssatz darf nicht 0% sein!")
            break
        i = 0
        while guthaben < zielguthaben:
            i += 1
            guthaben *= zinssatz
            if i == 1:
                print(f"Guthaben nach {i} Jahr: {round(guthaben, 2)} €")
            elif i > 1:
                print(f"Guthaben nach {i} Jahren: {round(guthaben, 2)} €")

        print(f"\nnach {i} Jahren hat sich dein Guthaben verdoppelt!")
        break
    except:
        print("Falsche Angabe, versuche es erneut!")
