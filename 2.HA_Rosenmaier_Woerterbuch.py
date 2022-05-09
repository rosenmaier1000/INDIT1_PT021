#Rosenmaier PTO21
#INDIT1
#Aufgabe 2.HA Woerterbuch DE in EN, Eingabe in deutsch, falls nicht vorhanden Meldung "nicht vorhanden"!!


woerterbuch = {"apfel":"apple","birne":"pear","kirsche":"cherry","melone":"melon","marille":"apricot","pfirsich":"peach"}   
#Erstellung des Woerterbuches

eingabe = input("Geben Sie das zu übersetzende Wort in deutsch ein: ")  #Eingabeaufforderung
eingabe = eingabe.lower()                                               #Umwandeln in Kleinbuchstaben


if eingabe not in woerterbuch:                                           #Check ob das Wort vorhanden....
    print("Wort ist nicht vorhanden!")                                   #Ausgabe des Textes wenn nicht vorhanden
    
else:
    print("Übersetzung Englisch:", woerterbuch[eingabe])                 #Ausgabe des Wort in Englisch wenn vorhanden
    
