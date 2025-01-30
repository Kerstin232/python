# 01 ülesanne
#kerstin


#see importib kilpkonna mooduli
import turtle

#kolmnurk
turtle.speed(2) #reguleeri 0-9
turtle.penup()
turtle.goto(-500,200)
turtle.pendown()
turtle.fd(200) #fd - forward lühi
turtle.left(120) # left right käsud -- lt/rt
turtle.fd(200) #fd - forward lühi
turtle.left(120) # left right käsud -- lt/rt
turtle.fd(200) #fd - forward lühi
turtle.left(120) # left right käsud -- lt/rt

#süda
turtle.penup()
turtle.goto(-200,200)
turtle.pendown()
turtle.fd(100)
turtle.circle(50,180)
turtle.right(90)
turtle.circle(50,180)
turtle.fd(100)

#lõpetab kilpkonna kokku ei jookseks 
turtle.done()
