import numpy as np

dataset = [0, -6, 10, 5, 8, 2, -12, 11, -2]

minimum = min(dataset)
maximum = max(dataset)
median = np.median(dataset)
first_quartile = np.percentile(dataset, 25)
third_quartile = np.percentile(dataset, 75)

print("Minimum:", minimum)
print("First quartile:", first_quartile)
print("Median:", median)
print("Third quartile:", third_quartile)
print("Maximum:", maximum)
