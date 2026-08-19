"""
Use .get() to safely look up a key that might not exist, 
providing a default value, and compare it to what happens with [] on a missing key."""

student_info = {
    "Eddy"  : 50,
    "Maria" : 80,
    "Zari"  : 76,
    "Luci"  : 69,
    "Vikrum": 70
}

print(student_info.get("Rohan"))
student_info["Rohan"] = 99
print(student_info)