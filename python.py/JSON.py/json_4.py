# Given a nested dictionary (e.g. an "address" sub-dict), dump it to JSON with indent=4 for readability.

import json

info = {
    "name" : "Salman",
    "age"  : 28 ,
    "address" : {"by_road" : "Lahore road Chiniot"},
    "city" : "Chiniot"
}

with open("json_4.json", "w") as file :
    json.dump(info["address"],file, indent=4)