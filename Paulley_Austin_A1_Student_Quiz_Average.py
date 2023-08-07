def toFixed(value, digits):
    return "%.*f" % (digits, value)

# PROGRAMMER:  your first and last name
# PROGRAM NAME: Quiz Average
# DATE WRITTEN: May 16, 2021
# PURPOSE: Use Input, Assignment, Output statements to calculate the average of 5 quizzes for 5 different students.
# Declare variables in alpha order
# Initialize variables used to store calculations or results
average = 0.0
total = 0.0

# Input Operations
print("Enter the name of Student #1")
stuName1 = input()
print("Enter quiz #1 for " + stuName1)
quiz1 = float(input())
print("Enter the name of Student #2")
stuName2 = input()
print("Enter the quiz #2 for " + stuName2)
quiz2 = float(input())
print("Enter the name of Student #3")
stuName3 = input()
print("Enter quiz #3 for " + stuName3)
quiz3 = float(input())
print("Enter the name of Student #4")
stuName4 = input()
print("Enter the quiz #4 for " + stuName4)
quiz4 = float(input())
print("Enter the name of Student #5")
stuName5 = input()
print("Enter the quiz #5 for " + stuName5)
quiz5 = float(input())

# Calculate Total of Quizzes
total = quiz1 + quiz2 + quiz3 + quiz4 + quiz5

# Calculate Average of Quizzes
average = total / 5

# OUTPUT OPERATIONS
# REPORT HEADING AND COLUMN HEADINGS
print("=======================================================")
print("                STUDENT QUIZZES")
print("=======================================================")
print("STUDENT NAME                   QUZZES")
print("=======================================================")

# STUDENT NAMES AND QUIZ GRADES
print(format(stuName1, "25s") + " " + format(quiz1, "6.2f"))
print(format(stuName2, "25s") + " " + format(quiz2, "6.2f"))
print(format(stuName3, "25s") + " " + format(quiz3, "6.2f"))
print(format(stuName4, "25s") + " " + format(quiz4, "6.2f"))
print(format(stuName5, "25s") + " " + format(quiz5, "6.2f"))
print("=======================================================")

# Total / sum of Quizzes
print("Total of the quizzes = " + toFixed(total,2))
print("=======================================================")

# Quiz Average
print("QUIZ AVERAGE = " + toFixed(average,2) + "%")
print("=======================================================")

# END PROGRAM

print(format(stuName1, "25s") + " " + format(quiz1, "6.2f"))


