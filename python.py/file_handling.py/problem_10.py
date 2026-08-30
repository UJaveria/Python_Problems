# Write a function that returns file contents, or None (not a crash) if the file is missing — via
# try/except FileNotFoundError 
def file_content(filename) :
    try :
        with open(filename,"r") as file :
            content = file.read()
            return content
    except :
        return FileExistsError

print(file_content("jia_file.txt"))