#1.feladat: Bekérni egy valós és egész számot megvizsgálni és kiirni a tipusát
"""
szam = int(input("Kérek egy számot:"))
szam2 = float(input("Kérek egy számot: "))
print(f"A megadott szám: {szam}")
print(f"A megadott szám: {szam2}")

print(type(szam))
print(type(szam2))
"""

#2.feladat: bekérni két egész számot és a hányadosát ki irni
"""
num1 = int(input("Kérek egy számot:"))
num2 = int(input("Kérek egy számot:"))
hanyados = num1 / num2
print(f"A 2 szám hányadosa: {hanyados}")

egesz = int(hanyados)
szorzat = egesz * 3
print(f"Az érték: {szorzat}")
"""
#3.feladat: kérjünk be 2 db stringet. határozzuk meg hogy a 2 hobbi megegyezik e vagy sem
"""
hobby = input(" Mi a hobbyd?")
hobby2 = input(" Mi a hobbyd?")
if hobby == hobby2:
    print("A 2 hobby megegyezik")
else:
    print("nem egyezik meg a 2 hobby")
"""
#4.feladat:Bekérni eegy hőmérséklet értéket és ,megvizsgálni hogy a megadott érték nagyobb mint 20 akkor irhja ki hogy jó idő van ha 10 és 20 alatti akkor ideális ha 10 alatti hidegvn
"""
temp = float(input("mennyi a temp?"))
if temp >= 20:
    print("meleg van")
if temp >= 10 and temp < 20:
    print("Ideális az idő")
if temp < 10:
    print("hideg van")
"""
#5.feladat: bekérni egy egész számot vizsgáljuk meg hogy páros e vagy páratlan ha az akkor +10 és irjuk ki ha nem akkor +5 és irjuk ki
szam = int(input("Kérem a számot"))
if szam % 2 ==0:
    print(" a szám páros")
    szam = szam + 10
    print(f"Az uj érték: {szam}")
else:
    print(" a szám páratlan")
    szam = szam + 5
    print(f"Az uj érték: {szam}")
