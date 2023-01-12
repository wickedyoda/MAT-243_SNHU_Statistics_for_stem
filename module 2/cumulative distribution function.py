import scipy.stats

dist = scipy.stats.norm(0, 1)  # mean = 0, standard deviation = 1

x = 1
cdf = dist.cdf(x)
print(cdf)  # 0.8413447460685429

p = 0.8
value = dist.ppf(p)
print(value)  # 0.8416212335729143
