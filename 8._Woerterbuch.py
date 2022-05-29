woerterbuch_deutsch = ["Apfel", "Birne", "Kirsche","Melone", "Marille", "Pfirsich"]
woerterbuch_english = ["apple", "pear", "cherry","melon", "apricot", "peach"]

#print(meine_liste[1])
#print(meine_liste[1][0]) #


#Eingabe

strdeutsch = input("Eingabe deutsches Wort: ") # Wort
print("Eingabe bestätigt", strdeutsch)

#Ermittlung Länge Wörterbuch (=Anzahl Einträge)
#len(woerterbuch_deutsch)


# while-Schleife über alle Elemente
#while woerterbuch_deutsch ([0]) < woerterbuch_deutsch ([7]):
if strdeutsch == "Apfel": #if-Abfrage zum Vergleich
        print(woerterbuch_english[0])
elif strdeutsch == "Birne":
        print(woerterbuch_english[1])
elif strdeutsch == "Kirsche":
        print(woerterbuch_english[2])
elif strdeutsch == "Melone":
        print(woerterbuch_english[3])
elif strdeutsch == "Marille":
        print(woerterbuch_english[4])
elif strdeutsch == "Pfirsich":
        print(woerterbuch_english[5])
else: #vergleich
        print("nicht im Woerterbuch enthalten")
    
    #woerterbuch_deutsch += [1]
    
    