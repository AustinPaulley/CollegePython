#-----------------------------------------------------------------------
# PROGRAMMER: Austin Paulley
# PROGRAM NAME: Assignment 2 1st Turtle
# DATE WRITTEN: 2/7
# PURPOSE: Rectangle with dotted lines
#-----------------------------------------------------------------------
import turtle
#icon shape
turtle.pensize(2);#changes pen size
turtle.speed(10)#changes turtle speed
turtle.shape("turtle");# changes shape to turtle
#start of code
#-----------------------------------------------------------------------
#starts solid lines
turtle.left(45)#turns Turtle Left 45
turtle.forward(250)#turtle moves 250
turtle.right(135)#turns Turtle right 135
turtle.forward(353)#moves Turtle 353
turtle.right(135)#turns Turtle right 135
turtle.forward(500)#moves Turtle 500 to make middle line 1
turtle.left(135)#moves Turtle left 135
turtle.forward(353)#moves turtle forward 353
turtle.left(135)#turns Turtle 135
turtle.forward(500)#moves turtle 500 to crate second middle line
#ends to solid lines
#---------------------------------------------------------------------
#starts top dotted lines
turtle.left(135)#moving turtle to face top line
turtle.forward(50)#pen up and down creating top line
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(53)
turtle.left(135)#end of top line
turtle.forward(500)#moving turtle to bottem right
#ends dotted lines
#---------------------------------------------------------------------
#bottom dotterd lines
turtle.right(135)#moving turtle to face bottem line
turtle.forward(50)#pen up and down creating bottem line
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(50)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(53)#end of the bottom line
#-----------------------------------------------------------------------
#ending programs
turtle.hideturtle();#Hides Turtle
#-----------------------------------------------------------------------
#end code
#Ending Programs
turtle.hideturtle();#Hides Turtle
