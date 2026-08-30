# Write save_list(filename, items) and load_list(filename) to persist a list of strings, one per line.

def save_list(filename, items) :
    with open(filename,"w") as file :
        for item in items :
            file.write(item)
            file.write("\n")


def load_list(filename) :
    items = []
    with open(filename, "r") as file :
        for line in file :
            items.append(line.strip("\n"))
    print(items)


items = ["Ali", "Sara", "Ahmed"]
filename = "names.txt"
save_list(filename, items)
load_list(filename)