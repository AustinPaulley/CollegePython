#Austin Paulley Custom Functions



# Create a file to write the output

fileName = input("Enter the file name to write the output\n"\
                 "type \"txt\" at the end of the file name\n")

outputFile = open(fileName, "w")

# Close file
outputFile.close()


#Assignment 9 Maximum Values
while True:
    try:
        print("Enter a positive whole interger for number 1")
        interger1 = float(input())
    except ValueError:
        print("Wrong data type entered - Re-Enter Positive value")
        continue
    else:
        if (interger1 <= 0):
            print("You entered a negative value -Re-Enter a Positve Value\n")
            continue
        else:
            break
while True:
    try:
        print("Enter a positive whole interger for number 2")
        interger2 = float(input())
    except ValueError:
        print("Wrong data type enteed - Re-Enter Positive value")
        continue
    else:
        if (interger2 <= 0):
            print("You entered a negative value -Re-Enter a Positve Value\n")
            continue
        else:
            break
#Assignment 9 Feet to Inches
        
        while True:
    try:
        print("What is the number of feet you are attempting to convert to inches?")
        feet = float(input())
    except ValueError:
        print("Wrong data type entered - Re-Enter Positive value")
        continue
    else:
        if (feet <= 0):
            print("You entered a negative value -Re-Enter a Positve Value\n")
            continue
        else:
            break

        def toFixed (value, digits):
    return "%.*f" % (digits, value)

#Total Purchase 2

print("What is the current tax? [enter decimal i.e. 0.04, 0.07]")
while True:# This loop will check data for a number less then or equal to 0
    try:
        taxRate = float(input())
    except ValueError:
        print("You entered the wrong data type\n" \
                "Re-enter a positive value [decimals are acceptable]")
        continue
    else:
        if (taxRate < 0) or (taxRate > 1):
            print("You entered a value less then 0 or greater than 1 n" \
                "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            break

# Price 1
print("Enter 1st Items Price")
while True:# This loop will check data for a number less then or equal to 0
    try:
        price1 = float(input())
    except ValueError:
        print("You entered the wrong data type\n" \
                "Re-enter a positive value [decimals are acceptable]")
        continue
    else:
        if (price1 < 0):
            print("You entered a value less then 0\n" \
                "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            break


#Assignment 11 wTemp

#===================================================================================================================    
    # Define function to create the external file to store output
def createoutFile():
    # Create an external data file using functions/methods such as open, write and close
    # to write results to an external output file
    fName = input("Enter a file name to write the results to an output file\n")
    oFile = open(fName + ".txt", "w")
    return fName, oFile
    # end createoutFile function
#===================================================================================================================
# Function To Check Data Type (looking for positive whole interger)
def checkIntDataType(dataType):
    while True:
        try:
            dataType = int(input())
        except ValueError:
            print("Wrong data type entered - Re-Enter Positive value")
            continue;
        else:
            if (dataType <= 0):
                print("You entered a negative value -Re-Enter a Positve Value\n")
                continue;
            else:
                break;
    return dataType;
#end checkIntDataType(dataType) Function
                
#===================================================================================================================
#Function to Create a List
#Could not get to work

def checkFloatDataType(count, totalDays, wTemp, stateName):
    count = 0
    while(count < totalDays):
        print("What is the outdoor tempature in " + stateName + " " + format(count + 1, "2d" ) + ":")
        while True:
            try:
                wTemp[count] = int(input())
            except ValueError:
                print("Wrong Data Type - Enter A Numerical Value ");
                print()
                continue;
            else:
                if (wTemp[count] < 0):
                    print("Negative Value Entered - Re-Enter A Numerical Value ");
                    print()
                    continue;
                else:
                    break;
                 #Update lvc
                 count = count + 1
#end checkFloatDataType(count, totalDays, wTemp, stateName) Function







#assignment 15 ALL Functions
#Define Major Functions

#Function to set up the screen
def setUpScreen():
    import turtle                       #Import the turtle module
    turtle.speed(1000)                  #Increases pen speed
    wn = turtle.Screen()                #Set up the screen
    wn.setup(1000,800)                  #Define space
    wn.bgcolor("lawngreen")             #change background color to green
    wn.title("WINDOW FOR THE HOUSE")    #Title
    turtle.width(4)                     #Pen size = 4
    turtle.color("Purple")              #Pen color
    
    #end setUpScreen function

#=====================================================================================   
#Function to draw the Sky
def drawSky():

    #draw the sky
    turtle.penup()                      #Pull pen up
    turtle.goto(-500, -100)             #Set Location
    turtle.pendown()                    #Put pen down
    turtle.color("deepskyblue")         #Set Color
    turtle.begin_fill()                 #Start Color
    for i in range(2):                  #Create Area
        turtle.forward(1000)
        turtle.left(90)
        turtle.forward(500)
        turtle.left(90)
    turtle.end_fill()                   #End Color

    #End drawSky
    
#=====================================================================================
#Function to draw the sun
def drawSun():

    #draw the sun
    turtle.penup()                      #Pull pen up
    turtle.goto(-360, 225)              #Set Location
    turtle.pendown()                    #Put pen down
    turtle.color("yellow")              #Set Color
    turtle.begin_fill()                 #Start Color
    turtle.circle(75)                   #Define Shape
    turtle.end_fill()                   #Stop Color

    #End drawSun

#=====================================================================================
#Function to draw a cloud
def draw_An_Cloud():

    #draw an cloud
    turtle.pendown()                    #Pull pen down
    turtle.color("white")               #Turtle Color
    turtle.begin_fill()                 #Start Filling
    turtle.circle(25)                   #Create Circle
    turtle.end_fill()                   #End Fill
    turtle.penup()                      #Pull Pen Back up

    #End draw_An_Cloud
    
#=====================================================================================
#Function to draw clouds
def drawClouds():

    #Cloud 1
    turtle.penup()                      #Pull pen up
    turtle.goto(200,200)                #Set Pen Location
    draw_An_Cloud()                     #Call draw_An_Cloud Function
    turtle.goto(220,240)
    draw_An_Cloud()
    turtle.goto(230,215)
    draw_An_Cloud()
    turtle.goto(180,225)
    draw_An_Cloud()

    #Cloud 2
    turtle.goto(300,200)
    draw_An_Cloud()
    turtle.goto(320,240)
    draw_An_Cloud()
    turtle.goto(330,215)
    draw_An_Cloud()
    turtle.goto(280,225)
    draw_An_Cloud()

    #Cloud 3
    turtle.goto(-190,210)
    draw_An_Cloud()
    turtle.goto(-210,240)
    draw_An_Cloud()
    turtle.goto(-220,220)
    draw_An_Cloud()
    turtle.goto(-180,220)
    draw_An_Cloud()

    #End drawClouds

#=====================================================================================
#Function to draw the roof
def drawRoof():

    #draw the roof 
    turtle.penup()                      #Pull pen up
    turtle.goto(-127,70)                #Set Pen Location
    turtle.pendown()                    #Put pen down
    turtle.color("black","grey")        #Set Turtle Color
    turtle.begin_fill()                 #Start Turtle Color
    for i in range(3):                  #Define Area
        turtle.forward(225)
        turtle.left(120)
    turtle.end_fill()                   #Stop Turtle Color

    #End drawRoof

#=====================================================================================
#Function to draw the chimney
def drawChimney():

    #draw the Chimney
    turtle.penup()                      #Pull pen up
    turtle.goto(20,130)                 #Set Pen Location
    turtle.pendown()                    #Put pen down
    turtle.color("black","lightblue")   #Set Turtle Color
    turtle.begin_fill()                 #Start Color
    for i in range (2):                 #Define Area
        turtle.forward(40)
        turtle.left(90)
        turtle.forward(100)
        turtle.left(90)
    turtle.end_fill()                   #End Color
    
    #End drawChimney
    
#=====================================================================================
#Function to draw the house
def drawHouse():
    
    #draw The House
    turtle.penup()                      #Pull pen up
    turtle.goto(-100,-100)              #Set Location
    turtle.pendown()                    #Pull pen down
    turtle.pensize(3)                   #Set Pen Size
    turtle.color("black","lightblue")   #(stroke,fill)
    turtle.begin_fill()                 #Start Color
    for i in range(4):                  #Set Location
        turtle.forward(170)
        turtle.left(90)
    turtle.end_fill()                   #Stop Color

    #End drawHouse
    
#=====================================================================================
#Function to draw a window
def draw_An_Window():

    #Create A Window
    turtle.pendown()                    #Put Pen Down
    turtle.color("black","white")       #Set Pen Color
    turtle.begin_fill()                 #Start Color
    for i in range (4):                 #Create Box
        turtle.forward(50)
        turtle.left(90)
    turtle.end_fill()

    #window horizontal cross

    turtle.penup()                      #Pull pen Up
    turtle.left(90)                     #Left 90
    turtle.forward(25)                  #Forward 25
    turtle.right(90)                    #Right 90
    turtle.pendown()                    #Put Pen Down
    turtle.color("black")               #Set Color
    turtle.forward(50)                  #Forward 50

    #window vertical cross
    
    turtle.penup()                      #Pull pen Up
    turtle.right(90)                    #Right 90
    turtle.forward(25)                  #Forward 25
    turtle.right(90)                    #Right 90
    turtle.forward(25)                  #Forward 25
    turtle.right(180)                   #Right 180
    turtle.pendown()                    #Put pen Down
    turtle.left(90)                     #Left 90
    turtle.forward(50)                  #Forward 50
    turtle.penup()                      #Put pen Up

    #End draw_An_Window

#=====================================================================================
#Create Two Windows
def drawWindows():

    #Create Two Windows
    turtle.penup()                      #Pull pen Up
    turtle.goto(0,0)                    #Set Location
    draw_An_Window()                    #Call Function to Draw Window
    turtle.goto(-30,0)                  #Move Location
    draw_An_Window()                    #Call Function to Draw Window
    
    #End drawWindows
    
#=====================================================================================
#Create a Door
def drawDoor():

    #Draw a Door
    turtle.right(90)                    #Rotate Right 90
    turtle.penup()                      #Pull Pen up
    turtle.goto(-40,-97)                #Set Location
    turtle.pendown()                    #Put Pen down
    turtle.right(90)                    #Rotate Right 90
    turtle.color("black","white")       #Set Turtle Color
    turtle.begin_fill()                 #Start Color
    for i in range(2):                  #Create Shape
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(80)
        turtle.left(90)
    turtle.end_fill()                   #End Color

    #Draw a Door Handle

    turtle.penup()                      #Pull Pen up
    turtle.goto(-30,-60)                #Set location
    turtle.pendown()                    #Lower pen
    turtle.color("black")               #Set Color
    turtle.begin_fill()                 #Start color
    turtle.circle(5)                    #Create Shape
    turtle.end_fill()                   #Stop Color

    #End drawDoor
    
#=====================================================================================
#Create a Sidewalk
def drawSidewalk():

    #Draw a sidewalk
    turtle.penup()                      #Pull Pen up
    turtle.goto(-40,-400)               #Set Location
    turtle.pendown()                    #Lower Pen
    turtle.color("black","grey")        #Set Color
    turtle.begin_fill()                 #Start Color
    for i in range(2):                  #Create Shape
        turtle.forward(50)
        turtle.left(90)
        turtle.forward(300)
        turtle.left(90)
    turtle.end_fill()                   #Start Color
    turtle.penup()                      #Pull Pen up

    #End drawSidewalk
    
#=====================================================================================
#Create a Tree Base
def draw_An_Tree_Base():

    #Draw tree Base
    turtle.pendown()                    #Lower Pen
    turtle.color("black","brown")       #Set Pen Color
    turtle.begin_fill()                 #Start Color
    for i in range(2):                  #Create Shape
        turtle.forward(30)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
    turtle.end_fill()                   #End Color
    turtle.penup()                      #Pull Pen Up

    #End draw_An_Tree_Base
    
#=====================================================================================
#Create Tree Leaves
def draw_An_Tree_Leaves():

    #Draw Leaves
    turtle.pendown()                    #Lower Pen
    turtle.color("darkgreen")           #Set Pen Color
    turtle.begin_fill()                 #Start Color
    turtle.circle(25)                   #Create Shape
    turtle.end_fill()                   #End Color
    turtle.penup()                      #Raise Pen

    #End draw_An_Tree_Leaves
    
#=====================================================================================
#Create the Trees
def drawTrees():

    #Tree 1
    
    turtle.goto(150,-120)               #Set Location
    draw_An_Tree_Base()                 #Call Function to create base
    turtle.goto(170,60)                 #Move Location
    draw_An_Tree_Leaves()               #Call Function to make Leaves
    turtle.goto(190,100)                #Move Location
    draw_An_Tree_Leaves()               #Call Function to make Leaves
    turtle.goto(200,75)                 #Move Location
    draw_An_Tree_Leaves()               #Call Function to make Leaves
    turtle.goto(150,85)                 #Move Location
    draw_An_Tree_Leaves()               #Call Function to make Leaves
    turtle.goto(140,50)                 #Move Location
    draw_An_Tree_Leaves()               #Call Function to make Leaves
    turtle.goto(200,50)                 #Move Location

    #Tree 2
    
    turtle.goto(250,-220)
    draw_An_Tree_Base()
    turtle.goto(270,-40)
    draw_An_Tree_Leaves()
    turtle.goto(290,0)
    draw_An_Tree_Leaves()
    turtle.goto(300,-25)
    draw_An_Tree_Leaves()
    turtle.goto(250,-15)
    draw_An_Tree_Leaves()
    turtle.goto(240,-50)
    draw_An_Tree_Leaves()
    turtle.goto(300,-50)

    #Tree 3

    turtle.goto(-200,-120)
    draw_An_Tree_Base()
    turtle.goto(-180,60)
    draw_An_Tree_Leaves()
    turtle.goto(-160,100)
    draw_An_Tree_Leaves()
    turtle.goto(-150,75)
    draw_An_Tree_Leaves()
    turtle.goto(-200,85)
    draw_An_Tree_Leaves()
    turtle.goto(-210,50)
    draw_An_Tree_Leaves()
    turtle.goto(-150,50)

    #Tree 4

    turtle.goto(-350,-220)
    draw_An_Tree_Base()
    turtle.goto(-330,-40)
    draw_An_Tree_Leaves()
    turtle.goto(-310,0)
    draw_An_Tree_Leaves()
    turtle.goto(-300,-25)
    draw_An_Tree_Leaves()
    turtle.goto(-350,-15)
    draw_An_Tree_Leaves()
    turtle.goto(-360,-50)
    draw_An_Tree_Leaves()
    turtle.goto(-300,-50)

    #End drawTrees
    
#=====================================================================================
#Function to Create Bush
def draw_An_Bush():

    #Draw the Bush
    turtle.pendown()                    #Move Pen Down
    turtle.color("darkgreen")           #Set color
    turtle.begin_fill()                 #Start Color
    turtle.circle(25)                   #Create Shape
    turtle.end_fill()                   #Stop Color
    turtle.penup()                      #Raise Pen

    #End draw_an_Bush

#=====================================================================================
#Function to Create Flowers On Bush
def draw_An_Flower():

    #Draw a Flower
    turtle.pendown()                    #Move Pen Down
    turtle.color("black","red")         #Set Color
    turtle.begin_fill()                 #Start color
    turtle.circle(5)                    #Create Shape
    turtle.end_fill()                   #Start Color
    turtle.penup()                      #Raise Pen
    
    #End draw_An_Flower
#=====================================================================================
#Function to Create a Flowered Bush
def drawScrubs():

    #Create the Bush
    turtle.goto(170,-190)               #Move Turtle Location
    draw_An_Bush()                      #Call Funcion draw_An_Bush
    turtle.goto(190,-150)
    draw_An_Bush()
    turtle.goto(200,-175)
    draw_An_Bush()
    turtle.goto(150,-165)
    draw_An_Bush()
    turtle.goto(140,-200)
    draw_An_Bush()
    turtle.goto(200,-200)
    draw_An_Bush()

    #Create the Flowers
    #Flower 1
    turtle.goto(200,-140)               #Move Turtle Location
    draw_An_Bush()                      #Call Funcion draw_An_Flower
    draw_An_Flower()
    turtle.goto(205,-145)
    draw_An_Flower()
    turtle.goto(210,-140)
    draw_An_Flower()
    turtle.goto(205,-135)
    draw_An_Flower()

    #Flower 2
    turtle.goto(170,-140)
    draw_An_Flower()
    turtle.goto(175,-145)
    draw_An_Flower()
    turtle.goto(180,-140)
    draw_An_Flower()
    turtle.goto(175,-135)
    draw_An_Flower()

    #Flower 3
    turtle.goto(150,-160)
    draw_An_Flower()
    turtle.goto(155,-165)
    draw_An_Flower()
    turtle.goto(160,-160)
    draw_An_Flower()
    turtle.goto(155,-155)
    draw_An_Flower()

    #Flower 4
    turtle.goto(180,-160)
    draw_An_Flower()
    turtle.goto(185,-165)               
    draw_An_Flower()
    turtle.goto(190,-160)
    draw_An_Flower()
    turtle.goto(185,-155)
    draw_An_Flower()

    #Flower 5
    turtle.goto(170,-180)
    draw_An_Flower()
    turtle.goto(175,-185)
    draw_An_Flower()
    turtle.goto(180,-180)
    draw_An_Flower()
    turtle.goto(175,-175)
    draw_An_Flower()

    #Flower 6
    turtle.goto(130,-180)
    draw_An_Flower()
    turtle.goto(135,-185)
    draw_An_Flower()
    turtle.goto(140,-180)
    draw_An_Flower()
    turtle.goto(135,-175)
    draw_An_Flower()

    #Flower 7
    turtle.goto(200,-180)
    draw_An_Flower()
    turtle.goto(205,-185)
    draw_An_Flower()
    turtle.goto(210,-180)
    draw_An_Flower()
    turtle.goto(205,-175)               
    draw_An_Flower()                    

    #End drawScrubs
    
#=====================================================================================
#Function to Draw Ctber Truck Body
def draw_An_cyberTruckBody():

    #Create Cyber truck body
    turtle.pendown()
    turtle.right(90)
    turtle.color("black","lightgrey")
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(60)              #Move Forward 60
        turtle.left(90)                 #Move left 90
        turtle.forward(280)             #Move Forward 280
        turtle.left(90)                 #Move Left 90
    turtle.end_fill()                   #End Color
    turtle.right(-135)                  #Move right -135
    turtle.begin_fill()                 #Start Color
    turtle.forward(70)                  #Move Forward 70
    turtle.right(56.25)                 #Move Right 56.25
    turtle.forward(235)                 #Move forward 235
    turtle.right(78.75)                 #Move Right 78.75
    turtle.forward(30)                  #Move Forward 30
    turtle.end_fill()                   #End Color
    turtle.penup()                      #Pull Pen up

    #End draw_An_cyberTruckBody()
    
#=====================================================================================
#Function to draw Cyber Truck Window
def draw_An_cyberTruckWindow():

    #Create Cyber Truck Window
    turtle.left(90)                     #Move Left 90
    turtle.forward (20)                 #Move Forward 20
    turtle.pendown()                    #Lower Pen
    turtle.color("black","White")       #Change Color
    turtle.begin_fill()                 #Start Color
    turtle.left(45)                     #Move Left 45
    turtle.forward(40)                  #Move Forward 40
    turtle.right(135)                   #Move Forward 135
    turtle.forward(30)                  #Move Forward 30
    turtle.right(90)                    #Move Right 90
    turtle.forward(30)                  #Move Forward 30
    turtle.end_fill()                   #End Color
    turtle.penup()                      #Raise pen

    #End draw_An_cyberTruckWindow()

#=====================================================================================
#Function to Create Cyber Truck Wheels
def draw_An_cyberTruckWheel():

    #Create Cyber truck Wheel
    turtle.pendown()                    #Lower Pen
    turtle.color("black")               #Set Color
    turtle.begin_fill()                 #Start Color
    turtle.circle(30)                   #Set Shape
    turtle.end_fill()                   #Stop Color
    turtle.penup()                      #Raise Pen

    #End draw_An_cyberTruckWheel()
    
#=====================================================================================
#Function to Create CyberTruck
def drawCyberTruck():

    #Create Cyber Truck Body
    turtle.goto(-400,-200)              #Set Location
    draw_An_cyberTruckBody()            #Call Function

    #Create Cyber Truck Window
    turtle.goto(-400,-200)              #Set Location
    draw_An_cyberTruckWindow()          #Call Function

    #Create Cyber Truck Wheel
    turtle.goto(-350,-230)              #Set Location
    draw_An_cyberTruckWheel()           #Call Function
    turtle.goto(-175,-230)              #Set Location
    draw_An_cyberTruckWheel()           #Call Function
    turtle.hideturtle()                 #Hide Turtle
    
    #End drawCyberTruck()
    
#=====================================================================================

#Function to call all major tasks in this main / conductor function / module
def main():
    
    #Draw Sky
    setUpScreen()                       #call function to set up the screen background
    drawSky()                           #call function to draw the sky
    drawSun()                           #call function to draw the sun
    drawClouds()                        #call function to draw 3 clouds using draw_An_Cloud

    #Draw House
    drawHouse()                         #call function to draw House
    drawChimney()                       #call function to draw Chimney
    drawRoof()                          #call Function to draw Roof
    drawWindows()                       #call Function to draw Windows using draw_An_Window
    drawDoor()                          #call Function to draw Door and Handle
    drawSidewalk()                      #call Function to draw Sidewalk

    #Draw Scenery
    drawTrees()                         #call Function to draw Trees using
                                        #draw_An_Tree_Base and draw_An_Tree_Leaves
    drawScrubs()                        #Call Function to create a flowered bush using
                                        #draw_An_Bush and #draw_An_Flower
    drawCyberTruck()                    #Call Function to create cyber truck using
                                        #draw_An_cyberTruckBody,draw_An_cyberTruckWindow
                                        #And draw_An_cyberTruckWheel

    
    #end main function / modules
#=====================================================================================

#Call the main function module to run as a standalone or imported to other programs
if __name__ == '__main__':
    main()

#=====================================================================================
#END PROGRAM


#Assignment 15 Gas Expensse

#===================================================================================================================    
    # Define function to create the external file to store output
def createoutFile():
    # Create an external data file using functions/methods such as open, write and close
    # to write results to an external output file
    fName = input("Enter a file name to write the results to an output file\n")
    oFile = open(fName + ".txt", "w")
    return fName, oFile
    # end createoutFile function
    
#===================================================================================================================
# Function To Check Data Type (looking for positive whole interger)
def checkIntDataType(dataType):
    while True:
        try:
            dataType = int(input())
        except ValueError:
            print("Wrong data type entered - Re-Enter Positive value")
            continue;
        else:
            if (dataType <= 0):
                print("You entered a negative value -Re-Enter a Positve Value\n")
                continue;
            else:
                break;
    return dataType;
#end checkIntDataType(dataType) Function
                
#===================================================================================================================
#Funtion to create list
def createList(count, totalFillUps, stationName, gasExpenses):
    while(count < totalFillUps):
        print("What was the price at " + stationName + " " + format(count + 1, "2d" ) + ":")
        while True:
            try:
                gasExpenses[count] = int(input())
            except ValueError:
                print("Wrong Data Type - Enter A Numerical Value ");
                print()
                continue;
            else:
                if (gasExpenses[count] < 0):
                    print("Negative Value Entered - Re-Enter A Numerical Value ");
                    print()
                    continue;
                else:
                    count = count + 1
                    break;

#End createList(count, totalFillUps, stationName, gasExpenses)
                
#===================================================================================================================
#Function to output the averages
def bottomStats(outFile, gasExpenses, average):
    outFile.write("============================================================="+ "\n")
    outFile.write(" "*15 + "Minumum Fill Up = " + "$ " + format(min(gasExpenses) , "6.2f")  + "\n")
    outFile.write(" "*15 + "Maximum Fill Up = " + "$ " + format(max(gasExpenses) , "6.2f")  + "\n")
    outFile.write(" "*15 + "Average Fill Up = " + "$ " + format(average, "6.2f") + "\n")
    outFile.write("=============================================================" + "\n")
#End bottomStats
    
#===================================================================================================================
#Function to determine greater or equal to 95
def determineGreaterOrEqualTo95(count, totalFillUps, gasExpenses, gasExpensesG):
    #Reset array
    count = 0
    gCount = 0
    while count < totalFillUps:
        if gasExpenses[count] > 94:
            gasExpensesG[count] = gasExpenses[count]
            gCount = gCount + 1;

        count = count + 1;
        
    return gCount;

#End determineGreaterOrEqualTo95(count, totalFillUps, gasExpenses, gasExpensesG)
    
#===================================================================================================================
def writeGreaterOrEqualTo95(count, totalFillUps, gasExpensesG, gCount, outFile):
    count=0
    
    outFile.write("============================================================="+ "\n")
    outFile.write("      Gas Expenses Greater Than or Equal To $95.00"+ "\n")
    outFile.write("============================================================="+ "\n")
    while count < totalFillUps:
        if gasExpensesG[count] != 0:
            outFile.write(" " *32 + format(gasExpensesG[count], "6.2f")+ "\n")
        count = count + 1;
        #End While Loop

    outFile.write("\n");
    outFile.write("============================================================="+ "\n")
    outFile.write(format(format("Gas Expenses >= $95 occur(s) ") +
                             format(gCount, "2d") + "time(s).", "^70s") + "\n");
    outFile.write("============================================================="+ "\n")
    return outFile;
#end def writeGreaterOrEqualTo95              

#===================================================================================================================
#Function to determine Less than 35
def determineLessThan35(count, totalFillUps, gasExpenses, gasExpensesF):
    #Reset array
    count = 0
    fCount = 0
    gasExpensesF[count] = 0
    while count < totalFillUps:
        if gasExpenses[count] < 36:
            gasExpensesF[count] = gasExpenses[count]
        fCount = fCount + 1;

        count = count + 1;
        
    return fCount;
#End determineLessThan35(count, totalFillUps, gasExpenses, gasExpensesF)
    
#===================================================================================================================
def writeLessThan35(count, totalFillUps, gasExpensesF, fCount, outFile):
    count=0
    
    outFile.write("============================================================="+ "\n")
    outFile.write("      Gas Expenses Less Than or Equal To $35.00"+ "\n")
    outFile.write("============================================================="+ "\n")
    while count < totalFillUps:
        if gasExpensesF[count] != 0:
            outFile.write(" " *32 + format(gasExpensesF[count], "6.2f")+ "\n")
        count = count + 1;
        #End While Loop

    outFile.write("\n");
    outFile.write("============================================================="+ "\n")
    outFile.write(format(format("Gas Expenses >= $35 occur(s) ") +
                             format(fCount, "2d") + "time(s).", "^70s") + "\n");
    outFile.write("============================================================="+ "\n")
    return outFile;
    #end writeLessThan35(count, totalFillUps, gasExpensesF, fCount, outFile)              

#===================================================================================================================
#Function to determine Less than 35
def determineGreaterThan35LessThan50(count, totalFillUps, gasExpenses, gasExpensesH):
    #Reset array
    count = 0
    hCount = 0
    gasExpensesH[count] = 0
    while count < totalFillUps:
        if gasExpenses[count] >35 and gasExpenses[count] <=50:
            gasExpensesH[count] = gasExpenses[count]
        hCount = hCount + 1;

        count = count + 1;
        
    return hCount;

#End determineGreaterThan35LessThan50(count, totalFillUps, gasExpenses, gasExpensesH)
    
#===================================================================================================================
def writeGreaterThan35LessThan50(count, totalFillUps, gasExpensesH, hCount, outFile):
    count=0
    
    outFile.write("============================================================="+ "\n")
    outFile.write("      Gas Expenses Greater Than $35 But Less Than $50 "+ "\n")
    outFile.write("============================================================="+ "\n")
    while count < totalFillUps:
        if gasExpensesH[count] != 0:
            outFile.write(" " *32 + format(gasExpensesH[count], "6.2f")+ "\n")
        count = count + 1;
        #End While Loop

    outFile.write("\n");
    outFile.write("============================================================="+ "\n")
    outFile.write(format(format("Gas Expenses  >$35 or <=50 occur(s) ") +
                             format(hCount, "2d") + "time(s).", "^70s") + "\n");
    outFile.write("============================================================="+ "\n")
    return outFile;
    #end writeGreaterThan35LessThan50(count, totalFillUps, gasExpensesH, hCount, outFile)            

#===================================================================================================================
#Function to determine Less than 35
def determineGreaterThan50LessThan95(count, totalFillUps, gasExpenses, gasExpensesI):
    #Reset array
    count = 0
    iCount = 0
    gasExpensesI[count] = 0
    while count < totalFillUps:
        if gasExpenses[count] >50 and gasExpenses[count] <95:
            gasExpensesI[count] = gasExpenses[count]
        iCount = iCount + 1;

        count = count + 1;

    return iCount;

    #End determineGreaterThan50LessThan95(count, totalFillUps, gasExpenses, gasExpensesI)
    
#===================================================================================================================
def writeGreaterThan50LessThan95(count, totalFillUps, gasExpensesI, iCount, outFile):
    count=0
    
    outFile.write("============================================================="+ "\n")
    outFile.write("      Gas Expenses Greater Than $50 But Less Than $95 "+ "\n")
    outFile.write("============================================================="+ "\n")
    while count < totalFillUps:
        if gasExpensesI[count] != 0:
            outFile.write(" " *32 + format(gasExpensesI[count], "6.2f")+ "\n")
        count = count + 1;
        #Emd While Loop

    outFile.write("\n");
    outFile.write("============================================================="+ "\n")
    outFile.write(format(format("Gas Expenses  >$50 or <95 occur(s) ") +
                             format(iCount, "2d") + "time(s).", "^70s") + "\n");
    outFile.write("============================================================="+ "\n")
    return outFile;
    #end writeGreaterThan50LessThan95(count, totalFillUps, gasExpensesH, hCount, outFile)

#===================================================================================================================




        


