import pandas as pd

data = pd.read_csv("customer_orders.csv")

print("Shape Before Cleaning:", data.shape)

print("\nMissing Values:")
print(data.isna().sum())

# Fill missing numeric columns with median
numeric_cols = data.select_dtypes(include=["number"]).columns
data[numeric_cols] = data[numeric_cols].fillna(data[numeric_cols].median())

# Remove duplicates
data = data.drop_duplicates()

print("\nShape After Cleaning:", data.shape)

print("\nFinal Data:")
print(data)
