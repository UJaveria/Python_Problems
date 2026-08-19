"""
Write a BMI calculator: given weight (kg) and height (m), 
compute BMI and print the category (underweight/normal/overweight/obese) 
using the standard thresholds."""

weight = float(input("Enter weight in kg : "))
height = float(input("Enter height in m  : "))

calc_BMI = weight / ( height * height)

if calc_BMI < 18.5 :
    print("Underweight")
elif calc_BMI < 24.9 :
    print("Healthy weight")
elif calc_BMI < 29.9 :
    print("Overweight")
else :
    print("Obesity")

    
"""
Underweight: Below 18.5
Healthy weight: 18.5 to 24.9
Overweight: 25.0 to 29.9
Obesity: 30.0 or higher"""