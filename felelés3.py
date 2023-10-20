#kérjünk be 5 számot és vizsgáljuk meg hogy az értékek nagyobb kisebb vagy egyenlő 50-el
"""
for x in range(1,6,1):
    szam = int(input("ajd meg egy számot"))
    if szam > 50:
        print(f"{szam} nagyobb mint 50")
    if szam < 50:
        print(f"{szam} kisebb mint 50")
    if szam == 50:
        print(f"{szam} egyenlő 50-el")
print("vége")
"""
#Kérjünk be addig gyümi neveket amig az első betű a
"""
gy = input("Adj meg wgy gyümi nevet: ")
while gy[0] != "a":
    gy = input("Adj meg wgy gyümi nevet: ")
else:
    print("Vége")
"""

#Kérjünk be 5db auto márka nevet és minden márka nevéből irjuk ki az első és utolsó nevet
for x in range(1,6,1):
    marka = input("Adjon meg egy márka nevet")
    print(f"{marka[0]} {marka[-1]}")
print("vége")