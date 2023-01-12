import scipy.stats as st

# For a normal distribution, if the mean is 0 and
# the standard deviation is 1, what is z* if P(z < z*) = 0.135?
print(st.norm.ppf(0.135, 0, 1))

# For a normal distribution, if the mean is 0 and
# the standard deviation is 1, what is z* if P(z > z*) = 0.405?
print(st.norm.isf(0.405, 0, 1))

# For a normal distribution, if the mean is 55 and
# the standard deviation is 7.5, what is x* if P(x < x*) = 0.8247?
print(st.norm.ppf(0.8247, 55, 7.5))

# For a normal distribution, if the mean is 55 and
# the standard deviation is 7.5, what is x* if P(x > x*) = 0.95?
print(st.norm.isf(0.95, 55, 7.5))