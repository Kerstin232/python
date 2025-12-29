## 	Iseseisev töö nr2 /

algnesaldo = 100
vali = input("deposiit või väljavõte? ")

if vali == "deposiit":
    summa = int(input("Sisesta summa: "))
    algnesaldo += summa
    print("Saldo", algnesaldo)

elif vali == "väljavõte":
    summa = int(input("Sisesta summa: "))
    algnesaldo -= summa
    print("Saldo", algnesaldo)
