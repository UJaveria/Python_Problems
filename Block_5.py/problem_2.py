"""
. Try to change one value in a tuple directly ( point[0] = 5 ) and read the error 
— explain in one sentence why tuples don't allow this."""
my_tup = (1,2,3,4,5)
my_tup[0] = 5
print(my_tup)
# Because tuple does not support item assignment i.e tuples are immutable -> can't be changed