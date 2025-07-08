import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator

plt.grid(False)

ax = plt.figure().add_subplot(projection='3d')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

x = np.arange(-1.5, 1.5, 0.01)
y = np.arange(-1.5, 1.5, 0.01)
X, Y = np.meshgrid(x, y)
Z = X**3

ys = np.arange(-1.5, 1.5, 0.01)
xs = np.zeros(ys.shape)
zs = xs**3

ax.plot_surface(X, Y, Z, alpha=0.5)
ax.plot(xs, ys, zs, color='black')
plt.title('A line of critical points')
plt.savefig('critical_line.pdf', format='pdf')
