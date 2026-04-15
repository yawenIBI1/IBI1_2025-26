# SIR.py - A simple stochastic SIR model for Practical 9

# Step 1: Import required libraries 
import numpy as np
import matplotlib.pyplot as plt

# Step 2: Define model parameters 
Total_population = 10000          # Total population size
Initial_Susceptible = 9999        # Initial susceptible individuals
Initial_Infected = 1              # Initial infected individuals
Initial_Recovered = 0             # Initial recovered individuals
beta = 0.3                        # Infection rate (transmission probability per contact)
gamma = 0.05                      # Recovery rate (probability of recovery per time step)
time_steps = 1000                 # Number of time steps to simulate

# Step 3: Initialize lists to track S/I/R over time 
S = [Initial_Susceptible]  # Track susceptible counts
I = [Initial_Infected]     # Track infected counts
R = [Initial_Recovered]    # Track recovered counts

# Step 4: Core time loop (1000 time steps, stochastic simulation)
for t in range(time_steps):
    # Get current state (last value in each tracking list)
    current_Susceptible = S[-1]
    current_Infected = I[-1]
    current_Recovered = R[-1]
    
    # Calculate infection probability for susceptible people
    # infection probability = infection rate (beta) × proportion of infected people in population
    infection_probability = beta * (current_Infected / Total_population)
    
    # Simulate new infections (binomial distribution: efficient batch calculation)
    # Equivalent to checking each susceptible person with infection_prob
    new_infected = np.random.binomial(n=current_Susceptible, p=infection_probability)
    
    # Simulate new recoveries (binomial distribution: check each infected person)
    new_recovered = np.random.binomial(n=current_Infected, p=gamma)
    
    # Update state for next time step
    new_S = current_Susceptible - new_infected
    new_I = current_Infected + new_infected - new_recovered
    new_R = current_Recovered + new_recovered
    
    # Append new state to tracking lists
    S.append(new_S)
    I.append(new_I)
    R.append(new_R)

# Step 5: Plot results 
# Set plot size and resolution 
plt.figure(figsize=(6, 4), dpi=150)

# Plot S/I/R curves with matching colors and labels
plt.plot(range(len(S)), S, label='susceptible', color='#1f77b4')  # Blue
plt.plot(range(len(I)), I, label='infected', color='#ff7f0e')    # Orange
plt.plot(range(len(R)), R, label='recovered', color='#2ca02c')  # Green

# Add required plot elements: labels, title, legend
plt.xlabel('time')
plt.ylabel('number of people')
plt.title('SIR model')
plt.legend()

# Save plot as PNG 
plt.savefig('SIR_model.png', dpi=150, bbox_inches='tight')

# Show the plot
plt.show()

# Step 6: Verify model behavior 
print("="*50)
print("SIR Simulation Completed Successfully!")
print("="*50)
print(f"Final Population Counts:")
print(f"  Susceptible: {S[-1]}")
print(f"  Infected: {I[-1]}")
print(f"  Recovered: {R[-1]}")
print("\nKey Notes (as per task questions):")
print("1. Run the code multiple times: Results will differ (stochastic model)")
print("2. Smaller population: Larger random fluctuations in curves")
print("3. Change beta/gamma:")
print("   - Higher beta: Faster spread, higher infection peak")
print("   - Higher gamma: Faster recovery, lower infection peak")
print("="*50)