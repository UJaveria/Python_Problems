"""
. Write a function that returns a tuple of (minimum, maximum, average) for a list of numbers, 
then unpack the result into three variables when calling it."""

def checker (num_list) :
    maximum = max(num_list)
    minimum = min(num_list)
    average = sum(num_list) / len(num_list)
    my_list = []
    my_list.append(maximum)
    my_list.append(minimum)
    my_list.append(average)
    my_tup = tuple(my_list)
    return my_tup

my_list = [1,2,3,4,5]
maximum , minimum , average = checker(my_list)
print("Maximum :",maximum)
print("Minimum :",minimum)
print("Average :",average)