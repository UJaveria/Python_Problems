# Append a new line to notes.txt without erasing existing content (mode "a")
with open("notes.txt","a") as file:
    text = "Programming is a skill.\n"
    file.write(text)