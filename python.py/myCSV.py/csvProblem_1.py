# Create Question students.csv with a header row (name, age, grade ) and 2–3 data rows using the csv module
import csv

info = [
    ["Ali",21,"A"],
    ["Sara",18,"B"],
    ["Mani",23,"A"],
    ["Eddy",21,"C"]
]
try :
    with open("students.csv","w",newline="") as file :
        writer = csv.writer(file)
        writer.writerow(["name","age","grade"])
        for i in info :
            writer.writerow(i)
except Exception as e :
    print(e)