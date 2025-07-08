import numpy as np
import matplotlib.pyplot as plt
import math

n = int(1e7)
num = 0
X = np.arange(n)
Z = np.zeros((n))

np.random.seed(42)

for i in range(n):
    Z[i] = num
    num += np.random.choice([-1, 1])

Y = Z / math.sqrt(n)

plt.plot(X, Y, lw=0.3)
plt.title('Brownian motion')
plt.savefig('brownian.pdf', format='pdf')
