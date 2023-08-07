#precode==================================================================
#Programmer: Austin Paulley
#Program name: Assignment #07 Graphic House Design using FOR LOOPS
#Date Written: 3-23
#start code==============================================================
import turtle
turtle.speed(0)

    #grass==================================================================

    turtle.bgcolor("lawngreen")

#sky==================================================================

turtle.penup()
turtle.goto(-500, -100)
turtle.pendown()
turtle.color("deepskyblue")
turtle.begin_fill()
for i in range(2):
    turtle.forward(1000)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
turtle.end_fill()

#sun==================================================================

turtle.penup()
turtle.goto(-360, 225)
turtle.pendown()
turtle.color("yellow")
turtle.begin_fill()
turtle.circle(75)
turtle.end_fill()

    #cloud1==================================================================

    turtle.penup()
    turtle.goto(200,200)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(220,240)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(230,215)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(180,225)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(25)
    turtle.end_fill()

    #cloud2==================================================================

    turtle.penup()
    turtle.goto(300,200)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(320,240)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(330,215)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(280,225)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.end_fill()

    #cloud3==================================================================

    turtle.penup()
    turtle.goto(-180,210)
    turtle.pendown()
    turtle.color("white")
    turtle.begin_fill()
    turtle.circle(45)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-220,240)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(45)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-230,215)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(45)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-170,215)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(45)
    turtle.end_fill()

#house==================================================================

turtle.penup()
turtle.goto(-100,-100)
turtle.pendown()
turtle.pensize(3)
turtle.color("black","lightblue")#(stroke,fill)
turtle.begin_fill()
for i in range(4):
    turtle.forward(170)
    turtle.left(90)
turtle.end_fill()

#chimney================================================================

turtle.penup()
turtle.goto(20,130)
turtle.pendown()
turtle.color("black","lightblue")
turtle.begin_fill()
for i in range (2):
    turtle.forward(40)
    turtle.left(90)
    turtle.forward(100)
    turtle.left(90)
turtle.end_fill()

#roof====================================================================

turtle.penup()
turtle.goto(-127,70)
turtle.pendown()
turtle.color("black","grey")
turtle.begin_fill()
for i in range(3):
    turtle.forward(225)
    turtle.left(120)
turtle.end_fill()

#window 1================================================================

turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.color("black","white")
turtle.begin_fill()
for i in range (4):
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()

#window 1 horizontal cross

turtle.penup()
turtle.goto(0,25)
turtle.pendown()
turtle.color("black")
turtle.forward(50)

#window 1 vertical cross

turtle.penup()
turtle.goto(25,0)
turtle.pendown()
turtle.left(90)
turtle.forward(50)

#window 2================================================================

turtle.penup()
turtle.goto(-80,0)
turtle.pendown()
turtle.right(90)
turtle.color("black","white")
turtle.begin_fill()
for i in range (4):
    turtle.forward(50)
    turtle.left(90)
turtle.end_fill()

#window 2 horizontal cross

turtle.penup()
turtle.goto(-80,25)
turtle.pendown()
turtle.color("black")
turtle.forward(50)

#window 2 vertical cross

turtle.penup()
turtle.goto(-55,0)
turtle.pendown()
turtle.left(90)
turtle.forward(50)

#door================================================================

turtle.penup()
turtle.goto(-40,-97)
turtle.pendown()
turtle.right(90)
turtle.color("black","white")
turtle.begin_fill()
for i in range(2):
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
turtle.end_fill()

#door handle

turtle.penup()
turtle.goto(-30,-60)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#sidewalk==============================================================

turtle.penup()
turtle.goto(-40,-400)
turtle.pendown()
turtle.color("black","grey")
turtle.begin_fill()
for i in range(2):
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(300)
    turtle.left(90)
turtle.end_fill()

#tree 1==============================================================
#tree base 

turtle.penup()
turtle.goto(150,-120)
turtle.pendown()
turtle.color("black","brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()

#tree leafs 

turtle.penup()
turtle.goto(170,60)
turtle.pendown()
turtle.color("darkgreen")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(190,100)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(200,75)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(150,85)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(140,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(200,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

#tree 2==============================================================
#tree base 

turtle.penup()
turtle.goto(250,-220)
turtle.pendown()
turtle.color("black","brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()

#tree leafs

turtle.penup()
turtle.goto(270,-40)
turtle.pendown()
turtle.color("darkgreen")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(290,0)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(300,-25)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(250,-15)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(240,-50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(300,-50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

#tree 3 ==============================================================
#tree base 

turtle.penup()
turtle.goto(-200,-120)
turtle.pendown()
turtle.color("black","brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()

#tree leafs 

turtle.penup()
turtle.goto(-180,60)
turtle.pendown()
turtle.color("darkgreen")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-160,100)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-150,75)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-200,85)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-210,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-150,50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

#tree 4 ==============================================================
#tree base 

turtle.penup()
turtle.goto(-350,-220)
turtle.pendown()
turtle.color("black","brown")
turtle.begin_fill()
for i in range(2):
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(200)
    turtle.left(90)
turtle.end_fill()

#tree leafs

turtle.penup()
turtle.goto(-330,-40)
turtle.pendown()
turtle.color("darkgreen")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-310,0)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-300,-25)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-350,-15)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-360,-50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(-300,-50)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

#right bush=============================================
turtle.penup()
turtle.goto(170,-190)
turtle.pendown()
turtle.color("darkgreen")
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(190,-150)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(200,-175)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(150,-165)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(140,-200)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

turtle.penup()
turtle.goto(200,-200)
turtle.pendown()
turtle.begin_fill()
turtle.circle(25)
turtle.end_fill()

#right bush flower 1


turtle.penup()
turtle.goto(200,-140)
turtle.pendown()
turtle.color("black","red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(205,-145)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(210,-140)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(205,-135)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#right bush flower 2

turtle.penup()
turtle.goto(170,-140)
turtle.pendown()
turtle.color("black","orange")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(175,-145)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(180,-140)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(175,-135)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#right bush flower 3

turtle.penup()
turtle.goto(150,-160)
turtle.pendown()
turtle.color("black","red")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(155,-165)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(160,-160)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(155,-155)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#right bush flower 4

turtle.penup()
turtle.goto(180,-160)
turtle.pendown()
turtle.color("black","yellow")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(185,-165)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(190,-160)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(185,-155)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#right bush flower 

turtle.penup()
turtle.goto(170,-180)
turtle.pendown()
turtle.color("black","orange")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(175,-185)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(180,-180)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(175,-175)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()
#right bush flower 6

turtle.penup()
turtle.goto(130,-180)
turtle.pendown()
turtle.color("black","yellow")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(135,-185)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(140,-180)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(135,-175)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#right bush flower 7

turtle.penup()
turtle.goto(200,-180)
turtle.pendown()
turtle.color("black","yellow")
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(205,-185)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(210,-180)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

turtle.penup()
turtle.goto(205,-175)
turtle.pendown()
turtle.begin_fill()
turtle.circle(5)
turtle.end_fill()

#cybertruck================================================================================
turtle.penup()
turtle.goto(-400,-200)
turtle.pendown()
turtle.right(90)
turtle.color("black","lightgrey")
turtle.begin_fill()
for i in range(2):
    turtle.forward(60)
    turtle.left(90)
    turtle.forward(280)
    turtle.left(90)
turtle.end_fill()

turtle.right(-135)
turtle.begin_fill()
turtle.forward(70)
turtle.right(56.25)
turtle.forward(235)
turtle.right(78.75)
turtle.forward(30)
turtle.end_fill()

#cyberwindow==============================================================================

turtle.penup()
turtle.goto(-400,-200)
turtle.left(90)
turtle.forward (20)
turtle.pendown()
turtle.color("black","White")
turtle.begin_fill()
turtle.left(45)
turtle.forward(40)
turtle.right(135)
turtle.forward(30)
turtle.right(90)
turtle.forward(30)
turtle.end_fill()

#cyberwheels===============================================================================

#leftwheel
turtle.penup()
turtle.goto(-350,-230)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()
#rightwheel
turtle.penup()
turtle.goto(-175,-230)
turtle.pendown()
turtle.color("black")
turtle.begin_fill()
turtle.circle(30)
turtle.end_fill()

#hide turtle=============================================================================

turtle.hideturtle()

#end code==================================================================================



