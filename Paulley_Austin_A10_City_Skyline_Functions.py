#Main Function (drawCity_Skyline)
def square(x, y, width, color):
    turtle.penup()
    turtle.goto(x, y)
    turtle.fillcolor(color)
    turtle.pendown
    turtle.begin_fill()
    for count in range(4):
        turtle.forward(width)
        turtle.left(90)
    turtle.end_fill()
    
#====================================================
# PROGRAMMER: AUSTIN PAULLEY
# PROGRAM NAME: Creating a Skyline
# Date Witten: 4/11/2022
# Purpose: Creating Turtle Designs and Organizing As Functions
#====================================================

#Startup Turtle
import turtle
turtle.speed(0)

#Background(setup_Screen)
square( -500, -500, 1000, 'black')

#Stars(draw_Stars)
square( -400, 300, 7, 'white')
square( -350, 256, 7, 'white')
square( 100, 140, 7, 'white')
square( 200, 300, 7, 'white')
square( 340, 250, 7, 'white')

#Buildings(draw_Building)
square( -500, -500, 400, 'grey')
square( 0, -500, 400, 'grey')
square( 300, -500, 600, 'grey')
square( -200, 0, 100,'grey')
square( -200, 100, 100,'grey')
square( -200, 200, 100,'grey')
square( -100, 0, 100,'grey')
square( -100, 100, 100,'grey')
square( -300, 0, 100,'grey')
square( -100, -500, 100,'grey')
square( -100, -400, 100,'grey')
square( -100, -300, 100,'grey')
square( -100, -200, 100,'grey')
square( -100, -100, 100,'grey')
square( -200, -100, 100,'grey')
square( -300, -100, 100,'grey')
square( 200, -100, 100,'grey')

#Windows(draw_Windows
square( -280, 0, 15,'white')
square( -160, 100, 15,'white')
square( -150, 200, 15,'white')
square( -50, 50, 15,'white')
square( -155, 0, 15,'white')
square( 375, 0, 15,'white')
square( 275, -50, 15,'white')
square( 345, 20, 15,'white')

#Ending Program
turtle.hideturtle()

#END Program
    
