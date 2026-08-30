"""
Write apply_twice(func, value) that calls func on value twice (e.g. apply_twice(square, 3) →81 ). 
Functions as values"""

def apply_twice(func, value) :
        print((func(value)) * (func(value)))

def square(n) :
    return (n * n)

value = 3
apply_twice(square,value)