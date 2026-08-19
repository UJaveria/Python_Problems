"""
Given a list of numbers, find and print the maximum and minimum without using max() / min() 
(loop through and compare manually) — then check your answer with max() / min() ."""

num_list = [11,93,49,56,38,25,56,13,34,1,44]

maximum = num_list[0]
minimum = num_list[0]
for val in num_list :
    if maximum < val :
        maximum = val
    if minimum > val :
        minimum = val
print("Maximum :",maximum)
print("Minimum :",minimum)