"""
Build a simple Mad Libs: ask for a noun, a verb, and an adjective via input, 
then insert them into a fixed sentence template using an f-string."""

noun = input("Enter a noun : ")
verb = input("Enter a verb : ")
adjective = input("Enter an adjective : ")
print(f"{noun}, who is {adjective}, is {verb}.")