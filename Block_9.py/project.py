# Storing Students in a list of dictionaries
students = [
    {"name" : "Ayesha Maha",
     "age"  : 15,
     "grade": "10th",
     "roll_num" : 12,
     "scores" : [72,94,87,65]
    },
    {
        "name" : "Maha",
        "age"  : 16 ,
        "grade" : "10th",
        "roll_num" : 13,
        "scores" : [86,88,96,78]
    }
]

# Menu loop
is_process = "yes"
while is_process.lower() != "quit" :
    # 1. Add a student — prompt for a name and at least one score; store the score as a list 
    # so more can be added later.
    print("What you want to do, select by number : ")
    menu = "1. Add a student\n2. Add a score to an existing student\n3. View one student's report\n4. View the class summary\n5. Search by partial name\n"
    print(menu)
    option = input("Select 1/2/3/4/5 : ")

    if option == "1" :
        name = input("Enter name : ")
        score = []
        s = int(input("Enter score : "))
        score.append(s)
        # students.append({"scores" : score})
        students.append({"name":name , "scores":score})
        print(students)

    # 2. Add a score to an existing student — 
    # look the student up by name (loop through the list; handle "not found" cleanly).
    elif option == "2" :
        name = input("Enter name : ")
        for dic in students :
            for key, value in dic.items() :
                if value == name :
                    dic.get(name)
                    print(dic["scores"])
                    score = int(input(f"Enter score of {name} : "))
                    dic["scores"].append(score)
                    print(f"{name} scores : {dic["scores"]}")

    # 3. View one student's report — print their name, their list of scores, 
    #     their average score (computed with a loop or sum()/len() ), 
    #     and a letter grade using the Block 8 grading logic.
    
    elif option == "3" :
        for dic in students :
            average_score = sum(dic["scores"]) / len(dic["scores"])
            print("""-----student's report-----""")
            for key , value in dic.items() :
                print(f"{key} : {value}")
            print(f"Average : {average_score}")

            if average_score <= 100 :
                if  average_score > 90  :
                    print("A")
                    print("Excellent work!")
                elif average_score > 70 :
                    print("B")
                    print("V.Good work!")
                elif average_score > 50 :
                    print("C")
                    print("Good work!")
                elif average_score > 30 :
                    print("D")
                    print("Poor work!")
                elif average_score > 0 :
                    print("F")
                    print("Let's set up extra practice time.")
                else :
                    print("Enter positive score!")
            else :
                print("Invalid input")
            print("\n")

    #    4. View the class summary — print every student's name and average, 
    #     then print who has the highest class average (loop through and track the max — 
    #     same pattern as the Block 6 "most expensive item" exercise).
    elif option == "4" :
        avg_scr = []
        for std in students :
            average_score = sum(std["scores"]) / len(std["scores"])
            print(f"name    : {std["name"]}")
            print(f"Average : {average_score}")
            avg_scr.append(average_score)
        avg_scr.sort(reverse= True)
        print(f"Average score list : {avg_scr}")

        for key, value in std.items() :
            heighest_avg = max(avg_scr)
        print(f"Heighest_avg : {heighest_avg}")

        # 5. Search by partial name — given a text fragment, 
        #     print every student whose name contains it (string operations from Block 3).

    elif option == "5" :
        partial_name = input("Enter partial name : ")
        for dic in students :
            name = dic["name"]
            part_name = name.split()
            if partial_name in part_name :
                print(dic)

  
    is_process = input("If you want to continue enter (yes) else enter (quit) : ")
    