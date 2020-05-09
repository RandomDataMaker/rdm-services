import numpy as np
import matplotlib.pyplot as plt

mu, sigma = 0, 0.1

s = []
for i in range(1000):
    v = np.random.normal(mu, sigma, 1)
    print(v)
    s.append(v[0])

count, bins, ignored = plt.hist(s, 1000, density=True)
plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) * np.exp( - (bins - mu)**2 / (2 * sigma**2) ), linewidth=2, color='r')

plt.show()
