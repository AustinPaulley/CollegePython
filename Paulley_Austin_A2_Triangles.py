#-----------------------------------------------------------------------
# PROGRAMMER: Austin Paulley
# PROGRAM NAME: Assignment 2 2nd Turtle
# DATE WRITTEN: 2/7
# PURPOSE: Triangle inside of another Triangle
#-----------------------------------------------------------------------
import turtle
#icon shape
turtle.pensize(2);#changes pen size
turtle.speed(10)#changes turtle speed
turtle.shape("turtle");# changes shape to turtle

#start of code
#-----------------------------------------------------------------------
#triangle 1
turtle.forward(250);#starts first line
turtle.left(120);#turns turtle 120
turtle.forward(250);#starts second line
turtle.left(120);##turns turtle 120
turtle.forward(250);#starts third line
#------------------------------------------------------------------------
#triangle 2
turtle.fillcolor("blue");#starts the blue for the second triangle
turtle.begin_fill();#starts fill
turtle.left(120);#turns turtle 120
turtle.forward(250);#move turtle 250 to first corner
turtle.left(140);#turns 140
turtle.forward(163);#first line of second triangle
turtle.left(80);#turns 80
turtle.forward(163);#second line of second triangle
#-----------------------------------------------------------------------
#ending programs
turtle.hideturtle();#hides Turtle
turtle.end_fill();#ends fill
#-----------------------------------------------------------------------
#end Code
