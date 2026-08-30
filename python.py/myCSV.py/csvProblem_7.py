# Given a CSV of transactions (item, amount, type where  type is credit/debit), compute the final balance

import csv

total_credit = 0
total_debit  = 0
with open("data.csv","r") as file :
    reader = csv.reader(file)
    for i in reader :
        if i[2] == "credit" :
            total_credit += int(i[1])
        elif i[2] == "debit" :
            total_debit += int(i[1])


total_balance = total_credit - total_debit
print(f"Total balance : {total_balance}")