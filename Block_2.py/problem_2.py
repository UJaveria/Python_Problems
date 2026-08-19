"""Convert a string "42" to an int, add 8, 
and print the result — and prove it broke before you converted it."""

val = "42"
result = int(val) + 8
print(result)
print()
# To prove it broke before I converted it
print("Without converting it will broke")
try :
    result = val + 8
    print(result)
except :
    print("TypeError: can only concatenate str (not 'int') to str")