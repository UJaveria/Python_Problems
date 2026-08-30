# Write apply_discount(price, percent=10) then final_bill(prices, percent=10)  that calls it in a
# loop and returns the total.

def apply_discount(price, percent= 10) :
    discount = price * (percent / 100)
    return (price - discount)

def final_bill(prices, percent=10):
    total = 0
    for price in prices :
        total += apply_discount(price)
    return total

prices = [100, 200, 500] 
print(final_bill(prices))