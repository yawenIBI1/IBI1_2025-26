import matplotlib.pyplot as plt

# 1. Define heart rate data
heart_rates = [72, 60, 126, 85, 90, 59, 76, 131, 88, 121, 64]

# 2. Calculate the number of patients and mean heart rate
num_patients = len(heart_rates) # Calculate the length of the list to obtain the total number of patients （11）
mean_heart_rate = sum(heart_rates) / num_patients
print(f"There are {num_patients} patients in the dataset, with a mean heart rate of {mean_heart_rate:.2f} bpm.")

# 3. Categorize and count heart rates  
low = 0 
normal = 0
high = 0

for hr in heart_rates:
    if hr < 60:
        low += 1
    elif 60 <= hr <= 120:
        normal += 1
    else:
        high += 1

# 4. Print category counts and identify the largest category
print(f"\nNumber of patients in each category:")
print(f"Low (<60 bpm): {low}")
print(f"Normal (60-120 bpm): {normal}")
print(f"High (>120 bpm): {high}")

# identify the largest category
categories = ["Low", "Normal", "High"]
counts = [low, normal, high]
max_count = max(counts) # Find the maximum value among the three categories
max_category = categories[counts.index(max_count)] 
# counts.index(max_count)：Locate the position of this maximum value in the list
# categories[...]：Retrieve the corresponding category name based on the position
print(f"\nThe category with the largest number of patients is {max_category}.")

# 5. Create a labelled pie chart
labels = ["Low (<60 bpm)", "Normal (60-120 bpm)", "High (>120 bpm)"]
colors = ["lightblue", "lightgreen", "lightcoral"]
plt.figure(figsize=(8, 8))
plt.pie(counts, labels=labels, colors=colors, autopct="%1.1f%%", startangle=90)
plt.title("Distribution of Resting Heart Rate Categories", fontsize=14)
plt.tight_layout()
plt.show()
