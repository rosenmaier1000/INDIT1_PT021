# if (Bedingung):
#         Anweisug1
# else :
#         Anweisug2

# die kleinere zahl soll von der größeren abgezogen werden
"""
strZahl1 = input("Zahl 1:")
floatZahl1 = float(strZahl1)

strZahl2 = input("Zahl 2:")
floatZahl2 = float(strZahl2)

if floatZahl1 < floatZahl2:
    floatDifferenz = floatZahl2 - floatZahl1

else:
    floatDifferenz = floatZahl1 - floatZahl2
    
print("Ergebnis = ",floatDifferenz)

"""


# die kleinere zahl soll von der größeren abgezogen werden mit negativer Zahlen ausgabe

strZahl1 = input("Zahl 1:")
floatZahl1 = float(strZahl1)

strZahl2 = input("Zahl 2:")
floatZahl2 = float(strZahl2)

if floatZahl1 < floatZahl2:
    floatDifferenz = floatZahl2 - floatZahl1
    floatNegDifferenz = floatZahl1 - floatZahl2
else:
    floatDifferenz = floatZahl1 - floatZahl2
    floatNegDifferenz = floatZahl2 - floatZahl1
    
print("Ergebnis = ",floatDifferenz)
print("Ergebnis negativ = ",floatNegDifferenz)
"""
# if (Bedingung):
#         Anweisug1
# elif :
#         Anweisug2
# elif :
#         Anweisug3
# elif :
#         ......
# else :
#         Anweisung 4 (default-Anweisung)

# die kleinere zahl soll von der größeren abgezogen werden

strZahl1 = input("Zahl 1:")
floatZahl1 = float(strZahl1)

strZahl2 = input("Zahl 2:")
floatZahl2 = float(strZahl2)

if floatZahl1 < floatZahl2:
    floatDifferenz = floatZahl2 - floatZahl1
    floatNegDifferenz = floatZahl1 - floatZahl2
    print("Ergebnis = ",floatDifferenz)
    print("Ergebnis negativ = ",floatNegDifferenz)
elif:
    floatDifferenz = floatZahl1 - floatZahl2
    floatNegDifferenz = floatZahl2 - floatZahl1
    print("Ergebnis = ",floatDifferenz)
    print("Ergebnis negativ = ",floatNegDifferenz)
    
else:
    print(Ergebnis = 0)
"""
