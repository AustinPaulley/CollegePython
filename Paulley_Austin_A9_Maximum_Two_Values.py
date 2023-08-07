def toFixed (value, digits):
    return "%.*f" % (digits, value)

# =======================================================================

# PROGRAMMER: AUSTIN PAULLEY
# PROGRAM NAME: Maximum of Two interger values Assignment#9
# Date Witten: 4/4/2022
# Lable Maximum of Two interger values

# =======================================================================
# Declare Vairables
# Initialize processed variable
maximumValue = 0.0

# =======================================================================
# Create a file to write the output

fileName = input("Enter the file name to write the output\n"\
                 "type \"txt\" at the end of the file name\n")

outputFile = open(fileName, "w")
# =======================================================================
# Input Operations
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
        print("Wrong data type entered - Re-Enter Positive value")
        continue
    else:
        if (interger2 <= 0):
            print("You entered a negative value -Re-Enter a Positve Value\n")
            continue
        else:
            break
        
# =======================================================================
# Calculations
maximumValue = max(interger1,interger2)

# =======================================================================
# File Output Operation
outputFile.write("=====================================================" + "\n")
outputFile.write("             Maximum Of Two Values        " + "\n")
outputFile.write("=====================================================" + "\n")
outputFile.write((" The maximum of " + format(interger1, "1,.2f") + " and ") + format(interger2, "1,.2f") + " is " + format(maximumValue, "1,.2f") + "\n")
outputFile.write("=====================================================")
# =======================================================================
# Close file
outputFile.close()

# =======================================================================
# Program Output
print()
print("========================================================================")
print(" The output will be written to " + fileName + " file on your computer.")
print("========================================================================")

# =======================================================================

#END PROGRAM
