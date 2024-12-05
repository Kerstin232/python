# h4
# Kerstin Lindh 05.12.2024

"""
Aia pikkus
Kirjuta programm, mis aitab aiapidajal arvutada aia ümbermõõtu.
Aed on ristküliku kujuline.
Programm peaks küsima kasutajalt kahe aiaosa pikkused meetrites ja seejärel arvutama aia kogupikkuse.
Väljasta lause, kasutades f-string vormindamist.
Näide:
Kasutaja sisestab: 4 ja 5
Programm väljastab: Aia kogupikkus on 18 meetrit."""

try:
    karbi_suurus = 5
    kingitused = int(input("Lisa kingituste arv: "))
    kastid = kingitused // karbi_suurus
    jaak = kingitused % karbi_suurus
    print(f"Saad teha {kastid} täis kinkekasti. Üle jääb {jaak} kingitust!")

except:
    print("Jälle tekitad probleeme!")

# a=int(input("sisesta külg 1: "))
# b=int(input("sisesta külg 2: "))
# ymbermoot=2*(a+b)
# print(f"Aia kogupikkus on {ymbermoot} meetrit.")
# 


