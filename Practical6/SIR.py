# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
# Initialization:create initial values of S, I, R, N, beta and gamma
N = 10000
S = 9999
I = 1
R = 0
beta = 0.3
gamma = 0.05
S_list, I_list, R_list = [S], [I], [R] # Create an empty list that stores changes in the number of people at each step

# create a loop to simulate the SIR model
for t in range(1000): # Simulate 1000 time units
    infection_prob = beta * I_list[-1]/N # Calculate the probability of infection
# Select newly infected and recovered people based on the probability of infection and recovery
    new_infected = np.random.choice([0, 1], S_list[-1], p=[1-infection_prob, infection_prob]).sum()
    new_recovered = np.random.choice([0, 1], I_list[-1], p=[1-gamma, gamma]).sum()
# Update the number of people in each group  
    S_new = S_list[-1] - new_infected
    I_new = I_list[-1] + new_infected - new_recovered
    R_new = R_list[-1] + new_recovered
# Make sure the number of people is not negative
    if S_new < 0:
        S_new = 0
    if I_new < 0:
        I_new = 0
    if R_new < 0:
        R_new = 0
# Add the updated number of people to the list
    S_list.append(S_new)
    I_list.append(I_new)
    R_list.append(R_new)

# Draw the SIR model gragh
plt.figure(figsize=(6, 4), dpi =150)
plt.plot(S_list, label='susceptible')
plt.plot(I_list, label='infected')
plt.plot(R_list, label='recovered')
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR Model')
plt.legend()
plt.show()