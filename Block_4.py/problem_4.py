"""
Given a list of numbers, print a new list containing only the even ones 
(a plain loop with .append() — list comprehensions come later)."""
num_list = [2,11,39,48,29,44,20,27,25,13]
even_list = []
for val in num_list :
    if val % 2 == 0 :
        even_list.append(val)

print(f"even_list : {even_list}")

