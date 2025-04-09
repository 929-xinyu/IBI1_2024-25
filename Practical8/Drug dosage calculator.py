# Project Plan:
# 1. The purpose of this code is to create a drug dosage calculator for children, specifically for paracetamol (acetaminophen) based on weight and strength.
# 2. The code will take the child's weight and the strength of the paracetamol as input.
# 3. It will calculate the recommended dosage based on the child's weight and the strength of the paracetamol.
# 4. The code will check if the weight is within a specified range (10-100 kg) and if the strength is one of the expected values (120 mg/5 ml or 250 mg/5 ml).

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