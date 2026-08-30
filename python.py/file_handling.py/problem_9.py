# Read a file, strip blank lines, and write the cleaned version to a new file.
with open("my_file.txt","r") as file :
    for line in file :
        if line == "\n" :
            continue
        else :
            with open("new_file.txt","a") as file :
                file.write(line)            
    