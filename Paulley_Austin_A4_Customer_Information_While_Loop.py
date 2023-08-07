def toFixed(value, digits):
    return "%.*f" % (digits, value)
#==============================================================================
# PROGRAMMER:    Austin Paulley
# PROGRAM NAME:  Customer Information Program using a While Loop
# DATE WRITTEN:  2/23/22
# PURPOSE:       DEMONSTRATE BASIC WHILE LOOP CONCEPT
#==============================================================================
# Declare variables in alpha order
#==============================================================================
# answer is the lcv
# While LOOP
# 1) programmer must decide on the lcv name or identifier
# 2) lcv must be initialized
# 3) lcv must be tested
# 4) lcv must be updated inside the WHILE LOOP
#==============================================================================
# Initialize variable(s) where calculated results are stored.
averagePurchase = 0.0
count = 0
totalAmount = 0.0
#==============================================================================
# Main Column Heading
print("==============================================================")
print("CUSTOMER PURCHASE INFORMATION")
print("==============================================================")
#==============================================================================
# Sub Column Heading
print("CUSTOMER NAME                       PURCHASE AMOUNT")
print("==============================================================")
#==============================================================================
# Initialize lcv "answer"
print("Do you wish to process a customer's information? [type 'y' or 'Y' otherwise enter 'no'] ")
answer = input()
#==============================================================================
# Display a blank line
print(" ")
#==============================================================================
# While Loop
# testing the lcv To enter more than one customer name and purchase amount
while (answer == "y") or (answer == "Y"):
    
    # Input Operations
    print("Enter Customer's name ")
    customerName = input()
    print("How much did the customer spend on this item? ")
    purchaseAmount = float(input())
    
    # keep a running total of the purchase amounts per customer
    totalAmount = totalAmount + purchaseAmount
    
    # count or tally the number of customers / purchases
    count = count + 1
    
    # Output each customer name and their purchase amount as a column
    print(f'{customerName:30s}{" ":10s}{"2":2s}{purchaseAmount:12,.2f}')
    
    # update lcv answer
    print("Do you wish to process a customer's information? [type 'y' or 'Y' otherwise enter 'no'] ")
    answer = input()
    print(" ")
    
    # end while loop
# calculate the average purchase amount
averagePurchase = totalAmount / count

# Output operations
print("==========================================================================================")

# Displays the total amount of purchases for all the customers
print(f'{"Customer Total Purchases = ":30s}{" ":10s}{"$":2s}{totalAmount:12,.2f}')
print("==========================================================================================")

# Displays the Average of purchases for all the customers
print(f'{"The Average Purcase Price = ":30s}{" ":10s}{"$":2s}{averagePurchase:12,.2f}')
print("==========================================================================================")
print("THIS PROGRAM IS COMPLETE - EDITED BY AUSTIN PAULLEY")
print("==========================================================================================")
#==============================================================================
# END PROGRAM
