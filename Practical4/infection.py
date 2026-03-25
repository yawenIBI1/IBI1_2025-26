# Pseudocode:
# 1. Define initial variables: starting infected, growth rate, total students, initial days
# 2. Print the initial infection status
# 3. Use a while loop: continue calculating daily infections while infected < total students  
# 4. Inside the loop: increment day counter
# 5. Inside the loop: update infected count (previous * (1 + growth rate))
# 6. Inside the loop: print the daily infected count
# 7. After loop ends: print the total number of days required
# ----------------------
# Actual Code:
# Core variables:
initial_infected = 5
growth_rate = 0.4  # 40% growth rate (in a decimal way)
total_students = 91  # Total number of students in the class
infected = initial_infected  # Current infected count
days = 0  # Counter for days

# Print initial state
print(f"Initial infected: {initial_infected} students, Growth rate: {growth_rate*100}%")
print("----------------------")

# While loop to calculate daily infections
while infected < total_students:     # condition
    days += 1  # Increment day counter
    infected = infected * (1 + growth_rate)  # Calculate new infected count
    # Print daily results (1 decimal place for readability)
    print(f"Day {days}: Infected count = {infected:.1f}")

# Loop finished, print final result
print("----------------------")
print(f"All {total_students} students infected. Total days taken: {days}")
