"""
Create a dictionary describing yourself (name, age, city, hobby). Print each value by key."""
my_info = {
    "name"  : "Javeria",
    "age"   : 21 ,
    "city"  : "Chiniot" ,
    "hobby" : "codding"
}

# printing values by keys
print(my_info["name"])
print(my_info["age"])
print(my_info["city"])
print(my_info["hobby"])

print()
# printing values key value method
for key in my_info :
    print(key, ":",my_info[key])