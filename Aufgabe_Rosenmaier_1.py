Terme = input("Bitte geben Sie die Anzahl der gewünschten Terme ein: ") # Eingabe der gewünschten Durchläufe
intTerme = int(Terme)                                                   # Text in Zahl umwandeln
 
print(intTerme)

intd = 0
intn = 0
floatErg = 0


while intd < intTerme:
    floatLeibniz = (((-1)**intn) / (2*intn + 1)) # Leibniz = (((-1)**n) / (2*n + 1)) für ** kann man auch pow (a, b) verwenden a=2 b=3 =8
    intd += 1
    intn += 1
    floatErg += floatLeibniz

    
print("Der angenäherte Wert bei", Terme)
print("Durchlaeufen")
print("beträgt:", floatErg*4 )

    