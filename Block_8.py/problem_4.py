"""
Given a year, determine if it's a leap year (divisible by 4, but not by 100 unless also by 400) — 
a good nested-condition exercise."""

year = int(input("Enter year : "))

if ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0) :
        print("Leap year")
else :
    print("Not a leap year")