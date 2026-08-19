"""
Write a loop that asks the user to guess a fixed secret number, 
giving "too high"/"too low" feedback, and stops when they guess correctly."""
import random 
number = random.randint(1,100)

while True :
    guess = int(input("Enter a number : "))
    if guess > number :
        print("Too heigh")
    elif guess < number :
        print("Too low")
    else :
        print("Correct guess!")
        break
