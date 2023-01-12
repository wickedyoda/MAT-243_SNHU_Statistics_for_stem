import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 49, the mean is 0 and
# the standard deviation is 1, what is t* if P(t < t*) = 0.135?
print(st.t.ppf(0.135, 49, 0, 1))

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 49, the mean is 0 and
# the standard deviation is 1, what is t* if P(t > t*) = 0.405?
print(st.t.isf(0.405, 49, 0, 1))

import scipy.stats as st

# For a t-distribution, if the degrees of freedom is 24, the mean is 55 and
# the standard deviation is 7.5, what is t* if P(t < t*) = 0.8247?
print(st.t.ppf(0.8247, 24, 55, 7.5))

# For a t-distribution, if the degrees of freedom is 24, the mean is 55 and
# the standard deviation is 7.5, what is t* if P(t > t*) = 0.95?
print(st.t.isf(0.95, 24, 55, 7.5))