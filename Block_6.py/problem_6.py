"""
Given a dictionary of item names to prices, 
find and print the most expensive item (loop through .items() and track the max)."""

item_list = {
    "pizza" : 2300,
    "juice" : 300,
    "cake"  : 1200,
    "Rsalad" : 1000
}

for key, value in item_list.items() :
    exp = max(item_list)
    expensive = item_list[exp]

print("Expensive item\n",exp,":",expensive)
