#hilfestellung berechnung durchmesser


import math

print(math.pi)

def eingabe ()
    correct = False
    
    while correct == False: # solange bis korrekte eingabe 
        input("Eingabe Radius: ")
        try:
        #in float umwandeln
        except ValueError:
            print("Keine gültige Zahl")
            
        correct = True
        
    return radius_eingegeben

 radius = eingabe()
 kreisumfang = 2*math.pi*radius