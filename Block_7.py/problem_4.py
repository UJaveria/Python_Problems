"""
Nested loop: print a 5x5 grid of * characters using two for loops."""

for row in range(1,6) :
    for col in range(1,6) :
        print("* ",end="")
    print()