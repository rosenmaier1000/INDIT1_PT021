# sonnig oder regnerisch kellerparty oder gartenparty

strWetter = input("Eingabe Wetter: ") # Eingabe Wetter
print("Eingabe bestätigt", strWetter)# Ausgabe des eingegebenen Wetter

string_1 = strWetter # Wettereingabe Kleinschreibung
kleinb = string_1.lower()
print("Kleinschreibung:", kleinb)

string_1 = strWetter # Wettereingabe Grossschreibung
grossb = string_1.upper()
print("Grossschreibung:", grossb)


if  strWetter.lower() == "sonnig": #vergleich
    print("Gartenparty")
elif strWetter.upper() == "REGNERISCH": #vergleich
    print("Kellerparty")
else: #vergleich
    print("keine Party")
    
    
