##problem 1
import scipy.stats

dist = scipy.stats.norm(150, 8.75)
score = dist.ppf(0.40)
print(score)

#Problem2
import scipy.stats

dist = scipy.stats.norm(150, 8.75)
value = dist.ppf(0.8)
print(value)
