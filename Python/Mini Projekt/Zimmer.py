print("Willkommen!")
print(" ")
print("Das Programm wird dir helfen dein Zimmer zu renovieren")
print(" ")
print("aber vorerst musst du ein paar Angaben tätigen")
print(" ")

#initialisierung

BreiteLW= float(input("Breite der längeren Wand (in m):"))
BreiteKW= float(input("Breite der kürzeren Wand (in m):"))
HöheW= float(input("Höhe des Zimmers (in m):"))
BreiteFen= float(input("Breite des Fensterramens (in m):"))
HöheFen= float(input("Höhe des Fensterramens (in m):"))
BreiteTür= float(input("Breite des Türramens (in m):"))
HöheTür= float(input("Höhe des Türramens (in m):"))

print(" ")
print("Bisher wird nur die fläche der Wände ausgerechnet, aber später werden auch mehr Angaben möglich sein")
print(" ")

FlächeTF= HöheTür*BreiteTür+BreiteFen*HöheFen
FlächeMitTF= round(2*BreiteLW*HöheW + 2*BreiteKW*HöheW-FlächeTF) 
FlächeOhneTF= 2*BreiteLW*HöheW + 2*BreiteKW*HöheW


#Verarbeitung

#Testcode

Antwort=int(input("Sollen Tür und Fenster beachtet werden? 1 für ja und 2 für nein:"))
if(Antwort>2):
    while(Antwort>2):
        Antwort=int(input("Bitte 1 für ja und 2 für nein angeben:"))
        if(Antwort==2):
            print(" ")
            print("Die Fläche der Wände (Tür und Fenster wurden nicht beachtet) beträgt",FlächeOhneTF,"m²")
            print(" ")
        elif(Antwort==1):
            print(" ")
            print("Die Fläche der Wände (Tür und Fenster wurden beachtet) beträgt",FlächeMitTF,"m²")
            print(" ")
elif(Antwort==1):
    print("Die Fläche der Wände (Tür und Fenster wurden beachtet) beträgt",FlächeMitTF,"m²")
elif(Antwort==2):
    print("Die Fläche der Wände (Tür und Fenster wurden nicht beachtet) beträgt",FlächeOhneTF,"m²")

#Testcode Ende
    
#Testcode2

Antwort2= int(input("Tapetenrechner ausführen? 1 für ja 2 für nein:")) #Tapetenrechner Start
import sys

if(Antwort2==2):
    print(" ")
    print("Programm beendet")
    sys.exit()

while(Antwort2>2):
    Antwort2=int(input("Bitte 1 für ja und 2 für nein angeben:"))
    if(Antwort2==2):
        print(" ")
        print("Programm beendet")
        sys.exit()
    elif(Antwort2==1):
        print(" ")
        BreiteRolle= float(input("Breite der Rolle in m:")) #0.56
        LängeRolle= float(input("Länge der Rolle in m:")) #10.05
        FlächeRolle= LängeRolle*BreiteRolle
        Antwort3= float(input("Tür und Fenster beachten? 1 für ja 2 für nein:"))
        print(" ")
        while(Antwort3>2):
            Antwort3= float(input("1 für ja und 2 für nein:"))
            if(Antwort3==2):
                BenötRoll2= round(FlächeOhneTF/FlächeRolle)
                print(" ")
                print(BenötRoll2,"Rollen werden benötigt")
            elif(Antwort3==1):
                BenötRoll= round(FlächeMitTF/FlächeRolle)
                print(" ")
                print(BenötRoll,"Rollen werden benötigt")
if(Antwort2==1):
    print(" ")
    BreiteRolle= float(input("Breite der Rolle in m:")) #0.56
    LängeRolle= float(input("Länge der Rolle in m:")) #10.05
    FlächeRolle= LängeRolle*BreiteRolle
    Antwort3= float(input("Tür und Fenster beachten? 1 für ja 2 für nein:"))
    while(Antwort3>2):
        Antwort3= float(input("1 für ja und 2 für nein"))
        if(Antwort3==1):
            BenötRoll= round(FlächeMitTF/FlächeRolle)
            print(" ")
            print(BenötRoll,"Rollen werden benötigt")
        elif(Antwort3==2):
            BenötRoll2= round(FlächeOhneTF/FlächeRolle)
            print(" ")
            print(BenötRoll2,"Rollen werden benötigt")
    if(Antwort3==1):
        BenötRoll= round(FlächeMitTF/FlächeRolle)
        print(" ")
        print(BenötRoll,"Rollen werden benötigt")
    elif(Antwort3==2):
        BenötRoll2= round(FlächeOhneTF/FlächeRolle)
        print(" ")
        print(BenötRoll2,"Rollen werden benötigt")
print(" ")
print("Vorerst beendet")
        

            
            


    

    
    
    



    
    

    

    








