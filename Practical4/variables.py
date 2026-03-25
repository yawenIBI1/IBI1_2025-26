# 4.1 
# Define Scotland's population in different years (unit: million)
a = 5.08  # Population in 2004
b = 5.33  # Population in 2014
c = 5.55  # Population in 2024

# Calculate the population change between periods
d = b - a  # Change from 2004 to 2014
e = c - b  # Change from 2014 to 2024

# Print results for verification
print("Population change 2004-2014:", d, "million")
print("Population change 2014-2024:", e, "million")
print("Is d greater than e?:", d > e)

# Population growth trend analysis
# d = 0.25 million, e = 0.22 million. Since d > e, 
# Scotland's population growth rate is decelerating.

# 4.2 Booleans
# Define boolean variables
X = True
Y = False
# Calculate the result of X OR Y
W = X or Y

# Print the result of W
print("Result of W = X or Y:", W)

# COMMENT: Truth table for W (OR logic: True if at least one is True)
# X=True, Y=True  → W=True
# X=True, Y=False → W=True
# X=False, Y=True → W=True
# X=False, Y=False → W=False
