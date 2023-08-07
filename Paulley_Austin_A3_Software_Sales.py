def toFixed(value, digits):
    return "%.*f" % (digits, value)

# Austin Paulley, If statments, 2/15/22
# Variables
# Calculation
discountAmount = 0.00#Calculations
softwarePurchaseAmount = 0.00
totalAmount = 0.00

# Inputs
print("What is the Retail Cost Per Software Package?")
priceSoftware = float(input())
print("What is The Quanity/Number of Packages Purchased?")
quantity = int(input())
print("")
print("====================================================")
print("The Retail Cost of the Software Package=$" + toFixed(priceSoftware,2))
print("The Quanity/Number of Packages Purchased=" + str(quantity))
print("====================================================")
if quantity < 10:#If Statements
    discountRate = 0.00
else:
    if quantity >= 10 and quantity <= 19:
        discountRate = 0.10
    else:
        if quantity >= 20 and quantity <= 49:
            discountRate = 0.20
        else:
            if quantity >= 50 and quantity <= 99:
                discountRate = 0.30
            else:
                if quantity >= 100:
                    discountRate = 0.40
    
    # Finding Discount Amount
    discountAmount = discountRate * quantity * priceSoftware
    
    # Calculation original amount of Software Purchases
    softwarePurchaseAmount = quantity * priceSoftware
    
    # Calculate the total amount of software purchase after the discount
    totalAmount = softwarePurchaseAmount - discountAmount
    
    # Output Results
    print("====================================================")
    print("               The Discount Precent Rate=" + toFixed(discountRate * 100,2) + "%")
    print("             Calculation Discount Rate=$" + toFixed(discountAmount,2))
    print("          Total Price Before Discount=$" + toFixed(softwarePurchaseAmount,2))
    print("          Total Amount After Discount=$" + toFixed(totalAmount,2))
    print("====================================================")
    # End Program
