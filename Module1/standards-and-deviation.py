from statistics import stdev, variance

numbers = [1, 2, 4, 5]
stdev_of_numbers = stdev(numbers)
variance_of_numbers = variance(numbers)

print(stdev_of_numbers)  # Output: 1.5811388300841898
print(variance_of_numbers)  # Output: 2.5
