# Read notes.txt and print its full contents.
with open("notes.txt","r") as file :
    output = file.read()
    print(output.strip())