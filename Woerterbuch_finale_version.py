#Rosenmaier
#Erweiterung der Woerterbuches
#1) Verwendung von Assoziativ-Arrays (Dictionary)
#2) Funktion zum Auslesen
#3) Funktion um neue Wörter hinzuzufügen



mein_woerterbuch = {"apfel":"apple", "birne":"pear", "kirsche":"cherry", "melone":"melon","pfirsich":"peach"}


print("Wählen Sie eine Funktion: ")
print("[A] = Wortabfrage")
print("[H] = Wort hinzu")

correct = False
    
while correct == False: #schleife
    eingabe = input("Funktionswahl: ") #eingabe     
    if eingabe == "A":
                                        
        wort=input("Wort in DE: ")
        wort = wort.lower() #alles in klein umwandeln
        if wort in mein_woerterbuch:
            print("Wort in EN: ",mein_woerterbuch[wort]) #übersetzung
        else:
            print('Nicht vorhanden')
    elif eingabe == "H":
        print("Bitte geben Sie die Wörter kleingeschrieben ein!!!!!",)   
        mein_woerterbuch[input('Wort in DE:')] = input('Wort in EN:') #wort hinzu
          
    else:
        print("Nicht bekannt")
