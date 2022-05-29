# Rosenmaier Berechnung
# Berechnung der Summe, der Differenz, des Produktes und des Quotients zweier Zahlen - mit Ausagbe 
# Funktion zur Berechnung von Summe, Different, Produkt und Quotient.
# Verhindern Sie das unmögliche Berechnungen gestartet werden.

Eingabe1 = float(input("Eingabe 1. Zahl: ")) #Eingabe Zahl1
Eingabe2 = float(input("Eingabe 2. Zahl: ")) #Eingabe Zahl2

#Summe
def summe(Eingabe1, Eingabe2):     
    Zwischensumme = Eingabe1 + Eingabe2
    return (Zwischensumme)

#Differenz
def differenz(Eingabe1, Eingabe2):      
    Zwischendifferenz = Eingabe1 - Eingabe2
    return (Zwischendifferenz)

#Produkt
def produkt(Eingabe1, Eingabe2):      
    Zwischenprodukt = Eingabe1 * Eingabe2
    return (Zwischenprodukt)

#Quotient
def quotient(Eingabe1, Eingabe2):
    if Eingabe2 == 0:
        print("Division durch Null")
        return
    Zwischenquotient = Eingabe1 / Eingabe2
    return (Zwischenquotient)

#Ergebnisse
Wert1 = summe(Eingabe1, Eingabe2)
Wert2 = differenz(Eingabe1, Eingabe2)
Wert3 = produkt(Eingabe1, Eingabe2)
Wert4 = quotient(Eingabe1, Eingabe2)

#Ausgaben
print("Summe: ", Wert1)
print("Differenz: ", Wert2)
print("Produkt: ", Wert3)
print("Quotient: ", Wert4)