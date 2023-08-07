
#===================================================================================================================
# Programmer: Austin Paulley
# Program Name: Assignment 15 Gas Expenses List
# Date: 4/18/2022
# Purpose: Final Gas Expenses
#===================================================================================================================

#Create Main Function For the test test average program
def mainGasProgram():
    #===================================================================================================================
    # Initialize Processed Variables
    total=0.00          #Total Price of Gas
    average=0.0         #Average Price of Gas
    count=0             #Price of Gas
    maximum=0.00        #Maximum of Gas
    minimum=0.00        #Minimum of Gas
    totalFillUps=0      #Total Tank Fills
    fileName = ''       #File Name
    outFile = ''        #Out File
    gCount=0            #Function >95
    fCount=0            #Function <35
    hCount=0            #Function >30,<50
    iCount=0            #Function >50,<95

    #===================================================================================================================
    # Call function to create an output file to store results
    fileName, outFile = createoutFile()
    
    #==================================================================================================================
    # Define Gas Station Name
    print("Enter the name of the Gas Station you filled up at")
    stationName = input()
    
    #===================================================================================================================
    # define the size pr the list/array
    #Checking to make sure the correct data is collected
    print(" How many times did you fill up at " + stationName)
    totalFillUps = checkIntDataType(totalFillUps);#Call Function

    #===================================================================================================================
    #Start Lv
    gasExpenses = [0] * (totalFillUps)      #Original List
    gasExpensesG = [0] * (totalFillUps)     #Function >95
    gasExpensesF = [0] * (totalFillUps)     #Function <35
    gasExpensesH = [0] * (totalFillUps)     #Function >30,<50
    gasExpensesI = [0] * (totalFillUps)     #Function >50,<95
    count = 0

    #===================================================================================================================
    # use While loop to Create the Array list "name"
    createList(count, totalFillUps, stationName, gasExpenses)
    # Using fileinput.input() method

    #=========================================================================================================
    #calculate total or sum then the average
    total = sum(gasExpenses)
    average = total / totalFillUps

    #=========================================================================================================
    # Reset count to 0
    count = 0
    
    #=========================================================================================================
    # Unsorted heading
    outFile.write("============================================================="+ "\n")
    outFile.write("      Unsorted List of Gas Expenses at " + stationName + "\n")
    outFile.write("============================================================="+ "\n")

    #=========================================================================================================
    # File Use while loop to Create the Array/list "name"
    while count < totalFillUps:
        outFile.write(f'{" "*16} {"gasExpenses "}{str(count + 1)}{" = "}{"$"} {gasExpenses[count]} ' + "\n")
        count = count + 1
    bottomStats(outFile, gasExpenses, average)  #Call Function
    
    #==========================================================================================================
    #Call sort function
    gasExpenses.sort()
    
    #===================================================================================================================
    #Reset array
    count = 0
    
    #===================================================================================================================
    #Sort gasExpenses[count]
    outFile.write("============================================================="+ "\n")
    outFile.write("      Sorted List of Gas Expenses at " + stationName + "\n")
    outFile.write("============================================================="+ "\n")
    while count < totalFillUps:
        outFile.write(f'{" "*16} {"gasExpenses "}{str(count + 1)}{" = "}{"$"} {gasExpenses[count]} ' + "\n")
        count = count + 1
    bottomStats(outFile, gasExpenses, average)  #Call Function

    #===================================================================================================================
    #Temperatures Greater Than Or Equal To 75   
    determineGreaterOrEqualTo95(count, totalFillUps, gasExpenses, gasExpensesG) #Call Function
    writeGreaterOrEqualTo95(count, totalFillUps, gasExpensesG, gCount, outFile) #Call Function
    
    #===================================================================================================================
    #Functions Less then 35
    determineLessThan35(count, totalFillUps, gasExpenses, gasExpensesF) #Call Function
    writeLessThan35(count, totalFillUps, gasExpensesF, fCount, outFile) #Call Function
    
    #===================================================================================================================
    #Function Greater Than 35 Less Than 50
    determineGreaterThan35LessThan50(count, totalFillUps, gasExpenses, gasExpensesH)#Call Function
    writeGreaterThan35LessThan50(count, totalFillUps, gasExpensesH, hCount, outFile)#Call Function
    
    #===================================================================================================================
    #Function Greater Than 50 Less Than 95
    determineGreaterThan50LessThan95(count, totalFillUps, gasExpenses, gasExpensesI)#Call Function
    writeGreaterThan50LessThan95(count, totalFillUps, gasExpensesI, iCount, outFile)#Call Function
    
    #===================================================================================================================
    # Close file
    outFile.close()
    
    #===================================================================================================================
    # Program Output
    print()
    print("========================================================================" + "\n")
    print(" The output will be written to " + fileName + " file on your computer." + "\n")
    print("========================================================================" + "\n")
    #===================================================================================================================
    #End MainGasExpensesProgram Function
    
    #===================================================================================================================










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
#Call main Tempw Program function
mainGasProgram()

#===================================================================================================================

# End Program
