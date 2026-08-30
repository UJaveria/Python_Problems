# Write append_log(filename, message) that appends "[entry N] message" , tracking the counter yourself.
def append_log(filename, message) :
    num = 1
    with open(filename, "r") as file :
        for line in file :
            num += 1
        with open(filename, "a") as file :
            file.write(f"[entery {num} ] {message}\n")


filename = "log.txt"

while True :
    message = input("Enter your message : ")

    if message == "" :
        break
    append_log(filename,message)