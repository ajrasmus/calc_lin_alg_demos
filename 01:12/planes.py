import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator

ax = plt.figure().add_subplot(projection='3d')

P = np.array([0, 0, 5])
e = np.array([-1, 0, 2])
f = np.array([0, -1, 2])

P_through_origin = [i * e + j *
                    f for i in range(0, 4, 1) for j in range(0, 4, 1)]
P_through_point = [P + v for v in P_through_origin]

ax.set_xlabel('x')
ax.xaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_ylabel('y')
ax.yaxis.set_major_locator(MaxNLocator(integer=True))
ax.set_zlabel('z')
ax.zaxis.set_major_locator(MaxNLocator(integer=True))

for pt in P_through_point:
    ax.quiver(pt[0], pt[1], pt[2], e[0], e[1], e[2], color='black')
    ax.quiver(pt[0], pt[1], pt[2], f[0], f[1], f[2], color='red')
    x = [pt[0], (pt + e)[0], (pt + e + f)[0], (pt + f)[0]]
    y = [pt[1], (pt + e)[1], (pt + e + f)[1], (pt + f)[1]]
    z = [pt[2], (pt + e)[2], (pt + e + f)[2], (pt + f)[2]]
    verts = [list(zip(x, y, z))]
    ax.add_collection3d(Poly3DCollection(verts, alpha=0.1, color='blue'))
ax.quiver(0, 0, 0, P[0], P[1], P[2], color='green')
ax.view_init(azim=35, elev=10)
plt.savefig('parametric_plane.pdf', format='pdf')
plt.savefig('parametric_plane.png', format='png')
