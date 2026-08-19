"""
Print the numbers 1 to 20, but print "skip" instead of the number for anything divisible by 4"""
for i in range(1, 21) :
    if i % 4 == 0 :
        print("skip")
    else :
        print(i)