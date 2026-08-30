# Convert a dictionary (name,age,city) to a JSON string with (json.dumps()) and print it.
import json

info = {
    "name" : "Salman",
    "age"  : 28 ,
    "city" : "Chiniot"
}

json_data = json.dumps(info)
print(json_data)
print(type(json_data))