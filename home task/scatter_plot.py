# scatter_plot.py

import matplotlib.pyplot as plt

# Data
study_hours = [1, 2, 3, 4, 5, 6, 7, 8]
scores = [50, 55, 65, 70, 75, 85, 90, 95]

# Create scatter plot
plt.scatter(study_hours, scores)

# Labels and title
plt.xlabel("Study Hours")
plt.ylabel("Exam Scores")
plt.title("Relationship Between Study Hours and Exam Scores")

# Show plot
plt.show()
