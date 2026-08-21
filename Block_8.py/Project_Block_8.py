"""
Small Project — Simple Grading & Feedback System 
Given a score (0–100), print a letter grade (A–F using standard cutoffs) 
AND a onesentence feedback message that differs by grade 
(e.g., A → "Excellent work!", F → "Let's set up extra practice time."). 
Handle invalid input (negative numbers or over 100) with its own message"""

score = int(input("Enter a score(1-100) : "))

if score <= 100 and score >= 0:
    if  score >= 90  :
        print("A")
        print("Excellent work!")
    elif score >= 70 :
        print("B")
        print("V.Good work!")
    elif score >= 50 :
        print("C")
        print("Good work!")
    elif score >= 30 :
        print("D")
        print("Poor work!")
    else :
        print("F")
        print("Let's set up extra practice time.")
else :
    print("Invalid input")