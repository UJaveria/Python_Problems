"""
Create a dictionary where each key maps to a list 
(e.g., {"fruits": ["apple", "banana"], "veggies": ["carrot"]} ), 
and write code to add a new item to one of the lists."""

item_dic = {"fruits": ["apple", "banana"], "veggies": ["carrot"]}
veg = input("Enter veggies : ")
item_dic["veggies"] = ["carrot",veg]
print(item_dic)