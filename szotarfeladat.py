diak= {
    
    "Ádám" : 16,
    "Éva" : 25,
    "László" : 18,
    "Erik" : 20,
    "Vali": 45,
    
    
    }
db = 0
for x in diak.values():
    if x >=20:
        db += 1
print(f"{db} diák töltötte be a 20 életévét!")



#2.feladat: kik azok a diákok akik betöltötték a 20 évet
for x, y in diak.items():
    if y >=20:
        print(x)
    

#3.feladat: Milyen átlagos életkorral rendelkeznek
        eletkor = 0
for x in diak.values():
    eletkor += x
atlag = eletkor / len(diak.values())
print("Átlag kor: {:.1f}".format(atlag))
    
    