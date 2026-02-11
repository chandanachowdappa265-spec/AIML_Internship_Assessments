import pandas as pd

# Create the Series
grades = pd.Series([85, None, 92, 45, None, 78, 55])

# Identify missing values
missing = grades.isnull()

# Fill missing values with 0
filled_grades = grades.fillna(0)

# Apply boolean mask (greater than 60)
filtered = filled_grades[filled_grades > 60]

# Output
print("Original Series:")
print(grades)

print("\nMissing Values (True means missing):")
print(missing)

print("\nFilled Series (NaN replaced with 0):")
print(filled_grades)

print("\nScores greater than 60:")
print(filtered)
