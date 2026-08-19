"""Write a program that reads a temperature as text input and converts it to a float, 
then prints it rounded to 1 decimal place using round() ."""
temp = input("Enter temperature in float : ")
float_temp = float(temp)
print(round((float_temp),1))