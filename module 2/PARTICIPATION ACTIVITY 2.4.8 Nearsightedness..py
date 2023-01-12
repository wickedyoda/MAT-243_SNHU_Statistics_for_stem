#problem 2
import math
p = 0.08
n = 256
std = math.sqrt(p * (1 - p) / n)
std

#problem 3
from math import comb

p = 0.08
q = 0.92
n = 256
k = 23

probability = 0

for i in range(23, n + 1):
    probability += comb(n, i) * (p ** i) * (q ** (n - i))

probability
