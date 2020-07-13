import numpy as np
import matplotlib.pyplot as plt


rg = np.random.default_rng(1)

# Build a vector of 10000 normal deviates with variance sigma^2 and mean mu
mu, sigma = 2, 0.5
v = rg.normal(mu,sigma,10000)

# Plot a normalized histogram with 50 bins
plt.hist(v, bins=50, density=1)       # matplotlib version (plot)

# Compute the histogram with numpy and then plot it

(n, bins) = np.histogram(v, bins= 30, density=True)  # NumPy version (no plot)
plt.plot(.5*(bins[1:]+bins[:-1]), n)
