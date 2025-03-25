# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

def run_sir_simulation(vaccination_rate):
    # Initialization:create initial values
    N = 10000
    V0 = int(N * vaccination_rate)
    S0, I0, R0 = N - V0 - 1, 1, 0  
    beta = 0.3
    gamma = 0.05

    # Create an empty list that stores changes in the number of people at each step
    S_list, I_list, R_list = [S0], [I0], [R0]

    # Create a loop to simulate the SIR mode
    for t in range(1000): # Simulate 1000 time units
        infection_prob = beta * I_list[-1] / (N - V0) if (N - V0) > 0 else 0 # Calculate the probability of infection
        
    # Select newly infected and recovered people based on the probability of infection and recovery
        new_infected = np.random.binomial(S_list[-1], infection_prob) if S_list[-1] > 0 else 0
        new_recovered = np.random.binomial(I_list[-1], gamma)
        
    # Update the number of people in each group
        S_new = max(0, S_list[-1] - new_infected)
        I_new = max(0, I_list[-1] + new_infected - new_recovered)
        R_new = max(0, R_list[-1] + new_recovered)
        
        # Add the updated number of people to the list
        S_list.append(S_new)
        I_list.append(I_new)
        R_list.append(R_new)
    
    return I_list  # Return the number of infected people at each time step

# Run the simulation with different vaccination rates
vaccination_rates = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
results = {}

for rate in vaccination_rates:
    results[f"{int(rate*100)}%"] = run_sir_simulation(rate)

# Plot the results
plt.figure(figsize=(12, 7))

colors = plt.cm.viridis(np.linspace(0, 1, len(vaccination_rates)))
for (label, data), color in zip(results.items(), colors):
    plt.plot(data, label=label, color=color)

plt.xlabel('Time')
plt.ylabel('Number of Infected People')
plt.title('SIR Model with Different Vaccination Rates')
plt.legend(title="Vaccination Rate")
plt.tight_layout()
plt.show()