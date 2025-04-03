# Project Plan:
# 1. The purpose of this code is to simulate the SIR model of disease spread and visualize the results.
# 2. Initialize the number of susceptible (S), infected (I), recovered (R) individuals, total population (N), beta and gamma.
# 3. Create a loop to simulate the SIR model over a specified number of time units.
# 4. Calculate the probability of infection and select newly infected and recovered individuals based on this probability.
# 5. Update the number of individuals in each group (S, I, R) and ensure that the values do not go negative and no more than toal people.
# 6. Store the updated values in lists to show the changes over time.
# 7. Use plt to create a line plot showing the number of susceptible, infected, and recovered individuals over time.

# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# initialization: create initial values of S, I, R, N, beta and gamma
N = 10000
S = 9999
I = 1
R = 0
beta = 0.3
gamma = 0.05
S_list, I_list, R_list = [S], [I], [R] # create an empty list that stores changes in the number of people once nubers change

# create a loop to simulate the SIR model
for t in range(1000): # simulate 1000 time units
    infection_probability= beta * I_list[-1]/N # calculate the probability of infection using the formula beta * I/N
# select newly infected and recovered people based on the probability of infection and recovery
    new_infected = np.random.choice([0, 1], S_list[-1], p=[1-infection_probability, infection_probability]).sum()
    new_recovered = np.random.choice([0, 1], I_list[-1], p=[1-gamma, gamma]).sum()
# update the number of people in each group  
    S_new = S_list[-1] - new_infected
    I_new = I_list[-1] + new_infected - new_recovered
    R_new = R_list[-1] + new_recovered
# make sure the number of people is not negative
    if S_new < 0:
        S_new = 0
    if I_new < 0:
        I_new = 0
    if R_new < 0:
        R_new = 0
# make sure the total number of people is not more than N
    if S_new + I_new + R_new > N:
        S_new = N - I_new - R_new
    if S_new < 0:
        S_new = 0
    if I_new < 0:
        I_new = 0
    if R_new < 0:
        R_new = 0

# add the updated number of people to the list
    S_list.append(S_new)
    I_list.append(I_new)
    R_list.append(R_new)

# draw the SIR model gragh and mame x-axis and y-axis
plt.plot(S_list, label='susceptible')
plt.plot(I_list, label='infected')
plt.plot(R_list, label='recovered')
plt.legend()
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR Model')
# show the plot
plt.show()