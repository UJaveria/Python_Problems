# Write power(base, exponent = 2)  a default parameter — and call it with and without the second
# argument

def power(base, exponent = 2) :
    return base ** exponent 

print(f"With default parameter : {power(2)}")
print(f"Without default parameter : {power(2,5)}")