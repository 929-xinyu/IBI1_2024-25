# Project Plan:
# 1. The purpose of the program is to calculate the first 10 triangular numbers.
# 2. Use a for loop from 1 to 10.
# 3. Use the formula to calculate the first 10 triangular number: Tn = n(n + 1)/2
# 4. Output the first 10 triangular numbers.

# loop through numbers from 1 to 10 using a for loop
for n in range(1, 11): # From 1 to 10
    # calculate the triangular number using the formula: Tn = n(n + 1)/2
    triangular_number = n * (n + 1) / 2
    # print the triangular numbers
    print("The first 10 triangular numbers are:" , triangular_number)