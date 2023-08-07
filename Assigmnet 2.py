#-----------------------------------------------------------------------
# PROGRAMMER: Austin Paulley
# PROGRAM NAME: Assignment 2 Code 1
# DATE WRITTEN: 2/7
# PURPOSE: Drawing the Olympic Rings Logo
#-----------------------------------------------------------------------
import turtle

turtle.shape("turtle");

#Blue Circle
turtle.width(10);
turtle.color("blue");
turtle.penup();
turtle.goto(-110,-25);
turtle.pendown();
turtle. circle(45);
#Black Circle
turtle.color("black");
turtle.penup();
turtle.goto(0,-25);
turtle.pendown();
turtle. circle(45);
#Red Circle
turtle.color("red");
turtle.penup();
turtle.goto(110,-25);
turtle.pendown();
turtle. circle(45);
#Yellow Circle
turtle.color("yellow");
turtle.penup();
turtle.goto(-55,-75);
turtle.pendown();
turtle. circle(45);
#Green Circle
turtle.color("green");
turtle.penup();
turtle.goto(55,-75);
turtle.pendown();
turtle. circle(45);
#----------------------------------------------------------------------
#End of Program
