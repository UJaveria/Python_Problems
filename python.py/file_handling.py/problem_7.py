#  Read a text file and count total words and total lines.

with open("my_file.txt","r") as file :
    total_words = 0
    total_lines = 0
    for line in file :
        line = line.strip()
        total_words += len(line.split())
        total_lines += 1
print(f"Total lines: {total_lines}")
print(f"Total words: {total_words}")