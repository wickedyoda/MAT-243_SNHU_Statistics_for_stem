#problem 1
mean_population = 172
mean_sampling_distribution = mean_population
print(mean_sampling_distribution)

#problem 2
import math
population_standard_deviation = 29
sample_size = 36
standard_error = population_standard_deviation / math.sqrt(sample_size)
print(standard_error)

#problem 3
import math
import scipy.stats

sigma = 29 / math.sqrt(36)
dist = scipy.stats.norm(172, sigma)
value = dist.cdf(180)
print(value)
