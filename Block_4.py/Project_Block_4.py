"""
Small Project — Shopping List Manager 
Build a menu-driven console program (loop until "quit") 
backed by a list: options to add an item, remove an item, view the whole list, 
and check if an item is already on the list. Print a friendly message for each action 
("Added 'milk' to your list.")."""

print("----Shopping List Manager----")

shopping_list = ["Milk","Food","dresses","Fruits"]
proceed = "yes"
while proceed.lower() != "quit" :
    print("What you want to do ?")

    print("1. Add an item\n2. Remove an item\n3. View whole list\n4. Is already exist ")
    option = int(input("Enter option 1/2/3/4 : "))
    print()
    # Adding item 
    if option == 1 :
        item = input("Enter item : ")
        if item in shopping_list :
            print(f"{item} is already exist.")
        else :
            shopping_list.append(item)
    # Removing item
    elif option == 2 :
        rem_item = input("Which item you want to remove : ")
        if rem_item in shopping_list :
            shopping_list.remove(rem_item)
            print(f"{rem_item} is removed successfully.")
        else :
            print(f"{rem_item} does not exist in shopping list.")
    # Viewing whole list
    elif option == 3 :
        print("Shopping list =",shopping_list)
    # Checking an item is already exist or not
    elif option == 4 :
        check_item = input("Enter item you want to check, Is present or not : ")
        if check_item in shopping_list :
            print(f"{check_item} is already present is list")
        else :
            print(f"{check_item} is Not present in list")

    else :
        print("Enter a valid option")
    print()
    proceed = input("If you want to continue enter 'yes' otherwise enter 'quit' : ")
    print()