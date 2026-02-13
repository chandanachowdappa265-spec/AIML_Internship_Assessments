import pandas as pd

# Step 1: Create DataFrame
data = pd.DataFrame({
    "Location": [" New York", "new york", "NEW YORK ", "New York"]
})

# Step 2: Before cleaning
print("Before Cleaning:")
print(data["Location"].unique())

# Step 3: Clean text
data["Location"] = data["Location"].str.strip().str.title()

# Step 4: After cleaning
print("\nAfter Cleaning:")
print(data["Location"].unique())

# Step 5: Display DataFrame
print("\nFinal Data:")
print(data)
