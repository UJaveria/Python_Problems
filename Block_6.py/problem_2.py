"""
Add a new key-value pair, update an existing value, and delete one key 
— print the dictionary after each step."""

my_info = {
    "name"  : "Javeria",
    "age"   : 21 ,
    "city"  : "Chiniot" ,
    "hobby" : "codding"
}

# Adding a new key-value pair
# Method 1
my_info["Program"] = "BSCS"
print(my_info)
print()

# Updating an existing value
my_info.update({"hobby":"Painting"})
print(my_info)
print()
# Deleting one key
my_info.pop("name")
print(my_info)