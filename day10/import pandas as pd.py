import pandas as pd

# Step 1: Create DataFrame
data = pd.DataFrame({
    "Location": [" New York", "new york", "NEW YORK ", "New York"]
})

# Step 2: Remove leading & trailing spaces
data["Location"] = data["Location"].str.strip()

# Step 3: Convert all text to lowercase (standardize case)
data["Location"] = data["Location"].str.lower()

# Step 4: Verify only one version exists
print("Unique Locations:", data["Location"].unique())

# Step 5: Display cleaned DataFrame
print("\nCleaned Data:")
print(data)
