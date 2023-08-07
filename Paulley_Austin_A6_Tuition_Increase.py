# PROGRAMMER: Austin Paulley
# PROGRAM NAME: Calculating College Intrest
# DATE: 3/6/22
# PURPOSE: To Learn the For Loop
# ==================================================
# Define Variable and data type
# ==================================================
# ==================================================
# Initialize Variables
count = 0
intrest = 0

# ==================================================
# Input Variables
print("What is the starting amount of tuition?")
tuition = float(input())
print("How many years are you in college")
years = int(input())
print("Enter the intrest as a decimal, For example 3% is 0.03")
intrest = float(input())

# ==================================================
# Titles
print("==================================================")
print("Projected Tuitions (Per Semester)")
print("==================================================")
print("        Year         Projected Tuition")

# ==================================================
# For Loop to calculate tuition
# ==================================================
for count in range(1, years + 1, 1):
    tuition = tuition * intrest + tuition
    print(f'{count:12,.0f}{" ":10s}{"$":2s}{tuition:12,.2f}')
# ==================================================
# Make intrest a whole number
intrest = intrest * 100
print("==================================================")
print("This was calculated with a intrest at % " + str(intrest))
print("==================================================")
print("PROGRAMMED BY: AUSTIN PAULLEY")
#===================================================
# End Program
