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

x = np.arange(-2.2, 2.2, 0.001)
y = np.arange(-2.2, 2.2, 0.001)

X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

ax.plot_surface(X, Y, Z, alpha=0.9, linewidth=0.5)
plt.savefig('sinx2+y2.pdf', format='pdf')

ax.cla()
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])


x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.sin(Y)
ax.plot_surface(X, Y, Z, alpha=0.9, linewidth=0.5)
plt.savefig('sinxsiny.pdf', format='pdf')

ax.cla()
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])


x = np.arange(-10, 10, 0.01)
y = np.arange(-10, 10, 0.01)

X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2

ax.plot_surface(X, Y, Z, alpha=0.9, linewidth=0.5)
plt.savefig('x2-y2.pdf', format='pdf')

ax.cla()
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])


x = np.arange(-10, 10, 0.01)
y = np.arange(-10, 10, 0.01)

X, Y = np.meshgrid(x, y)
Z = X * np.exp(-Y)
ax.plot_surface(X, Y, Z, alpha=0.9, linewidth=0.5)
plt.savefig('xexp-y.pdf', format='pdf')

ax.cla()
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])


x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)

X, Y = np.meshgrid(x, y)
Z = np.sin(X + Y)
ax.plot_surface(X, Y, Z, alpha=0.9, linewidth=0.5)

plt.savefig('sinx+y.pdf', format='pdf')
