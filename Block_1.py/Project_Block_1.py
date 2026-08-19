"""Small Project — Unit Price Calculator 
Store an item's total price and quantity in variables. 
Compute and print the price per unit, formatted to 2 decimal places. 
Then let the user override the quantity via input() and recompute"""

total_price = float(input("Enter total price : "))
quantity = int(input("Enter quantity of item : "))
price_per_unit = total_price / quantity
print(round((price_per_unit),2))