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


def f(x, y): return x**2 + x - y**2


x = np.arange(-1.5, 1.5, 0.01)
y = np.arange(-1.5, 1.5, 0.01)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

curve_x = np.arange(-1, 1, 0.0001)
curve_y_top = np.sqrt(1 - curve_x**2)
curve_y_bottom = -np.sqrt(1 - curve_x**2)
curve_z_top = f(curve_x, curve_y_top)
curve_z_bottom = f(curve_x, curve_y_bottom)

xs = [-1 / 2, -1 / 4, -1 / 4, 1, -1]
ys = [0, np.sqrt(15) / 4, -np.sqrt(15) / 4, 0, 0]
zs = list(map(f, xs, ys))
ax.set_aspect('equal')
# ax.view_init(azim=20)
ax.plot_surface(X, Y, Z, linewidth=0, alpha=0.5)
ax.plot(curve_x, curve_y_top, curve_z_top, color='black')
ax.plot(curve_x, curve_y_bottom, curve_z_bottom, color='black')
ax.scatter(xs, ys, zs, color='red')

plt.title('Extreme points of $f(x,y)=x+x^2-y^2$ on the unit disk')
plt.savefig('harmonic_extrema.pdf', format='pdf')
plt.savefig('harmonic_extrema.png', format='png')
