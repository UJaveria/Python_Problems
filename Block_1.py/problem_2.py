"""Swap the values of two variables a and b without a third helper variable (hint: a, b = b, a )."""
a = int(input("Enter number_a : "))
b = int(input("Enter number_b : "))
a,b = b, a
print("a :",a)
print("b :",b)