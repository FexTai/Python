#initialisierung

BreiteLW= float(input("Breite der längeren Wand:"))
BreiteKW= float(input("Breite der kürzeren Wand:"))
HöheW= float(input("Höhe des Zimmers:"))
BreiteFen= float(input("Breite des Fensterramens:"))
HöheFen= float(input("Höhe des Fensterramens:"))
BreiteTür= float(input("Breite des Türramens:"))
HöheTür= float(input("Höhe des Türramens:"))

Antwort= int(input("Sollen Tür und Fenster beachtet werden? 1 für ja und 2 für nein:"))

FlächeTF= HöheTür*BreiteTür+BreiteFen*HöheFen
FlächeMitTF= round(2*BreiteLW*HöheW + 2*BreiteKW*HöheW-FlächeTF) 
FlächeOhneTF= 2*BreiteLW*HöheW + 2*BreiteKW*HöheW


#Verarbeitung

if(Antwort==2):
    print(FlächeOhneTF,"m²")
elif(Antwort==1):
    print(FlächeMitTF,"m²")

Antwort2= int(input("Tapetenrechner ausführen? 1 für ja 2 für nein:"))
import sys

if(Antwort2==1):
    BreiteRolle= 0.56
    LängeRolle= 10.05 #float(input("Länge der Tapetenrolle:"))
    FlächeRolle= LängeRolle*BreiteRolle
    Antwort3= float(input("Tür und fenster beachten? 1 für ja 2 für nein:"))
elif(Antwort2==2):
    print(" ")
    print("Programm beendet")
    sys.exit()
    
if(Antwort3==1):
    BenötRoll= round(FlächeMitTF/FlächeRolle)
    print(BenötRoll,"Rollen")
else:
    if(Antwort3==2):
        BenötRoll2= round(FlächeOhneTF/FlächeRolle)
        print(BenötRoll2,"Rollen")
     



    

    
    
    



    
    

    

    




