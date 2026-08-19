"""
Reverse a list two ways: using .reverse() and using slicing ( [::-1] ) — 
confirm both give the same result."""

num_list_1 = [1,2,3,4,5,6]
# List reversing using .reverse()
num_list_1.reverse()
print(num_list_1)

num_list_2 = [1,2,3,4,5,6]
# List reversing using slicing
rev = num_list_2[::-1]
print(rev)

if num_list_1 == rev:
    print("Both reversed lists are same.")
else :
    print("Both reversed lists are Not same.")