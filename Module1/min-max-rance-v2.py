import pandas as pd
scores = ('3,5,8,1,−6,4')

# Calculating the range by subtracting the minimum from the maximum
score_range = scores.max() - scores.min()
print(score_range)

# Defining a function that can be used repeatedly
def range_of_scores(x):
  return x.max() - x.min()
print(range_of_scores(scores))
