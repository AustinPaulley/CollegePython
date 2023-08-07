def toFixed (value, digits):
    return "°.*f" % (digits, value)


#===================================================================================================================
# Programmer: Austin Paulley
# Program Name: Assignment 11 Creating And Manipulating Arays or Lists
# Date: 4/18/2022
# Purpose: Finding Average Temp\
#===================================================================================================================

#Processed Variables
total=0.00
average=0.0
count=0


#Create Export File

fileName = input("Enter the file name to write the output\n"\
                 "type \"txt\" at the end of the file name\n")

outputFile = open(fileName, "w")

#===================================================================================================================

# Define State Name
print("Enter the name of the state you are recording the \n daily tempature for: [i.e. Flordia,Georgia, New York]")
stateName = input()



# define the size pr the list/array
while True:
    try:
        print("How many days will you record the outdoor tempature \n for the state of " + stateName)
        totalDays = int(input())
    except ValueError:
        print("Wrong data type entered - Re-Enter Positive value")
        continue
    else:
        if (totalDays <= 0):
            print("You entered a negative value -Re-Enter a Positve Value\n")
            continue
        else:
            break

wTemp = [0] * (totalDays)


# use While loop to Create the Array list "name"


while count < totalDays:
        print("What is the outdoor tempature in " + stateName + " " + format(count + 1, "2d" ) + ":")
        wTemp[count] = float(input())

        #Update lvc
        count = count + 1

#==========================================================================================================

#calculate total or sum then the average
total = sum(wTemp)
average = total / totalDays
        
# set count to 0
count = 0
#=========================================================================================================
# Unsorted heading
outputFile.write("============================================================="+ "\n")
outputFile.write("    Unsorted Temperature's List for the state of " + stateName + "\n")
outputFile.write("============================================================="+ "\n")

# File Use while loop to Create the Array/list "name"
while count < totalDays:
    outputFile.write(f'{" "*16} {"wTemp "}{str(count + 1)}{" = "} {wTemp[count]} {"°"}' + "\n")
    count = count + 1
outputFile.write("=============================================================" + "\n")
outputFile.write(" "*16 + "Minumum Temp = " + format(min(wTemp) , "6.2f") + "°" + "\n")
outputFile.write(" "*16 + "Maximum Temp = " + format(max(wTemp) , "6.2f") + "°" + "\n")
outputFile.write(" "*16 + "Average Temp = " + format(average, "6.2f") + "°" + "\n")
outputFile.write("=============================================================" + "\n")
#==========================================================================================================
#Call sort function
wTemp.sort()

#Reset array
count = 0
#Sort wTemp[count]


outputFile.write("============================================================="+ "\n")
outputFile.write(" Sorted Temperature's List for the state of " + stateName + "\n")
outputFile.write("============================================================="+ "\n")
while count < totalDays:
    outputFile.write(f'{" "*16} {"wTemp "}{str(count + 1)}{" = "} {wTemp[count]} {"°"}' + "\n")
    count = count + 1
outputFile.write("============================================================="+ "\n")
outputFile.write(" "*16 + "Minumum Temp = " + format(min(wTemp) , "6.2f") + "°" + "\n")
outputFile.write(" "*16 + "Maximum Temp = " + format(max(wTemp) , "6.2f") + "°" + "\n")
outputFile.write(" "*16 + "Average Temp = " + format(average, "6.2f") + "°" + "\n")
outputFile.write("=============================================================" + "\n")


# Close file
outputFile.close()

# Program Output
print()
print("========================================================================" + "\n")
print(" The output will be written to " + fileName + " file on your computer." + "\n")
print("========================================================================" + "\n")


# End Program
