# Read a CSV of (name, score ) and compute the average score — remember, values arrive as strings.
import csv

total_score = 0
num = 0
with open("mycsv.csv","r") as file :
    reader = csv.DictReader(file)
    for i in reader :
        total_score += int(i["score"])
        num += 1
avg = total_score / num
print(round((avg),2))