# Initialize an empty list to store triangular numbers
triangular_numbers = []

# Loop through numbers from 1 to 10
for n in range(1, 11):
    # Calculate the triangular number using the formula: T_n = n(n + 1)/2
    triangular_number = n * (n + 1) / 2
    # Append the result to the list
    triangular_numbers.append(triangular_number)

# Print the list of triangular numbers
print("The first 10 triangular numbers are:", triangular_numbers)