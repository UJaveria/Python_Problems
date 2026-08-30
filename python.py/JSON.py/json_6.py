# Write add_record(filename, record) — loads existing data, appends the new record, saves it back
# (no data loss).

import json

def add_record(filename, record) :
    try :
        with open(filename,"r") as file :
            data = json.load(file)
            print(data)
        with open(filename, "w") as file :
            json.dump(record,file,indent=4)
    except :
        print("FileNotFoundError")


    
filename = "json_5.json"
record = students = [
    {
        "name": "Hamza",
        "roll_no": 201,
        "department": "CS",
        "semester": 4,
        "gpa": 3.45
    },
    {
        "name": "Maham",
        "roll_no": 202,
        "department": "SE",
        "semester": 3,
        "gpa": 3.78
    },
    {
        "name": "Usman",
        "roll_no": 203,
        "department": "IT",
        "semester": 5,
        "gpa": 3.12
    },
    {
        "name": "Hira",
        "roll_no": 204,
        "department": "CS",
        "semester": 2,
        "gpa": 3.91
    }
]
add_record(filename,record)