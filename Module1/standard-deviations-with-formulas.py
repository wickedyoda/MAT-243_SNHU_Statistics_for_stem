from math import sqrt

def mean(data):
  return sum(data) / len(data)

def stdev(data):
  return sqrt(variance(data))

def variance(data):
  return mean((x - mean(data)) ** 2 for x in data)

numbers = [1, 2, 3, 4, 5]
stdev_of_numbers = stdev(numbers)
variance_of_numbers = variance(numbers)

print(stdev_of_numbers)  # Output: 1.5811388300841898
print(variance_of_numbers)  # Output: 2.5