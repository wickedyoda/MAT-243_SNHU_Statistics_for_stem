def variance(data):
  mean = sum(data) / len(data)
  return sum((x - mean) ** 2 for x in data) / len(data)

data = [1, 2, 4, 5]
variance = variance(data)

print(variance)  # Output: 2.5
