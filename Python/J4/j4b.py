guthaben = 2000
zielguthaben = 2 * guthaben
zinssatz = 1.03
i = 0

while guthaben < zielguthaben:
    i += 1
    guthaben *= zinssatz
    if i == 1:
        print(f"Guthaben nach {i} Jahr: {round(guthaben, 2)} €")
    elif i > 1:
        print(f"Guthaben nach {i} Jahren: {round(guthaben, 2)} €")

print(f"\nnach {i} Jahren hat sich dein Guthaben verdoppelt!")
