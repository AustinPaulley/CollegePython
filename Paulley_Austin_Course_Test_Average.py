def toFixed(value, digits):
    return "%.*f" % (digits, value)
#============================================================
# Programmer:       Austin Paulley
# Program Name:     Calculating Average Test Scores
# Date Written:     2/23/22
# Purpose:          Showing While Loop Skills
#============================================================
# declare variables in alpha order
# answer is the lcv
# initialize variables
averageClassGrade = 0.0
count = 0
totalTestGrades = 0.0
#============================================================
# Main Column Headings
print("========================================================")
print("Test Information")
print("========================================================")
print("Student Name and Grade of Test")
print("========================================================")
#============================================================
# Initialize lcv "awnser"
print("Do you wish to add a test? {type 'y' or 'Y' otherwise enter 'no'}")
answer = input()
print("  ")
#============================================================
# While Loop
# testing the lcv To enter more than one customer name and purchase amount
while answer == "y" or answer == "Y":
    
    # Input Operations
    print("Enter Students Name ")
    studentName = input()
    print("What was their test score")
    testScore = float(input())
    
    # running total of test scores
    totalTestGrades = totalTestGrades + testScore
    
    # Number of test
    count = count + 1
    
    # Output customer name and their test score
    print(studentName + "                        " + "%" + toFixed(testScore,2))
    
    # update lcv answer
    print("Do you wish to process a students's information? [type 'y' or 'Y' otherwise enter 'no'] ")
    answer = input()
    print("  ")
    
    # end while loop
averageClassGrade = totalTestGrades / count
#============================================================
# Output Operations
print("========================================================")

# Displays the total amount of test for all the students
print(f'{"Students Total Test Scores = ":30s}{" ":10s}{"%":2s}{totalTestGrades:12,.2f}')
print("========================================================")

# Displays the Average Test Scores of all Students
print(f'{"The average test score = ":30s}{" ":10s}{"%":2s}{averageClassGrade:12,.2f}')
print("========================================================")
#============================================================
if averageClassGrade >= 90 and averageClassGrade <= 100:
    print("Excellent Class Average")
else:
    if averageClassGrade >= 80 and averageClassGrade <= 89.99:
        print("Good Class Average")
    else:
        if averageClassGrade >= 70 and averageClassGrade <= 79.99:
            print("Satisfactory Class Average")
        else:
            if averageClassGrade <= 60:
                print("Unsatisfactory Class Average")
#============================================================
print("========================================================")
print("THIS PROGRAM IS COMPLETE - BY AUSTIN PAULLEY")
print("========================================================")

# End Program
