# Given a JSON file of products (name , price , stock ), return names of all products below a stock  threshold.
import json

info = [
    {"name": "Laptop", "price": 80000, "stock": 10},
    {"name": "Mouse", "price": 2000, "stock": 3},
    {"name": "Keyboard", "price": 5000, "stock": 7},
    {"name": "Headphones", "price": 4000, "stock": 2}
]

def low_stock(filename) :
    theresold = 5
    names = []
    with open(filename,"r") as file :
        data = json.load(file)
        for product in data :
            if product["stock"] < theresold :
                names.append(product["name"])
    return(names)

filename = "json_7.json"
print(low_stock(filename))