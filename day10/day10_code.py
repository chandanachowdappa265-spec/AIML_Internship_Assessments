import pandas as pd

# Step 1: Create Sample Data
data = pd.DataFrame({
    "Price": ["$100", "$250", "$300", "$150"],
    "Date": ["2024-01-01", "2024-02-01", "2024-03-01", "2024-04-01"]
})

# Step 2: Check initial data types
print("Before Conversion:\n")
print(data.dtypes)

# Step 3: Remove '$' symbol and convert Price to float
data["Price"] = data["Price"].str.replace("$", "", regex=False).astype(float)

# Step 4: Convert Date column to datetime
data["Date"] = pd.to_datetime(data["Date"])

# Step 5: Check data types after conversion
print("\nAfter Conversion:\n")
print(data.dtypes)

# Step 6: Display cleaned data
print("\nFinal Data:")
print(data)
