#Ülesanne 2
#05.12.2024

import turtle

#akna seaded
aken = turtle.screen()
aken.setup(width=500,height=400)
aken.title("olüpiarõngad, Kerstin Lindh")


#sinine kilpkonn
turtle.speed(0)
turtle.penup()
turtle.goto(-200,100)
turtle.pendown()
turtle.color("blue")
turtle.pensize(6)
turtle.circle(50,360)
#must kilpkonn
turtle.speed(0)
turtle.penup()
turtle.goto(-90,100)
turtle.pendown()
turtle.color("black")
turtle.pensize(6)
turtle.circle(50,360)
#punane
turtle.speed(0)
turtle.penup()
turtle.goto(80,100)
turtle.pendown()
turtle.color("red")
turtle.pensize(6)
turtle.circle(50,360)
#kollane
turtle.speed(0)
turtle.penup()
turtle.goto(-150,100)
turtle.pendown()
turtle.color("red")
turtle.pensize(6)
turtle.circle(50,360)
#rohleline
turtle.speed(0)
turtle.penup()
turtle.goto(-30,100)
turtle.pendown()
turtle.color("green")
turtle.pensize(6)
turtle.circle(50,360)

