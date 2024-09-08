#Initialissierung
ANTEIL_JUNG_ERWACHSEN= 1
ANTEIL_ERWACHSEN_ALT= 1
GEBURTEN_ERWACHSENE= 1
GEBURTEN_ALT= 1

schritt = 0
jung=int(input("Startanzahl der jungen Mäuse:"))
erwachsen=int(input("Startanzahl der erwachsenen Mäuse:"))
alt=int(input("Startanzahl der alten Mäuse:"))
print("")

while schritt < 10:
    hilf = erwachsen*GEBURTEN_ERWACHSENE + alt*GEBURTEN_ALT
    alt = round(erwachsen * ANTEIL_ERWACHSEN_ALT)
    erwachsen = round(jung*ANTEIL_JUNG_ERWACHSEN)
    jung = hilf
    schritt = schritt + 1
    ga= jung+erwachsen+alt
    PJ= round(jung/ga*100)
    PE= round(erwachsen/ga*100)
    PA= round(alt/ga*100)
    print("schritt",schritt)
    print(" ")
    print("Die berechneten Populationswerte sind:")
    print("Anzahl junger Mäuse:",jung)
    print("Anzahl erwachsener Mäuse:",erwachsen)
    print("Anzahl alter Mäuse:",alt)
    print("Gesamtanzahl der Mäuse:",ga)
    print(" ")
    print("j:","/","o"*jung,"/")
    print("e:","/","o"*erwachsen,"/")
    print("a:","/","o"*alt,"/")
    print("Prozentualle Anteile")
    print( "J:",PJ,"%","E:",PE,"%","A:",PA,"%")  #auf lange dauer gleichen sich die anteile nicht aus
    
    



