# Lab 2/1:
# Programm, das in 10°-Schritten zwischen 0 und 180 den jew Cosinus-Wert berechnet ausgibt!

inta=0
intb=181
intc=-10

while inta < intb:
    
    
    from math import * #from math import cos radians sollte funktionieren.
    Erg = cos(radians(inta))
    floatErg = float(Erg)
    inta += 10
    intc += 10
    
    
    
    print("Der Wert bei Winkel", intc)
    print("beträgt", floatErg)

