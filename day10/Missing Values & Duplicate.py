import pandas as pd
import numpy as np

# Create sample data with missing values & duplicates
data = pd.DataFrame({
    "Order_ID": [101, 102, 103, 104, 104],
    "Customer": ["A", "B", "C", "D", "D"],
    "Amount": [500, np.nan, 700, 800, 800],
    "Quantity": [1, 2, np.nan, 4, 4]
})

# Save as CSV
data.to_csv("customer_orders.csv", index=False)

print("CSV file created successfully!")
