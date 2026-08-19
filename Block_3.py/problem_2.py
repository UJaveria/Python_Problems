"""Given a full name as one string, split it and print "Last, First" format."""
full_name = "Ume Javeria"
separation = full_name.split(" ")
first_name = separation[0]
last_name = separation[-1]
print("First_name :",first_name)
print("Last_name  :",last_name)