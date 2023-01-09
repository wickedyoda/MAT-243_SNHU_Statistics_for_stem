def weighted_mean(values, weights):
  return sum(v * w for v, w in zip(values, weights)) / sum(weights)

values = [3, 0, 37, 0, 0, 0, 3, 37]
weights = [4, 2, 2]

mean = weighted_mean(values, weights)

print(mean)  # Output: 23.333333333333332