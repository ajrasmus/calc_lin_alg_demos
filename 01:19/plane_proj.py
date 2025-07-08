import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator


vec = np.array([[1], [6], [8]])
base_1 = np.array([[1], [0], [0]])
base_2 = np.array([[0], [1], [0]])
proj = (np.dot(vec.T, base_1) / np.dot(base_1.T, base_1)) * base_1 + \
    (np.dot(vec.T, base_2) / np.dot(base_2.T, base_2)) * base_2
diff = vec - proj

ax = plt.figure().add_subplot(projection='3d')

x = np.arange(-10, 10, 1)
y = np.arange(-10, 10, 1)

X, Y = np.meshgrid(x, y)
Z = 0 * X + 0 * Y


eps = 1e-16
ax.axes.set_xlim3d(left=-8. - eps, right=8. + eps)
ax.axes.set_ylim3d(bottom=-8. - eps, top=8. + eps)
ax.axes.set_zlim3d(bottom=-8. - eps, top=8. + eps)

ax.set_xlabel('x')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_ylabel('y')
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_zlabel('z')
ax.zaxis.set_major_locator(MaxNLocator(integer=True))

ax.quiver(0, 0, 0, vec[0, 0], vec[1, 0], vec[2, 0], color='black')
ax.scatter(proj[0], proj[1], proj[2], color='black')
ax.plot_surface(X, Y, Z, color='blue', alpha=0.5)
ax.plot([proj[0, 0], vec[0, 0]], [proj[1, 0],
                                  vec[1, 0]], [proj[2, 0], vec[2, 0]], '--', color='black')
ax.view_init(azim=25, elev=20)
plt.savefig('proj_plane.pdf', format='pdf')

plt.show()
