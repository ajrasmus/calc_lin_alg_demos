import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator

plt.grid(False)

fig = plt.figure(figsize=(10, 8))
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
ax = fig.add_subplot(projection='3d')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

x = np.arange(-2, 2, 0.1)
y = np.arange(-2, 2, 0.1)

X, Y = np.meshgrid(x, y)
Z = 2 * X**2 + Y**2

ax.plot_surface(X, Y, Z, alpha=0.5, linewidth=0.5, zorder=0)
plt.savefig('paraboloid.pdf', format='pdf', bbox_inches='tight')

Z_new = 3 + 4 * (X - 1) + 2 * (Y - 1)

ax.plot_surface(X, Y, Z_new, alpha=0.9, linewidth=0.5, zorder=5)

ax.scatter(1, 1, 3, color='black', alpha=1, zorder=10)
plt.savefig('paraboloid_with_plane.pdf', format='pdf', bbox_inches='tight')
