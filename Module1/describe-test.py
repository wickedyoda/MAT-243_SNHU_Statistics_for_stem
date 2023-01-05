import pandas as pd

numbers = [0, -6, 10, 5, 8, 2, -12, 11, -2]

# Convert the list to a Pandas series
series = pd.Series(numbers)

# Prints the summary for the series
print(series.describe())

