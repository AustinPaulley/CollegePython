import random

random.seed()   #Prepare random number generator

# PROGRAMMER: Austin Paulley
# PROGRAM: Guess the number
# WRITTEN:3/1/22
# PUPOSE: Use while loop to guess a number with a built in rnadom number generator function.
# Declare Intergers
# Creating While Loop to make program repeat
print("Do you wish to play the [Guess the number game]?[Type 'y' or 'Y' for yes otherwise type no to exit the program")
answer = input()
while answer == "y" or answer == "Y":
    
    # Create a Random Number
    number = int(random.random() * 101)
    
    # Output statement to provide directions to user
    print("Guess a number, any number between 0 and 100")
    guess = -1
    count = 0
    while guess != number:
        count = count + 1
        print(" Enter your guess [Positve whole numbers only]")
        guess = int(input())
        if guess == number:
            print("You Guessed the correct number ==> " + format(guess, "d"))
            print("your number of guesses ==> " + format(count, "d"))
            if count < 5:
                print("You are winner, guessing the correct number in " + format(count, "d"))
            print("Do you wish to play the [Guess the number game again]?[Type 'y' or 'Y' for yes otherwise type no to exit the program")
            answer = input()
        else:
            if guess > number:
                print("Your guess of " + format(guess, "d") + " is too high")
            else:
                print("Your guess of " + format(guess, "d") + " is too low")
print("THANKS FOR PLAYING THE GUESS THE NUMBER GAME – HAVE A NICE DAY")
print("Programmed By Austin Paulley")
