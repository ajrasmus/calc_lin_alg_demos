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

x = np.arange(-1.7, 1.7, 0.001)
y = np.arange(-8, 8, 0.001)

X, Y = np.meshgrid(x, y)
Z = np.sin(np.exp(X) * np.sin(Y))

ax.view_init(azim=-170)
ax.plot_surface(X, Y, Z, linewidth=0)
plt.title('The harmonic function $f(x,y)=e^x \sin(y)$')
plt.savefig('harmonic.pdf', format='pdf')

ax.cla()
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

x = np.arange(-10, 10, 0.01)
y = np.arange(-10, 10, 0.01)

X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2 + X**3 - 3 * X**2 * Y - 3 * X * Y**2 + Y**3

ax.set_aspect('equal')
ax.view_init(azim=20)
ax.plot_surface(X, Y, Z, linewidth=0)
plt.title('A harmonic polynomial')
plt.savefig('harmonic_2.pdf', format='pdf')
