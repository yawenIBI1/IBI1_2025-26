# spatial_SIR.py - 2D Spatial Stochastic SIR Model for Practical 9

# Step 1: Import libraries 
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Initialize 100x100 population grid
# State encoding: 0 = Susceptible, 1 = Infected, 2 = Recovered
# Create 100x100 array of all zeros 
population = np.zeros((100, 100), dtype=int)

# -------------------------- Extra exercise: vaccination rates --------------------------
vaccination_rate = float(input("Please enter vaccination rate (e.g., 0.3 for 30%): "))
total_cells = 100 * 100
num_vaccinated = int(total_cells * vaccination_rate)

indices = np.random.choice(total_cells, num_vaccinated, replace=False)
for idx in indices:
    row = idx // 100
    col = idx % 100
    population[row, col] = 3 
# ------------------------------------------------------------------------

# Randomly select 1 initial infected individual 
outbreak = np.random.choice(range(100), 2)  # Get 2 random coordinates (row, col)
population[outbreak[0], outbreak[1]] = 1  # Mark the outbreak point as infected 

# Step 3: Define model parameters 
beta = 0.3       # Infection probability: infected individual infects 8 neighbors with this chance
gamma = 0.05     # Recovery probability: infected individual recovers with this chance per time step
time_steps = 100 # Number of time steps to simulate 

# Save history of population states for plotting
history = [population.copy()]  # Store initial state 

# Step 4: Core time loop 
# Define 8-directional Moore neighborhood offsets 
neighbor_offsets = [(-1, -1), (-1, 0), (-1, 1),
                    (0, -1),          (0, 1),
                    (1, -1),  (1, 0), (1, 1)]

for t in range(1, time_steps + 1):
    # Create a copy of current population to avoid overwriting during the time step
    next_pop = population.copy()
    
    # Find all currently infected individuals 
    infected_rows, infected_cols = np.where(population == 1)
    
    # Step 4.1: Spread infection to neighbors
    for r, c in zip(infected_rows, infected_cols):
        # Check all 8 neighbors for each infected individual
        for dr, dc in neighbor_offsets:
            # Calculate neighbor coordinates
            nr, nc = r + dr, c + dc
            # Ensure neighbor is within grid bounds (0 <= row/col < 100) 
            if 0 <= nr < 100 and 0 <= nc < 100:
                # Only susceptible individuals can be infected
                if population[nr, nc] == 0:
                    # Infect neighbor with probability beta
                    if np.random.rand() < beta:
                        next_pop[nr, nc] = 1  # Mark neighbor as infected 
    
    # Step 4.2: Recovery of infected individuals
    for r, c in zip(infected_rows, infected_cols):
        # Recover with probability gamma 
        if np.random.rand() < gamma:
            next_pop[r, c] = 2  # Mark individual as recovered
    
    # Step 4.3: Update population state for next time step
    population = next_pop
    history.append(population.copy())

# Step 5: Plot results 
# Create 2x2 subplot to show disease spread at key time steps (0, 10, 50, 100)
fig, axes = plt.subplots(2, 2, figsize=(10, 10), dpi=150)
# Time steps to visualize 
plot_time_points = [0, 10, 50, 100]
# Subplot positions (row, column)
subplot_positions = [(0, 0), (0, 1), (1, 0), (1, 1)]

# Plot each time step
for t, (row, col) in zip(plot_time_points, subplot_positions):
    ax = axes[row, col]
    # Use viridis colormap and nearest interpolation
    im = ax.imshow(
        history[t],
        cmap="viridis",
        interpolation="nearest",
        vmin=0,  # Fix color scale to 0-2 for consistent state mapping
        vmax=3
    )
    ax.set_title(f"Time Step {t}", fontsize=10)
    # Set ticks 
    ax.set_xticks([0, 20, 40, 60, 80])
    ax.set_yticks([0, 20, 40, 60, 80])
    ax.tick_params(axis="both", labelsize=7)

plt.subplots_adjust(left=0.08, right=0.88, top=0.90, bottom=0.08, wspace=0.3, hspace=0.3)

# Add color bar to explain state encoding
cbar = fig.colorbar(im, ax=axes, shrink=0.7, pad=0.06)
cbar.set_ticks([0, 1, 2, 3])
cbar.set_ticklabels(["Susceptible (0)", "Infected (1)", "Recovered (2)", "Vaccinated (3)"])
cbar.ax.tick_params(labelsize=7)
cbar.ax.set_title("State", fontsize=8, pad=5)

fig.suptitle("2D Spatial SIR Model: Disease Spread Over Space & Time", 
             fontsize=12, y=0.95)

# Adjust layout and save high-resolution plot
plt.savefig("spatial_SIR_model.png", dpi=150, bbox_inches="tight")

# Show the plot
plt.show()

# Step 6: Simulation completion & verification
print("="*60)
print("2D Spatial SIR Model Simulation Completed Successfully!")
print("="*60)
print(f"Vaccination rate: {vaccination_rate*100:.0f}%")
print("States: 0=Susceptible, 1=Infected, 2=Recovered, 3=Vaccinated")
print("="*60)