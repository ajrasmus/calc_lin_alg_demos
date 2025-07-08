import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator

ax = plt.figure().add_subplot(projection='3d')

x = np.arange(-3, 3, 1)
y = np.arange(-3, 3, 1)

X, Y = np.meshgrid(x, y)

Z = 0 * X + 0.5 * Y

ax.plot_surface(X, Y, Z, color='blue', alpha=0.5)
ax.quiver(0, 0, 0, 0, -1, 2, color='black')
ax.quiver(0, 0, 0, 0, 2, 1, color='black')
ax.quiver(0, 0, 0, 2, 0, 0, color='black')
ax.view_init(azim=15, elev=40)
ax.set_xlabel('x')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_ylabel('y')
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_zlabel('z')
ax.zaxis.set_major_locator(MaxNLocator(integer=True))
plt.savefig('normal_plane.pdf', format='pdf')

plt.show()
