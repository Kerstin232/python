#ülesanne 3
#kerstin lindh 05.12.2024

# 3.1
nimi = "imre"# sõne ee - string eng lüh str
vanus = 20 #intm integer -ee täisarv
keskmine = 4.53 # float -ee komarv
#plussiga kokku
print(nimi+" "+str(vanus)+" aastat vana ja keskmine hinne on "+str(keskmine))
#komaga kokku 
print(nimi,",",vanus," aastat vana ja keskmine hinne on",keskmine)
print(f"{nimi}, {vanus} aastat vana ja keskmine hinne on {keskmine}")

# 3.7
import turtle
# kolmnurk 1
kylje_pikkus = 30
nurk = 120
varv = "red"
turtle.speed(2) #reguleeri 0-9
turtle.color(varv)
turtle.fd(kylje_pikkus) #fd - forward lühi
turtle.left(nurk)#left right käsud -- lt/rt
turtle.fd(kylje_pikkus) #fd - forward lühi
turtle.left(nurk) # left right käsud -- lt/rt
turtle.fd(kylje_pikkus) #fd - forward lühi
turtle.left(120) # left right käsud -- lt/rt


turtle.penup()
turtle.goto(kylje_pikkus*1.5,0)
turtle.pendown()
#kolmnurk 2
turtle.speed(2) #reguleeri 0-9
turtle.color(varv)
turtle.fd(kylje_pikkus) #fd - forward lühi
turtle.left(nurk)#left right käsud -- lt/rt
turtle.fd(kylje_pikkus) #fd - forward lühi
turtle.left(nurk) # left right käsud -- lt/rt
turtle.fd(kylje_pikkus) #fd - forward lühi
turtle.left(nurk)

turtle.penup()
turtle.goto(kylje_pikkus*3,0)
turtle.pendown()
#kolmnurk 3
turtle.speed(2) #reguleeri 0-9
turtle.color(varv)
turtle.fd(kylje_pikkus) #fd - forward lühi
turtle.left(nurk)#left right käsud -- lt/rt
turtle.fd(kylje_pikkus) #fd - forward lühi
turtle.left(nurk) # left right käsud -- lt/rt
turtle.fd(kylje_pikkus) #fd - forward lühi


turtle.done()