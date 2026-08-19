"""
Given a messy string with inconsistent spacing ( "  Hello   World  " ), 
clean it to exactly "Hello World" using .strip() and .split() / .join() ."""

string = "  Hello   World  "
s = string.strip().split()
print(" ".join(s))
