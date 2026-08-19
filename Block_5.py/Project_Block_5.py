"""
Small Project — Coordinate Distance Checker 
Store two points as tuples, 
e.g. point_a = (2, 3) and point_b = (7, 8) . 
Compute the distance between them using the distance formula ( ((x2-x1)**2 + (y2-y1)**2) ** 0.5 ) 
and print the result rounded to 2 decimal places. Let the user input both points as text and convert them."""
a = input("Enter x1 : ")
b = input("Enter y1 : ")
c = input("Enter x2 : ")
d = input("Enter y2 : ")

point_a = (int(a),int(b))
point_b = (int(c),int(d))

x1 , y1 = point_a
x2, y2 = point_b

distance = (((x2 - x1)**2 + (y2 - y1)**2) ** 0.5)
result = round((distance),2)
print(result)