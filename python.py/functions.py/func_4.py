# Write describ_number(n) that returns (not prints) "positive","negative", or "zero"

def describe_number(n) :
    if n > 0 :
        return "positive"
    elif n < 0 :
        return "negative"
    else :
        return "zero" 

print(f"For Positive number : {describe_number(19)}")
print(f"For Negative number : {describe_number(-10)}")
print(f"For Zero number : {describe_number(0)}")