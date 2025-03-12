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