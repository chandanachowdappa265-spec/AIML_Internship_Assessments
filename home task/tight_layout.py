# dashboard.py

import matplotlib.pyplot as plt

# Data
categories = ['Electronics', 'Clothing', 'Home']
sales = [300, 450, 200]

# Create figure
plt.figure(figsize=(10, 4))

# --- Subplot 1: Bar Chart ---
plt.subplot(1, 2, 1)
plt.bar(categories, sales)
plt.title("Sales by Category")
plt.xlabel("Categories")
plt.ylabel("Sales")

# --- Subplot 2: Line Plot (Trend Example) ---
months = ['Jan', 'Feb', 'Mar']
monthly_sales = [250, 400, 500]

plt.subplot(1, 2, 2)
plt.plot(months, monthly_sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")

# Prevent overlap
plt.tight_layout()

# Show dashboard
plt.show()
