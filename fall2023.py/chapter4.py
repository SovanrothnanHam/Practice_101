# Write a program that will calculate the area of a circle
# radius = 20
# x = radius*radius*3.14159
# print (x) 
# miles = float(input("Enter the number of miles: "))
# kilometers = miles * 1.609
# print(f"The equivalent distance in kilometers is {kilometers}")

# 4.5.birth day to be determined
 # Prompt the user to answer the first question

# 4.6.Prompt the user to enter weight in pounds
# Get the weight in pounds from the user.
weight = eval(input("Enter weight in pounds: "))
# Get the height in inches from the user.
height = eval(input("Enter height in inches: "))
KILOGRAMS_PER_POUND = 0.45359237
METERS_PER_INCH = 0.025
# Convert weight to kilograms.
weightInKilograms = weight * KILOGRAMS_PER_POUND
# Convert height to meters.
heightInMeters = height * METERS_PER_INCH
# Calculate BMI.
bmi = weightInKilograms / (heightInMeters * heightInMeters)
# Print the BMI and for".2f" which tells the format()function to format the number as a floating-point number with two decimal places.
print("BMI is", format(bmi, ".2f"))
# Classify the BMI.
if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Overweight")
else:
    print("Obese")
