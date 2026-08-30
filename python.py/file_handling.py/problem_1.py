# Write three lines to notes.txt using with open(...).

with open("notes.txt","w") as file :
    text = "Python is heigher level language.\nIt is easy to learn.\nIts commonly used in Artifical Intelligence.\n"
    file.write(text)
