#problem 2
from math import sqrt

sample_mean = 3.26
population_mean = 1.86
sample_std = 2.12
sample_size = 15

z = (sample_mean - population_mean) / (sample_std / sqrt(sample_size))
print(z)

#problem 3
from scipy.stats import norm

mean = 1.86
std = 0.26
x = 3.26

probability = norm.cdf( (x - mean) / std )
probability
print(probability)

#problem 4
from math import sqrt

x_bar = 2.72
mu = 1.86
s = 2.12
n = 15

z_statistic = (x_bar - mu) / (s / sqrt(n))

print(z_statistic)

#problem 5

