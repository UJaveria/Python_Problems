"""
Given a day number (1–7), print the day name using if/elif — 
then challenge: rewrite it using a dictionary lookup instead, and compare which is cleaner."""

day_num = int(input("Enter day number from 1-7 : "))

# using if/else
if day_num == 1 :
    print("Monday")
elif day_num == 2 :
    print("Tuesday")
elif day_num == 3 :
    print("Wednesday")
elif day_num == 4 :
    print("Thursday")
elif day_num == 5 :
    print("Friday")
elif day_num == 6 :
    print("Saturday")
elif day_num == 7 :
    print("Sunday")
else :
    print("Enter valid number")


# Using dictionary 
days_dict = {
    1 : "Monday" ,
    2 : "Tuesday",
    3 : "Wednesday",
    4 : "Thursday" ,
    5 : "Friday" ,
    6 : "Saturday" ,
    7 : "Sunday"
}

day_num = int(input("Enter day number from 1-7 : "))

for key, val in days_dict.items() :
    if key == day_num :
        print(key,":",val)

# Dictionary is cleaner