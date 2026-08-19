"""
Write a simple traffic light simulator: given a color string ("red"/"yellow"/"green"), 
print the correct instruction ("Stop"/"Slow down"/"Go") and print "Invalid color" for anything else."""

color = input('Enter a color ("red"/"yellow"/"green") : ')

if color.lower() == "red" : 
    print("Stop")
elif color.lower() == "yellow" :
    print("Slow down")
elif color.lower() == "green" :
    print("Go")
else :
    print("Invalid color")