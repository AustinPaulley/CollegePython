def toFixed (value, digits):
    return "%.*f" % (digits, value)

# =======================================================================

# PROGRAMMER: AUSTIN PAULLEY
# PROGRAM NAME: Calculate Feet to Inches Assignment#9
# Date Witten: 4/4/2022
# Calculate Feet to Inches using Functions

# =======================================================================
# Declare Vairables
# Initialize processed variable
totalInches = 0.0

# =======================================================================
# Create a file to write the output

fileName = input("Enter the file name to write the output\n"\
                 "type \"txt\" at the end of the file name\n")

outputFile = open(fileName, "w")
# =======================================================================
# Input Operations
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
                    


# =======================================================================
# Calculations
totalInches = feet * 12

# =======================================================================
# File Output Operation
outputFile.write("====================================" + "\n")
outputFile.write("  Converting Feet To Inches" + "\n")
outputFile.write("====================================" + "\n")
outputFile.write((format(feet, "10,.2f") + " feet = ") + format(totalInches, "10,.2f") + " inches" + "\n")
outputFile.write("====================================")

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
