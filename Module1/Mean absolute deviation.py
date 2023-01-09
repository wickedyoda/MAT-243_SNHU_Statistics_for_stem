from statistics import mean
def mad(data):
    return sum(abs(x - mean(data)) for x in data) / len(data)


numbers = [1, 2, 4, 5]
mean_absolute_deviation = mad(numbers)

print(mean_absolute_deviation)  # Output: 1.4
