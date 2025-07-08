import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = [-4, 4]
Y = [-2, 2]

vec = np.array([[1], [3]])
base = np.array([[2], [1]])
proj = (np.dot(vec.T, base) / np.dot(base.T, base)) * base
perp = vec - proj

ax = plt.gca()
ax.set_aspect('equal')
ax.scatter(proj[0, 0], proj[1, 0], color='black')
ax.plot(X, Y)
ax.plot([proj[0, 0], vec[0, 0]], [proj[1, 0], vec[1, 0]], '--', color='black')
ax.arrow(0, 0, 1, 3, width=0.02, color='black')
ax.axis('off')
plt.savefig('proj.pdf', format='pdf')
