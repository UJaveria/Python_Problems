# Write stats(numbers) returning a tuple (minimum, maximum, average)  Unpack all three on call.

def stats(numbers) :
    maximum = numbers[0]
    minimum = numbers[0]
    add_num = 0
    for num in numbers :
        add_num += num
        if num > maximum :
            maximum = num 
        elif num < minimum :
            minimum = num
    average = add_num / len(numbers)
    return (maximum, minimum, average)

numbers = [21,94,44,23,11,80]
maximum, minimum, average = stats(numbers)
print(f"Maximum : {maximum}")
print(f"Minimum : {minimum}")
print(f"Average : {average}")