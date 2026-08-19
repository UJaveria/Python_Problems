"""
Check whether a string is a valid-looking email by testing it contains "@" and "."
(not real validation — just a taste of string checks)."""
string = input("Enter string : ")
if "@" and "." in string :
    print("String is a valid-looking email.")
else :
    print("String is not a valid-looking email.")