"""
Small Project - Type-Safe age checker
Ask the user for their birth year as text input. Convert it to an int, 
compute their age (assume current year is fixed in a variable), 
and print whether they are a minor, an adult, or a senior — 
printing the age's type at each step so the conversions are visible."""

birth_year = input("Enter your birth year : ")
b_year = int(birth_year)
current_year = 2026
age = current_year - b_year

if b_year <= current_year :
    if age < 18 :
        print(f"You are of {age}.So you are minor.")
    elif age < 60 :
        print(f"You are of {age}.So you are an adult.")
    else :
        print(f"You are of {age}.So you are senior.")
else :
    print("Enter valid year")

