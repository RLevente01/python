hobby = {
    
    "László" : "foci",
    "Éva" : "röpi",
    "Ádám" : "sakk",
    "Linda" : "olvasás",
    "Aladár" : "gokart",
   
   
}

print(f"Aladár hobbija: ",hobby["Aladár"])
eva_hobby = hobby["Éva"]
print(f"Éva hobbija: {eva_hobby}")
print(hobby.get("Linda"))

print("Ádám" in hobby)

hobby["Ádám"] = "pc játékok"
print(hobby["Ádám"])

hobby["Dóra"] = "sminkelés"

print("-------------------------------------------------------------------")

#Kulcs-érték kiiratása:
for kulcs,ertek in hobby.items():
    print(kulcs, ":" , ertek)

print("-------------------------------------------------------------------")

#Csak az értékek kiiratása:
for x in hobby.values():
    print(x)

print("-------------------------------------------------------------------")

#Csak a kulcsok kiiratása:
for y in hobby:
    print(y)

print("-------------------------------------------------------------------")