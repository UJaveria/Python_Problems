"""
Small Project — Username Generator 
Take a person's first name and last name as input. 
Generate three username suggestions: firstname_lastname (lowercase), 
first initial + lastname, and lastname + last 2 digits of a given "birth year" input. 
Print all three, formatted cleanly."""

first_name = input("Enter your first name : ")
last_name = input("Enter your last name : ")
birth_year = input("Enter your birth year : ")

# Suggestion 1
firstname_lastname = first_name.lower().strip() + last_name.lower()
print(firstname_lastname)

# Suggestion 2
First_last_name = first_name.capitalize().strip() + last_name.capitalize()
print(First_last_name)

# Suggestion 3
last_dig_name = last_name.lower().strip() + birth_year[2:]
print(last_dig_name)