#Programm welches nach Eingabe des Radius den Kreisumfang berechnet.
#Unter Verwendung der Konstante pi
#Die Eingabe in einer eigenen Funktion erfolgen
# Sicherstellung: a) handelt es sich um eine Zahl
#                 b) ist diese auch positiv

import math

print("pi =" ,math.pi)

def eingabe():
    correct = False
    
    while correct == False:  # solange bis korrekte eingabe 
        radius = input("Eingabe Radius: ")
        try: 
            rad = float(radius)     #in float umwandeln
            if rad > 0:
                correct = True                
            else:
                print("Zahl ungültig!! (bitte eine positive Zahl eingeben) ") #mögliche ausgabe
        except ValueError:
            print("Eingabe ungültig!! (bitte eine positive Zahl eingeben)") #mögliche ausgabe
    return rad

def kreisumfang(radius):
    umfang = 2*radius*math.pi
    return umfang

kreisradius = eingabe() #eingabe
umfang = kreisumfang(kreisradius)
print("Berechneter Kreisumfang: ", umfang) #ausgabe