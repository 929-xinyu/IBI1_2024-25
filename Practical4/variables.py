# Project Plan:
# 1. The purpose of the program is to compare the time spent on two commuting methods: walking + bus and driving + walking.
# 2. Calculate the total time for each commuting method using variables.
# 3. The time values taken for each method are stored in variables.
# 4. Compare the total time for both methods using if-else statements.
# 5. Output the total time for each method and show which one is faster.

# walking + transit time in minutes
a = 15       # the time it takes to walk to the bus stop
b = 75       # time taken by bus (1 hour 15 minutes = 75 minutes)
c = a + b    # total time for walking + bus

# driving + walking time in minutes
d = 90       # time taken by car (1 hour 30 minutes = 90 minutes)
e = 5        # the time it takes to walk from the parking lot to the office
f = d + e    # total time for driving + walking
# output the total time for each commuting method

# compare the total time spent on both modes of commuting
if c < f:
    print("walking + bus is faster, total time:", c, "minutes")
else:
    print("driving + walking is faster，total time：", f, "minutes")

# Project Plan:
# 1. The purpose of the program is to check the truth table for W.
# 2. Use the logical AND operator to check the truth table.
# 3. Use the variables X and Y to represent the truth values.
# 4. Clculate W using the logical AND operator.
# 5. Output the truth table for W.

# The truth table for W (X AND Y) is:
# | X     | Y     | W = X AND Y |
# |-------|-------|-------------|
# | True  | True  | True        |
# | True  | False | False       |
# | False | True  | False       |
# | False | False | False       |

# Part 1: Logical AND operation
X = True   # boolean value
Y = True   # boolean value
W = X and Y  # W should only be true when both X and Y are true

print("The truth table for W is:")
print(f"X = {X}, Y = {Y}, W = {W}")  # print the result

# Part 2: Comparison checks
c = 10
e = 5
f = 15

# Check 1: f should be greater than c
if f > c:
    print("Check 1 passed: f is greater than c")
else:
    print("Check 1 failed: f is not greater than c")

# Check 2: c should be greater than e (alternative check)
if c > e:
    print("Check 2 passed: c is greater than e")
else:
    print("Check 2 failed: c is not greater than e")