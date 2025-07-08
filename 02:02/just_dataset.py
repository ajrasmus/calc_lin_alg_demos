import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
eps = 1
num_pts = 1000
X = 5 * np.random.rand(num_pts)
Y = 2 * np.sin(3 * X + 2) + (2 * np.random.rand(num_pts) - 1) * eps

plt.scatter(X, Y, color='blue', alpha=0.5)
plt.savefig('dataset.pdf', format='pdf')
