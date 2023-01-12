## Problem 1
import scipy.stats

dist = scipy.stats.norm(150, 8.75)

x = 150
prob = dist.sf(x)
print(prob) # 0.5

##problem 2
import scipy.stats

dist = scipy.stats.norm(150, 8.75)
lower_bound_prob = dist.cdf(132.5)
upper_bound_prob = dist.cdf(167.5)
probability = upper_bound_prob - lower_bound_prob
print(probability)

##problem 3
import scipy.stats

dist = scipy.stats.norm(150, 8.75)

cdf = dist.cdf(160)
prob = 1 - cdf
print(prob)

##problem 4
import scipy.stats

dist = scipy.stats.norm(150, 8.75)

upper_bound = dist.cdf(170)
lower_bound = dist.cdf(165)
probability = upper_bound - lower_bound
print(probability)
