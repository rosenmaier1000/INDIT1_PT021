#print("Hallo,Welt!") # Funktion besteht aus Funktionsnamen und in Klammer(Parameter1, Parameter..,....)

#print("Ergebnis: ",12)

#def summe(summand1, summand2):
#    zwischensumme = suammand1 + summand2
#   return zwichensumme #mit return gebe ich den wert zurück und kann das unterprogramm immer wieder aufrufen

#wert1 = summe(23,24)
#print("summe: ", wert1)

#wert2 = summe(1,-3)
#print("summe: ", wert2)

#wert3 = summe(wert1, wert2)
#print("summe: ", wert3)

#schreiben sie ein programm das sie nach der eingabe von 2 zahlen fragt
#und danach die summe, die differenz, das produkt und den qutienten der beiden zahlen
#ausgibt

#schreiben sie jeweils eine funktion zur berechnung von summe, diff, produkt und
#quotient

#verhindern sie dass mathematisch unmögliche berechnungen gestartet werden

#hilfestellunf aufgabe

def summe(Zahl1,Zahl2):
    summe = Zahl1 + Zahl2
    return summe

Zahl1 = input("Eingabe Zahl1: ") # Eingabe
Zahl2 = input("Eingabe Zahl2: ") # Eingabe
    
print("Summe = ",summe)