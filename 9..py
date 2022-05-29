woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche","Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry","melon", "apricot", "peach"]

#print(meine_liste[1])
#print(meine_liste[1][0]) #


#Eingabe

strdeutsch = input("Eingabe deutsches Wort: ") # Eingabe 
print("Eingabe bestätigt", strdeutsch)# Ausgabe 

#Ermittlung Länge Wörterbuch (=Anzahl Einträge)
max = len(woerterbuch_deutsch)
min = 0

# while-Schleife über alle Elemente
while min <= max:
    
    if strdeutsch == woerterbuch_deutsch[0]: #if-Abfrage zum Vergleich
        print(woerterbuch_english[0])
    else: #vergleich
        min += 1
  

#tupel unveränderbare liste
#aufgabe dictionary mit erweiterung, dieses programm dient nur als hilfestell.