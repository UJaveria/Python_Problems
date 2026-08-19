"""
Given three side lengths, determine if they can form a triangle 
(each side must be less than the sum of the other two)."""

side_a = int(input("Enter length of side_a : "))
side_b = int(input("Enter length of side_b : "))
side_c = int(input("Enter length of side_c : "))

flage = True
if (side_a < (side_b + side_c)) :
    flage = True
elif(side_b < (side_a + side_c)) :
    flage = True
elif(side_c < (side_a + side_b)) :
    flage = True
else :
    flage = False

if flage == True :
    print("These can form rectangle")
else :
    print("These cannot form the rectangle")