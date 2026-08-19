"""
Given a list with duplicate values, print a list with duplicates removed 
(hint: build a new list, only append if not already inside it 
— or convert to a set() and back, and compare the two approaches)."""


duplicate_list = [12,9,22,12,3,11,22,9,13,3,11,13]
print("Using loop ")
new_list = duplicate_list
for i in new_list:
    new_list.sort()
    new_list.remove(i)
print(new_list)

print("Using set() ")
# using set()
rem_duplicates = set(duplicate_list)
print(list(rem_duplicates))