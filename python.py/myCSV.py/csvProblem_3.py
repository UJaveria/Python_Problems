# Read students.csv with csv.DictReader and print each row as a dictionary.
import csv
with open("students.csv","r") as file :
    reader = csv.DictReader(file) 
    for row in reader :
        print(row)