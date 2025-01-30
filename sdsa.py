#1.1 Tervitus
print("Tere, maailm!")

#1.2Aasta liblikas
aasta = 2020 
liblikas = "teelehe-mosaiikliblikas"
lause_keskosa = " aasta liblikas on "
lause = str(aasta) + lause_keskosa + liblikas
print(lause)

#1.3 Pilved
korgus = float(input("Sisesta pilvede kõrgus:"))
if korgus > 6:
    print("Ülemised")
elif korgus >= 2 and korgus <= 5:
    print("Keskmine")
else:
    print("alumised")


#1.4 Bussid

import math
inimene = 138
koht = 40

jaak =inimene % koht


if jaak > 0:
    busside_arv = (inimene // koht)+1
else:
    busside_arv = inimene // koht

if jaak == 0:
    jaak = koht



print(f"Busside arb: {busside_arv}")
print(f"Viimases bussis on inimesi: {jaak}")

#2.1 Äratus

kordade_arv = int(input("Kordade arv:"))

for i in range (kordade_arv):
    print("Tõuse ja sära!")