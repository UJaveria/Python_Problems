# Write is_adult(age) that returns True/False based on wether age >= 18.

def is_adult(age) :
    if age > 0 :
        if age >= 18 :
            return True
        else :
            return False
    else :
        return "Invalid age"



print(is_adult(19))