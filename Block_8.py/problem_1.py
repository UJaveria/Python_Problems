"""
Write a program that categorizes a number as negative, zero, or positive."""
number = int(input("Enter a number : "))
if number > 0 :
    print(f"Positive")
elif number < 0 :
    print("Negative")
else :
    print("Zero")