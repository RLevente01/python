#Kérjünk addig be egész számokat amig azok párosak majd számolhjuk meg hány db
"""
szam2= 0
while True:
    szam = int(input("Adj meg egy számot"))
    if szam % 2 == 0:
        szam2 +=1
    else:
        break
print(f"Enny páros szám volt {szam2}")
"""

#kérjünk be 10 db egész számot értékeljük ki aszerint hogy páros vagy páratlan és osztható e 3-mal

for x in range(1,11,1):
    szam = int(input("Kérem a számot"))
    if szam % 2 == 0: 
        print("A szám páros")
    else: 
        print("A szám páratlan")
    if szam % 3 == 0:
        print("A szám osztható 3-mal")
    else:
        print("A szám nem osztható 3-mal")
print("Vége")







#Kérjünk be 5db gyügyölcs nevet és vizsgáljuk meg hogy az utolsó karaktere a vagy sem

for x in range(1,6,1,)
gy = input("Adj meg egy gyümi nevet: ")
if gyumi[-1] == "a":
    print(f"A {gy} az utolsó betűjeaz a ")
else: 
