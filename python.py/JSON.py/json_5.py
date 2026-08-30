# Save a list of dictionaries (student records) to a JSON file, then load and print each one.

import json

students = [
    {
        "name": "Ali",
        "age": 20,
        "roll_no": 101,
        "marks": 85
    },
    {
        "name": "Sara",
        "age": 21,
        "roll_no": 102,
        "marks": 92
    },
    {
        "name": "Ahmed",
        "age": 19,
        "roll_no": 103,
        "marks": 78
    },
    {
        "name": "Ayesha",
        "age": 20,
        "roll_no": 104,
        "marks": 88
    }
]

with open("json_5.json","w") as file :
    json.dump(students,file,indent=4)

with open("json_5.json","r") as file :
    data = json.load(file)
    print(data)
    print(type(data))