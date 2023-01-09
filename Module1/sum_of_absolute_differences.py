from statistics import mean

data = [1, 2, 4, 5]
mean_of_data = mean(data)
sum_of_absolute_differences = sum(abs(x - mean_of_data) for x in data)

print(sum_of_absolute_differences)  # Output: 5
