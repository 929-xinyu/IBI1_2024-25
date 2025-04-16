# Project Plan:
# 1. The purpose of this code is to create a drug dosage calculator for children, specifically for paracetamol (acetaminophen) based on weight and strength.
# 2. Define a function that takes the child's weight and the strength of the paracetamol and input parameters.
# 3. Check if the weight is within a specified range (10-100 kg) and if the strength is one of the expected values (120 mg/5 ml or 250 mg/5 ml).
# 4. Calculate the dosage based on weight and strength, and return the volume in ml.
# 5. Test the function with sample data to ensure it works as the way we want.

def calculate_pain_relief(weight, strength):
    # check if weight is within the specified range
    if weight < 10 or weight > 100:
        raise ValueError("the weight must be between 10 and 100 kg")
    
    # check if strength is one of the expected values
    if strength not in [120, 250]:
        raise ValueError("the strength must be either 120 mg/5 ml or 250 mg/5 ml")
    
    # calculate the dosage based on weight
    dosage = 15 * weight
    
    # calculate the volume based on the strength
    if strength == 120:
        volume = (dosage / 120) * 5
    elif strength == 250:
        volume = (dosage / 250) * 5
    
    return volume

# the example I give is to use it to test the code.
try:
    weight = float(input("please enter the child's weight (kg): "))
    strength = int(input("please enter the child's strength (ml): "))
    volume = calculate_pain_relief(weight, strength)
    print(f"{volume:.2f} ml")
except ValueError as e:
    print(e)