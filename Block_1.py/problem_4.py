"""Write a program that stores a rectangle's width and height in variables, 
then computes and prints its area and perimeter."""
rect_width = float(input("Enter rectangle's width : "))
rect_height = float(input("Enter rectangle's height : "))
rect_area = rect_width * rect_height
rect_perimeter = 2 * (rect_width + rect_height)
print("Rectangle's area :",rect_area)
print("Rectangle's perimeter : ",rect_perimeter)