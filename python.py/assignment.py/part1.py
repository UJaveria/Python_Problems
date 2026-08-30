sales_amount = []
total_sales = 0
for emp in range(1,6) :
    amount = float(input("Enter amount : "))
    sales_amount.append(amount)
    total_sales += amount
print("------Total Sales------")
print(f"Total Sales : {total_sales}")
# Average sale 
print("------Average Sales------")
average_sale = total_sales / len(sales_amount)
print(f"Average Sale : {average_sale}")

# Calculating tax
if total_sales > 100000 :
    tax = (15 / 100)
elif total_sales >= 50000 :
    tax = (10 / 100)
else : 
    tax = (5 / 100)
# Sale amount and Tax amount
for amount in sales_amount :
    print(f"Sale amount : {amount}, Tax amount : {amount * tax}")