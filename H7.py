# Ülesanne 7.2
# Kasuta etteantud loendit ja toesta nõutud operatsioonid. Lisa igale tegevusele kommentaar ja vasta täislausega:
# “jaanuar”,-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3
# Kuva mõõdetava kuu nimetus
# Kuva viimase mõõtmise tulemus
# Kuva ainult temperatuurid
# Leia kuu maksimaalne ja minimaalne temperatuur
# Leia kuu keskmine temperatuur
# Mitu korda esines -20 kraadi
# Eemalda element nr 5
# Lisa 5. elemendi kohale temperatuur, mis on sinu vanus
# Sorteeri temperatuurid nimekirjas kasvavas järjekorras


Jtemp = ["jaanuar",-16,-12,-15,-20,0,-1,-20,-2,-20,-14,-18,-8,2,-1,-14,-7,-15,-17,-6,-17,-17,-7,0,3,-20,-17,-15,-8,-12,3]
print(f"Mõõdetav kuu:{Jtemp[0]}")
print(f"Viimase mõõtmise tulemus:{Jtemp[-1]} kraadi")

maks = -100
mini = 100
summa = 0
Kokku = 0
kordused = 0

for t in range(1, len(Jtemp)):
    print(Jtemp[t],end=" ") #prindib kõik tempid
    if Jtemp[t]>maks: #max temp kontroll
        maks =Jtemp[t]
        if Jtemp[t]<mini:    #min temp konrtorll
            mini=Jtemp[t]
        summa+=Jtemp[t]
        Kokku+=1
        if Jtemp[t]== -20:
            kordused+=1

Jtemp.pop(5)
Jtemp.insert(5,24)
#Jtemp.sort()

print()
print(f"maksimum temp on: {maks}")
print(f"Miinimum temp on: {mini}")
print(f"Keskmine temp on: {summa/Kokku:0.2f}")
print(f"Temp -20 esineb: {kordused} korda")