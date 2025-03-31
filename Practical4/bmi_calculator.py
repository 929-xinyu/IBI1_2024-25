# Project Plan:
# 1. The purpose of the program is to calculate the BMI of a person based on their weight and height.
# 2. Use input() to store the weight and height values.
# 3. Use float() to convert the input values to float.
# 4. Use the formula to calculate BMI: BMI = weight / (height ** 2)
# 5. Determine the categories based on the weight and height:
#    - Underweight: BMI < 18.5
#    - Normal weight: 18.5 <= BMI <= 30
#    - Obese: BMI > 30
# 6. Output the BMI and its category.

# Store the person's weight in kilograms
weight = float(input("Enter your weight in kg: "))
# Store the person's height in meters
height = float(input("Enter your height in meters: "))

# Calculate BMI using the formula: BMI = weight / (height ** 2)
bmi = weight / (height ** 2)

# Determine the BMI category
if bmi < 18.5:
    category = "underweight"
elif 18.5 <= bmi <= 30:
    category = "normal weight"
else:
    category = "obese"

# Print the BMI and category
print("Your BMI is " + str(bmi) + ", which is considered " + category + ".")