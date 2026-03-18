import matplotlib.pyplot as plt

# 1. Define population data (2020 and 2024, in millions)
population_data = {
    "UK": {"2020": 66.7, "2024": 69.2}, 
    "China": {"2020": 1426, "2024": 1410},
    "Italy": {"2020": 59.4, "2024": 58.9},
    "Brazil": {"2020": 208.6, "2024": 212.0},
    "USA": {"2020": 331.6, "2024": 340.1}
}

# 2. Calculate percentage change for each country using the given formula
percent_changes = {}
for country, data in population_data.items():
    population_2020 = data["2020"]
    population_2024 = data["2024"]
    # Formula: percent change = ((pop_2024 - pop_2020) / pop_2020) * 100
    pct_change = ((population_2024 - population_2020) / population_2020) * 100
    percent_changes[country] = pct_change
    print(f"{country}: {pct_change:.2f}% population change (2020-2024)")

# 3. Sort countries by percentage change in descending order: largest increase to largest decrease)
sorted_countries = sorted(percent_changes.items(), key=lambda x: x[1], reverse=True)
# sorted(..., key=lambda x: x[1], reverse=True)：Sort the tuples in descending order by their second element (percentage change value)

print("\nPopulation changes sorted from largest increase to largest decrease:")
for country, change in sorted_countries:
    print(f"- {country}: {change:.2f}%")

# Identify country with largest increase and largest decrease
largest_increase_country = sorted_countries[0][0] # sorted_countries[0]: the first element in the "sorted_countries" list
largest_decrease_country = sorted_countries[-1][0] # sorted_countries[-1][0]: the first element in the "sorted_countries[-1]" list
print(f"\nThe country with the largest population increase: {largest_increase_country}")
print(f"The country with the largest population decrease: {largest_decrease_country}")

# 4. Create a labelled bar chart
countries = [country for country, _ in sorted_countries]
changes = [change for _, change in sorted_countries]

plt.figure(figsize=(10, 6))
bars = plt.bar(countries, changes, color=["lightgreen" if c > 0 else "lightcoral" for c in changes])

# Add labels and title
plt.title("Percentage Population Change (2020-2024)", fontsize=14)
plt.xlabel("Country", fontsize=12)
plt.ylabel("Percentage Change (%)", fontsize=12)
plt.axhline(y=0, color="black", linestyle="-", linewidth=0.8)  # Add zero line for clarity
plt.tight_layout()

# Optional: Add value labels on top of bars
for bar in bars:
    height = bar.get_height() # height of the bar: changes in percentage
    plt.text(
    bar.get_x() + bar.get_width()/2.,  # X coordinate: horizontal center of the bar
    height + (0.1 if height > 0 else -0.1),  # Y coordinate: offset from the top/bottom of the bar
    f'{height:.2f}%',  # Text to display (2 decimal places with percentage sign)
    ha='center',  # Horizontal alignment: center
    va='bottom' if height > 0 else 'top'  # Vertical alignment
)

plt.show()
