szamok = [86,12,5,31,18,100,18]

for x in szamok:
    print(x)
    
print("__________________________________________________________________________________________________________________________")

print(f"Az első eleme a listának: {szamok[0]}")
elemek_szama = len(szamok)
print(f"A lista elemeinek száma: {elemek_szama}")
utolso_indexu = elemek_szama -1
print(f"Az utolso eleme: {szamok[utolso_indexu]}")

tizennyolc=szamok.count(18)
print(tizennyolc)


db= 0
for x in szamok:
    if x > 20:
        db = db+1
print(f"20-nál nagyobb számok darabja: {db}")


mini = min(szamok)
maxi = max(szamok)
osszeg = sum(szamok)
print(f"A legkisebb eleme: {mini}, a legnagyobb eleme:{maxi} és összegük:{osszeg}")

#Bekérünk 5 db zöldésget a felhasználótól és tároljuk listában és irjuk ki
zoldsegek=[]

for x in range(1,6,1):
    z=input("Kérem a zöldségeket")
    zoldsegek.append(z)
for x in zoldsegek:
    print(x)
    
#A paradicsom hanyadik a sorba
hely = zoldsegek.index("paradicsom")
print(f"A paradicsom a sorban a(z): {hely + 1}.")
    
    
    
    
    
    
    