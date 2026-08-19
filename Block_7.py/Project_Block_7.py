"""
Small Project — Number Guessing Game 
The program picks a fixed number (or use a hardcoded one for now — random comes later). 
The user guesses in a while loop that continues until correct, printing "too high" or "too low" each time,
 and finally reports how many guesses it took."""

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
