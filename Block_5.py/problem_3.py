"""
Given a list of (name, score) tuples, loop through and print each as "name: score"."""
my_list = [("name","score")]
for val in my_list :
    for i in list(val) :
        print(f"{i}:",end=" ")
