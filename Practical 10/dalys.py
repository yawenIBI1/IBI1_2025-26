import os
import pandas as pd # dataset processing
import matplotlib.pyplot as plt
import numpy as np

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# ====================== 1 Importing a dataset ======================
# Check working directory 
print("Current working directory:", os.getcwd()) # "getcwd" equals to "pwd"
# List files 
print("Files in directory:", os.listdir()) # "listdir" equals to "ls"

# Read CSV file into dataframe
dalys_data = pd.read_csv("dalys-rate-from-all-causes.csv")

# ====================== 2 Working with dataframes ======================
print("\n=== First 5 rows ===")
print(dalys_data.head(5)) # check first five lines

# Show dataframe information
print("\n=== Data info ===")
dalys_data.info() # Check data types, column names, and row count

# Show summary statistics
print("\n=== Data description ===")
print(dalys_data.describe()) # view statistical summaries for numeric columns (count, mean, standard deviation, quantiles）

# iloc: locate by row index and column index
# loc: locate by row index and column name

# Access first row, fourth column
print("\nValue at (0, 3):", dalys_data.iloc[0, 3])
# Rows come before the comma, columns come after the comma

# iloc examples
print("\n--- iloc examples ---")
print(dalys_data.iloc[2, 0:5])
print(dalys_data.iloc[0:2, :])
print(dalys_data.iloc[0:10:2, 0:5])

# Show Year and DALYs for first 10 rows (Afghanistan)
print("\n--- Year and DALYs for first 10 rows ---")
first_10 = dalys_data.iloc[0:10, [2, 3]]
print(first_10)

# Max DALYs year in Afghanistan's first 10 years
max_year_afg = first_10.loc[first_10["DALYs"].idxmax(), "Year"]

# Maximum DALYs in Afghanistan's first 10 years was in: 1990
print(f"# Max DALYs in Afghanistan first 10 years: {max_year_afg}")

# Boolean column selection
print("\n--- Boolean column selection ---")
my_columns = [True, True, False, True]
print(dalys_data.iloc[0:3, my_columns])

# loc example
print("\n--- loc examples ---")
print(dalys_data.loc[2:4, "Year"])

# Zimbabwe data using Boolean mask
zimbabwe_mask = dalys_data["Entity"] == "Zimbabwe"
zimbabwe = dalys_data.loc[zimbabwe_mask, :]
print("\n--- Zimbabwe data ---")
print(zimbabwe[["Entity", "Year", "DALYs"]].head())

zim_min = zimbabwe["Year"].min()
zim_max = zimbabwe["Year"].max()

# Zimbabwe DALYs recorded from 1990 to 2019
print(f"# Zimbabwe data: {zim_min} - {zim_max}")

# ====================== 3 Across countries ======================
recent_data = dalys_data.loc[dalys_data["Year"] == 2019, ["Entity", "DALYs"]]

max_idx = recent_data["DALYs"].idxmax()
min_idx = recent_data["DALYs"].idxmin()

max_country = recent_data.loc[max_idx, "Entity"]
min_country = recent_data.loc[min_idx, "Entity"]


# 2019 maximum DALYs country: [max_country]
# 2019 minimum DALYs country: [min_country]
print(f"\n# 2019 highest DALYs: {max_country}")
print(f"# 2019 lowest DALYs: {min_country}")

# Plot for MAX or MIN country 
target = max_country
data = dalys_data.loc[dalys_data["Entity"] == target]

plt.figure(figsize=(8,5))
plt.plot(data.Year, data.DALYs, 'b+-', label=target)
plt.xticks(data.Year, rotation=-90)
plt.title(f"DALYs over time in {target} (2019 highest)")
plt.xlabel("Year")
plt.ylabel("DALYs")
plt.legend()
plt.tight_layout()

plt.savefig(f"{max_country}_DALYs_trend.png", dpi=150, bbox_inches="tight")
plt.show()

# ====================== 4 Extra question ======================
# Question: What is the distribution of DALYs across all countries in 2019?
print("\n--- Extra question: 2019 DALYs boxplot ---")
plt.figure(figsize=(6,4))
plt.boxplot(recent_data["DALYs"], vert=False)
plt.title("2019 Global DALYs Distribution")
plt.xlabel("DALYs")
# plt.yticks([]) to shade the "1" label on y-axis
plt.tight_layout()

plt.savefig("2019_Global_DALYs_boxplot.png", dpi=150, bbox_inches="tight")
plt.show()

dalys_range = recent_data["DALYs"].max() - recent_data["DALYs"].min()
print(f"# 2019 global DALYs range: {dalys_range:.2f}")