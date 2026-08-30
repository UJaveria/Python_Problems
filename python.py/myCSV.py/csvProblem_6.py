# Write csv_to_dicts(filename) — your own version of DictReader to see what's happening underneath.

import csv

def csv_to_dicts(filename) :
    with open(filename,"r") as file :
        reader = csv.DictReader(file)
        for i in reader :
            print(i)

filename = "mycsv.csv"
csv_to_dicts(filename)