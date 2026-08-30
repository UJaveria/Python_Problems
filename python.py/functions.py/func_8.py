# Write validate_password(password) returning (is_valid, reason)— length, digit, uppercase —
# reason = first rule failed.

import re
def validate_password(password) :
    length = len(password)
    is_digit = bool(re.findall(("[0-9]+"),password))
    is_uppercase = bool(re.findall(("[A-Z]+"),password))
    reason = None
    is_valid = False
    if length >= 8 and is_digit == True and is_uppercase == True :
        is_valid = True
    else : 
        if length >= 8 :
            if is_digit == False :
                reason = "No digit"
            elif is_uppercase == False :
                reason = "No uppercase"
        else :
            reason = "Length"
    return(is_valid,reason)

password = input("Enter password : ").strip()
is_valid , reason  = validate_password(password)
print(f"is_valid = {is_valid}\nreason = {reason}")