#  Read a CSV of products and write a filtered CSV containing only rows below a given stock number

import csv


mylist = []
with open("csvdata.csv","r") as file :
    reader = csv.DictReader(file)
    for i in reader :
        if int(i["stock"]) < 15 :
            mylist.append(i)
with open("filterFile.csv","w",newline="") as myfile :
    writer = csv.writer(myfile)
    writer.writerow(["product","price","stock"])
    for i in mylist :
        writer.writerow(i)