from scipy.stats import binom

n = 5
p = 0.3
rv = binom(n, p)

x = range(n+1)
pmf = rv.pmf(x)
print(pmf)
