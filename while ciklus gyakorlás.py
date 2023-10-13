#Kérünk be 10db egész számot és vizsgáljuk meg ha páros a szám -10 és kiirni az uj értéket ha páratlan +10 és ezt is kiirni
"""
for x in range(1,11,1):
    szam = int(input("Adj meg egy számot: "))
    if szam  % 2 ==0 :
        szam2 = szam - 10
        print(f"{szam2}  a szám páros")
    else:
        szam3 = szam +10
        print (f"{szam3} a szám páratlan")
"""
#Kérjünk be addig számokat amig nem lesz páros és nem nagyobb mint 10
"""
szam = int(input("Kérem a számot: "))
while  szam % 2 != 0 or szam < 10:
    szam = int(input("Kérem a számot: "))
print("Siker")
"""

#Kérünk be addig számokat amig nagyobb mint 100:
"""
szam = int(input("Kérem a számot: "))
while szam > 100:
    szam = int(input("Kérem a számot: "))
print("Siker")
"""

#BEkérni 2 egész számot és megvizsgálni a 2 szám összgét és amennyi lett a annyiszor ki irni
"""
szam = int(input("Kérem a számot: "))
szam2 = int(input("Kérem a számot: "))
szam3= szam + szam2
for x in  range(1,szam3+1,1):
    print(f"{x}. :Siker")
"""
#Kérjünk be addig keresztnevet és életkort diig mig nem azt kapja meg hogy Béla 40:
nev = input("Add meg a neved: ")
eletkor = int(input("Add meg a korod: "))
while nev != "Béla" or eletkor != "40":
    nev = input("Add meg a neved")
    eletkor = int(input("Add meg a korod"))
print("Siker")
    

    