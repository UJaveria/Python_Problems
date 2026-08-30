# Read notes.txt line by line, printing each with its line number.

with open("notes.txt","r") as file :
    for line in file :
        print(line.strip())