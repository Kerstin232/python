## 	Iseseisev töö nr2 /

algnesaldo = 100
valik = input("deposiit või väljavõte? ")

if valik == "deposiit":
    summa = int(input("Sisesta summa: "))
    algnesaldo += summa
    print("Saldo", algnesaldo)

elif valik == "väljavõte":
    summa = int(input("Sisesta summa: "))
    algnesaldo -= summa
    print("Saldo", algnesaldo)
