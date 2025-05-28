# Project Plan:
# 1.The purpose of this code is to simulate the spatial SIR model of disease spread on a grid and visualize the results.
# 2.The code initializes a grid representing a population, simulates the spread of an infection, and visualizes the results using a custom colormap.
# 3.The simulation includes infecting neighboring cells and recovering infected individuals over a specified number of timesteps.
# Import necessary libraries
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib.colors import ListedColormap
import numpy as np
# Initialize the data
size = 100
beta = 0.3
gamma = 0.05
timesteps = 100

# Create custom colormap: susceptible=purple, infected=blue-green, recovered=yellow
colors = ['#4b006e', '#00a896', '#fde74c']
cmap = ListedColormap(colors)

# Initialize population grid (0=susceptible, 1=infected, 2=recovered)
population = np.zeros((size, size), dtype=np.uint8)

# Random initial outbreak
outbreak = np.random.choice(range(size), 2)
population[outbreak[0], outbreak[1]] = 1

# Function to infect neighbors
def infect_neighbors(pop, beta):
    """Infect susceptible neighbors of infected individuals"""
    infected_positions = np.argwhere(pop == 1)
    new_pop = pop.copy()
    
    for i, j in infected_positions:
        # Check all 8 neighbors (Moore neighborhood)
        for x in range(max(0, i-1), min(size, i+2)):
            for y in range(max(0, j-1), min(size, j+2)):
                if pop[x, y] == 0 and np.random.random() < beta:
                    new_pop[x, y] = 1
    return new_pop

# Function to handle recovery
def recover(pop, gamma):
    """Recover infected individuals with probability gamma"""
    infected_mask = (pop == 1)
    recovery_mask = np.random.random(pop.shape) < gamma
    pop[np.logical_and(infected_mask, recovery_mask)] = 2
    return pop

# Simulation loop
fig, ax = plt.subplots(figsize=(8, 6))
plots = []  # To store plots at different timesteps

for t in range(timesteps + 1):
    # Update population
    if t > 0:
        population = infect_neighbors(population, beta)
        population = recover(population, gamma)
    
    # Plot at specific timesteps
    if t in [0, 10, 50, 100]:
        plt.figure()
        plt.imshow(population, cmap=cmap, interpolation='nearest')
        plt.title(f'Time Step {t}')
        plt.colorbar(ticks=[0, 1, 2], label='State (0=S, 1=I, 2=R)')
        plt.show()

# Animation (optional)
fig, ax = plt.subplots()
img = ax.imshow(population, cmap=cmap, interpolation='nearest')

def update(frame):
    global population
    if frame > 0:
        population = infect_neighbors(population, beta)
        population = recover(population, gamma)
    img.set_data(population)
    ax.set_title(f'Time Step {frame}')
    return img,

ani = FuncAnimation(fig, update, frames=timesteps, interval=100, blit=True)
plt.colorbar(img, ticks=[0, 1, 2], label='State (0=S, 1=I, 2=R)')
plt.show()