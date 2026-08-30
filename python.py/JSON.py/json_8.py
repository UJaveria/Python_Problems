#Load a JSON file safely — return an empty list if the file doesn't exist yet (the "first run" pattern).

import json 

def find_file(filename) :
    try : 
        with open(filename,"r") as file :
            data = json.load(file)
            return data
    except :
        return []
    
filename = input("Enter file name : ")
print(find_file(filename))