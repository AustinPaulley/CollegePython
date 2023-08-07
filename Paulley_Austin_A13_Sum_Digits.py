
#===================================================================================================================
# Programmer: Austin Paulley
# Program Name: Assignment 13 
# Date: 4/18/2022
# Purpose: Creating Strings and Functions
#===================================================================================================================

#Create Main Function For the test test average program
def mainStringProgram():
    #===================================================================================================================
    # Initialize Processed Variables
    string1 = 0.0
    count = 0
    totalDigits = 0
    sum = 0
    #===================================================================================================================
    # Call function to create an output file to store results
    fileName, outFile = createoutFile() 
    #==================================================================================================================
    print("Enter a sequence of digits with nothing separating them: 892744688 (Press the enter key)")
    string1 = input()
    #==================================================================================================================
    #==================================================================================================================
    # Headings
    outFile.write("-" * 72 + "\n")
    outFile.write(" " *15 + "There are " + str(len(string1)) + " different numbers in the string." + "\n")
    outFile.write("-" * 72 + "\n")
    outFile.write(" " *34 + "They are" + "\n")
    outFile.write("-" * 72 + "\n")
    #==================================================================================================================
    #Make the List
    for x in (string1): 
        outFile.write(" " *38 + x + "\n")
    outFile.write("-" * 72 + "\n")
    #==================================================================================================================
    #Calculate the sum
    for x in (string1):
        sum+=int(x)
    outFile.write(" " *25 + "Sum of all digits entered = " + str(sum) + "\n")
    outFile.write("-" * 72 + "\n")
    #==================================================================================================================
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
#Call main Tempw Program function
mainStringProgram()
#===================================================================================================================   
    
