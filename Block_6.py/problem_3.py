"""
Given a dictionary of student names to scores, 
loop through with .items() and print "name scored score"."""

student_info = {
    "Eddy"  : 50,
    "Maria" : 80,
    "Zari"  : 76,
    "Luci"  : 69,
    "Vikrum": 70
}

for key, value in student_info.items() :
    print(f"{key} scored {value}")