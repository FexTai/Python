#Initialissierung
ANTEIL_0_14weiter= 0.066
ANTEIL_15_49weiter= 0.029
ANTEIL_50_64weiter= 0.066

ANTEIL_0_14bleiben= 0.93
ANTEIL_15_49bleiben= 0.97
ANTEIL_50_64bleiben= 0.925
ANTEIL_65bleiben= 0.972

GEBURTEN_15_49= 0.2

schritt = 0

Kinder=float(input("Startanzahl der 0-14 jährigen:"))
Jugendliche=float(input("Startanzahl der 15-49 jährigen:"))
Erwachsene=float(input("Startanzahl der 50-64 jährigen:"))
Alte= float(input("Startanzahl der 65+ jährigen:"))
print("")

while schritt < 10:
    hilf = round(Jugendliche*GEBURTEN_15_49+Kinder*ANTEIL_0_14bleiben)
    Kinder = hilf
    Jugendliche= round(Kinder*ANTEIL_0_14weiter+Jugendliche*ANTEIL_15_49bleiben)
    Erwachsene = round(Jugendliche*ANTEIL_15_49weiter + Erwachsene*ANTEIL_50_64bleiben)
    Alte = round(Erwachsene*ANTEIL_50_64weiter+Alte*ANTEIL_65bleiben)
    schritt = schritt + 1
    ga= Kinder+Jugendliche+Erwachsene+Alte
    PK= round(Kinder/ga*100)
    PJ= round(Jugendliche/ga*100)
    PE= round(Erwachsene/ga*100)
    PA= round(Alte/ga*100)
    print("schritt",schritt)
    print(" ")
    print("Die berechneten Populationswerte sind:")
    print(" ")
    print("Anzahl der Kinder:",Kinder,"mio")
    print("Anzahl der Jugendlichen:",Jugendliche,"mio")
    print("Anzahl der Erwachsenen:",Erwachsene,"mio")
    print("Anzahl der Alten:", Alte,"mio")
    print(" ")
    print("Gesamtanzahl der Menschen:",ga,"mio")
    print(" ")
    print("Prozentualle Anteile:")
    print(" ")
    print("Prozentualle Anteile")
    print( "K:",PK,"%","J:",PJ,"%","E:",PE,"%","A",PA,"%")
    print(" ")
    print("Populationspyramide(in mio):")
    print(" ")
    print("K:","/","o"*Kinder,"/")
    print("J:","/","o"*Jugendliche,"/")
    print("E:","/","o"*Erwachsene,"/")
    print("A:","/","o"*Alte,"/")
    