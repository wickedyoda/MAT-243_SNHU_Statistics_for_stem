import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t < -0.25)?
print(st.t.cdf(-0.25, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t < 1.5)?
print(st.t.cdf(1.5, 30, 0, 1))

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t > -0.25)?
print(st.t.sf(-0.25, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(t > 1.5)?
print(st.t.sf(1.5, 30, 0, 1))

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(-0.25 < t < 1.5)?
print(st.t.cdf(1.5, 30, 0, 1) - st.t.cdf(-0.25, 30, 0, 1))

# For a t-distribution, if the degrees of freedom is 30, the mean is 0,
# and the standard deviation is 1, what is P(1.5 < t < 2.85)?
print(st.t.cdf(2.85, 30, 0, 1) - st.t.cdf(1.5, 30, 0, 1))

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 59, the mean is 55,
# and the standard deviation is 7.5, what is P(t < 62)?
print(st.t.cdf(62, 59, 55, 7.5))

# For a t-distribution, if the degrees of freedom is 34, the mean is 55,
# and the standard deviation is 7.5, what is P(t > 51)?
print(st.t.sf(51, 34, 55, 7.5))

# For a t-distribution, if the degrees of freedom is 59, the mean is 55,
# and the standard deviation is 7.5, what is P(49 < t < 60)?
print(st.t.cdf(60, 59, 55, 7.5) - st.t.cdf(49, 59, 55, 7.5))
