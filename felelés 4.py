#1 feladat: Kérjünk be 5 db egész számot és meg kell vizsgálni hogy az adott érték osztható e 3-mal vagy 5-el.
"""
for x in range(1,6,1):
    szam = int(input("Kérek egy számot"))
    if szam % 3 == 0 or szam % 5 == 0:
        print(f"{szam} osztható 3-mal vagy 5-el ")
        
    else:
         print(f"{szam} nem osztható egyik számmal se")
"""




#2 feladat: Kérünk be addig számokat AMIG OSZTHATÓ 3-MAL és megszámolni hogy hány db ilyen szám volt.
"""
szam = int(input("Kérek egy számot"))
db = 0
while szam % 3 == 0:
      szam = int(input("Kérek egy számot"))
      db = db + 1
print(f"{db}")
"""

#kérjünk be 10db egész számot és minden 2. értéket viszgáljunk meg hogy kisebb vagy nagyobb vagy egyenlő 50-el ha nagyobb akkor /2 ha egyenlő *2 ha kisebb /3
"""
for x in range(1,11,1):
    
     szam = int(input("Kérek egy számot"))
     if x % 2 == 0:
        if szam > 50:
            szam = szam / 2
        elif szam == 50:
            szam = szam * 2
        else:
            szam = szam / 3
        print(f"A kapott érték: {szam}")
"""


#KÉRJÜNK BE 5DB zöldség nevt és vizsgáljuk meg hogy hány  db olyan van aminek első p és utolsó karaktere a
"""
db = 0
for x in range(1,6,1):
    zoldseg = input("adj meg egy zöldséget")
    if zoldseg[0] == "p" and zoldseg[-1] == "a":
        db = db + 1
        
print(f"{db} volt, ami jo")
"""


#Bekérni egy egy keresztnevet addig amig nem azt kapjuk hogy Alex és 38számoljuk meg hogy a keresztnév hány betűből áll és hány üres kör voltnev = "Alex"
db = 0
while nev != "Alex" or kor != "38":
    nev = input("Adj meg egy nevet: ")
    kor = input("Adj meg egy kort: ")
    db = db + 1
print(f"{db} darab kör volt üres")
alex = len("Alex")
print(f"Alex {alex} darab betüből áll!")
