# Check whether a file exists before reading it (os.path.exists or try/except).

import os
is_file_exist = os.path.exists("notes.txt")
print(is_file_exist)

if is_file_exist == True :
    with open("notes.txt","r") as file :
        text = file.read()
        print(text.strip())