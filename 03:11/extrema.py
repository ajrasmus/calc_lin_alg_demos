import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator

plt.grid(False)

fig = plt.figure()

ax = fig.add_subplot(projection='3d')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

x = np.arange(-1.75, 2.75, 0.01)
y = np.arange(-1.75, 2.75, 0.01)

X, Y = np.meshgrid(x, y)
Z = (3 * X**4 - 8 * X**3 - 6 * X**2 + 24 * X - 6 * Y**2) / 5
x1 = 1
x2 = 2
x3 = -1
y1, y2, y3 = 0, 0, 0
z1 = (3 * x1**4 - 8 * x1**3 - 6 * x1**2 + 24 * x1 - 6 * y1**2) / 5
z2 = (3 * x2**4 - 8 * x2**3 - 6 * x2**2 + 24 * x2 - 6 * y2**2) / 5
z3 = (3 * x3**4 - 8 * x3**3 - 6 * x3**2 + 24 * x3 - 6 * y3**2) / 5


ax.set_aspect('equal')
ax.view_init(azim=60)
ax.plot_surface(X, Y, Z, linewidth=0, color='blue', alpha=0.5)
ax.scatter([x1, x2, x3], [y1, y2, y3], [z1, z2, z3], color='black', zorder=10,
           alpha=1.0)
plt.savefig('graph.pdf', format='pdf', bbox_inches='tight')

plt.clf()

new_ax = fig.add_subplot()
new_ax.scatter(x1, y1, color='black', zorder=10)
new_ax.scatter(x2, y2, color='red', zorder=10)
new_ax.scatter(x3, y3, color='green', zorder=10)
contour = new_ax.contour(X, Y, Z, levels=np.arange(-20, 20, 1), colors='blue',
                         linestyles='solid')
fmt = {level: int(level) for level in contour.levels}
new_ax.clabel(contour, contour.levels, inline=True, fmt=fmt)
new_ax.set_xticks([])
new_ax.set_yticks([])
new_ax.set_aspect('equal')
plt.savefig('contour.pdf', format='pdf', bbox_inches='tight')
