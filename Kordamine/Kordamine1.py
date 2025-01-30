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

    #2.2 Porgand

porgandid = 0
ringide_arv = 6 

while  ringide_arv > 0:
    if ringide_arv % 2 == 0:
        porgandid += ringide_arv    
    ringide_arv-=1

print(porgandid)

#2.5

import random

ounad = 14
pp = int(input("Mitu pp tahab õuna: "))

for i in range(pp):
    suv_oun = random.randint (1,2)
    print(suv_oun)
    ounad -= suv_oun

print(f"Lumuvalkekesele jäi {ounad} õuna!")


#3.1

fail = open("C:/Users/klindh/Documents/GitHub/python/Kordamine/rebased.txt", encoding="UTF-8") 

vastuvõetud = []

for rida in fail:
    vastuvõetud.append(int(rida))

fail.close()

aasta = input("Lisa aasta 2011 -2019: ")

print(vastuvõetud[int(aasta[3])-1])


#3.3 Sissetulekud

fail = open("C:/Users/klindh/Documents/GitHub/python/Kordamine/konto.txt", encoding="UTF-8") 



for kirje in fail:
    if float (kirje) >0:
        print(float(kirje), end= "\n")


fail.close()



#3.3 jukebox
musa = "edm.txt"
fail = open("C:/Users/klindh/Documents/GitHub/python/Kordamine/edm.txt", encoding="UTF-8") 

nr = 1
for pala in fail:
        print (str(nr)+"."+pala, end="")
        nr+=1


print()       
Valik = int(input("Vali lugu: "))
fail = open("C:/Users/klindh/Documents/GitHub/python/Kordamine/edm.txt", encoding="UTF-8") 
mangin = 1
for pala in fail:
        if Valik == mangin:
                print(pala, end="")
        mangin+=1


fail.close()








