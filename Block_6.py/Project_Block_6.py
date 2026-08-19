"""
Small Project — Contact Book 
A dictionary where keys are names and values are phone numbers. 
Menu-driven loop: add a contact, look up a contact (handle "not found" gracefully with .get() ), 
update a contact, delete a contact, and list all contacts. Persist nothing yet — in-memory 
is fine for this block."""

info_dict = {
    "Maha" : "0300-6382365",
    "Eddy" : "0322-8274193",
    "Zari" : "0325-2947358"
    }

procedure = "yes"
while procedure != "quit" :
    print("Menu\nChoose options by numbers.")

    print("1. Add contact\n2. Look up a contact\n3. Update contact\n4. Delete contact\n5. Show contacts")

    option = input("Select option according to operations\n1/2/3/4/5 : ")

    # Adding contact
    if option == "1" :
        num = int(input("how many contacts you want to add : "))
        for i in range(1,num+1) :
            name = input("Enter name of person : ")
            number = input(f"Enter {name}'s number : ")
            info_dict[name] = number
        print()
    # Looking contact
    elif option == "2" :
        contact = input("Enter name : ")
        print(contact,":",info_dict.get(contact))
        print()
    # Update contact
    elif option == "3" :
        update_contact = input("Enter name : ")
        num_contact = input("Enter number")
        info_dict.update({update_contact:num_contact})
        print()
    # Delete contact
    elif option == "4" :
        name_key = input("Enter name you want to delete : ")
        if name_key in info_dict :
            info_dict.pop(name_key)
            print(info_dict)
        else :
            print(f"{name_key} is not found.")
        print()
    # Show contact
    elif option == "5" :
        for key, value in info_dict.items() :
            print(key,":",value)
        print()
    procedure = input("Are you want to continue : ")