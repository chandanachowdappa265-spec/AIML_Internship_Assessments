import numpy as np


scores = np.random.randint(50, 101, size=(5, 3))


mean_scores = scores.mean(axis=0)

centered_scores = scores - mean_scores


print("Original Scores (5 students, 3 subjects):")
print(scores)

print("\nMean of each subject (column-wise mean):")
print(mean_scores)

print("\nCentered Scores (after broadcasting normalization):")
print(centered_scores)
