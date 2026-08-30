# Write a dictionary to a file with json.dump() , then read it back with json.load() .

import json

info = {
    "name" : "Salman",
    "age"  : 28 ,
    "city" : "Chiniot"
}

with open("json_3.json","w") as file :
    json.dump(info,file,indent=4)


with open("json_3.json","r") as file :
    data = json.load(file)
    print(data)