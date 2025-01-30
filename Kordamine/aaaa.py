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









