"""
Loop through a list of numbers and use break to stop as soon as a negative number is found, 
printing "Found a negative!" and the value."""

num_list = [12,38,43,28,19,-3,47,9,4]

for i in num_list :
    if i < 0 :
        print("Found a negative!",i)
        break
else :
    print("Not found")