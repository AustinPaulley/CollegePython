# Programmer:Austin Paulley
# Program Name:Total Prices
# Date Made:1/30/22
# Purpose:Assignment 01
# Declaring Variables
#Initialize variables
afterTax = 0.0
beforeTax = 0.0
fileName =''
outFile = '' 
tax = 0.0
taxRate = 0.0
#Create File name where results will be stored (ask user for the file name)
fileName = input("Enter the file name where you wish to write the output/results\n")
outFile = open(fileName + " .txt", "w")

#Inputs

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
# Price 2
print("Enter 2nd Items Price")
while True:# This loop will check data for a number less then or equal to 0
    try:
        price2 = float(input())
    except ValueError:
        print("You entered the wrong data type\n" \
                "Re-enter a positive value [decimals are acceptable]")
        continue
    else:
        if (price2 < 0):
            print("You entered a value less then 0\n" \
                "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            break


# Price 3
print("Enter 3rd Items Price")
while True:# This loop will check data for a number less then or equal to 0
    try:
        price3 = float(input())
    except ValueError:
        print("You entered the wrong data type\n" \
                "Re-enter a positive value [decimals are acceptable]")
        continue
    else:
        if (price3 < 0):
            print("You entered a value less then 0\n" \
                "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            break


# Price 4
print("Enter 4th Items Price")
while True:# This loop will check data for a number less then or equal to 0
    try:
        price4 = float(input())
    except ValueError:
        print("You entered the wrong data type\n" \
                "Re-enter a positive value [decimals are acceptable]")
        continue
    else:
        if (price4 < 0):
            print("You entered a value less then 0\n" \
                "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            break


# Price 5
print("Enter 5th Items Price")
while True:# This loop will check data for a number less then or equal to 0
    try:
        price5 = float(input())
    except ValueError:
        print("You entered the wrong data type\n" \
                "Re-enter a positive value [decimals are acceptable]")
        continue
    else:
        if (price5 < 0):
            print("You entered a value less then 0\n" \
                "Re-enter a positive value [decimals are acceptable]")
            continue
        else:
            break


#Tax Rate=======================================================================

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


# Math
beforeTax = price1 + price2 + price3 + price4 + price5
tax = beforeTax * taxRate
afterTax = beforeTax + tax

# Outputs
outFile.write("=======================================================" + "\n")
outFile.write("                Total Purchase Receipt" + "\n")
outFile.write("=======================================================" + "\n")
outFile.write(f'{"Price 1 = ":30s}{" ":10s}{"$":2s}{price1:12,.2f}' + "\n")
outFile.write(f'{"Price 2 = ":30s}{" ":10s}{"$":2s}{price2:12,.2f}' + "\n")
outFile.write(f'{"Price 3 = ":30s}{" ":10s}{"$":2s}{price3:12,.2f}' + "\n")
outFile.write(f'{"Price 4 = ":30s}{" ":10s}{"$":2s}{price4:12,.2f}' + "\n")
outFile.write(f'{"Price 5 = ":30s}{" ":10s}{"$":2s}{price5:12,.2f}' + "\n")
outFile.write("=======================================================" + "\n")
outFile.write(f'{"Before Tax = ":30s}{" ":10s}{"$":2s}{beforeTax:12,.2f}' + "\n")
outFile.write(f'{"Tax = ":30s}{" ":10s}{"$":2s}{tax:12,.2f}' + "\n")
outFile.write(f'{"After Tax = ":30s}{" ":10s}{"$":2s}{afterTax:12,.2f}' + "\n")
outFile.write("=======================================================" + "\n")

#Close newly formed external file where output will be written
outFile.close()
#End Program
