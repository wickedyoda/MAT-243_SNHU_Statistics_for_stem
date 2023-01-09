from collections import Counter

# List of numbers
numbers = [0,0,0,0,0,0,0,3,3,6,10]

# Create a Counter object
counter = Counter(numbers)

# Find the mode
mode = counter.most_common(1)

# Print the mode
print(mode)
