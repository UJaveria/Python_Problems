# Append a new row to students.csv without erasing existing rows.

import csv

info = ["Mia",19,"B"]
with open("students.csv","a") as file :
    writer = csv.writer(file)
    writer.writerow(info)