import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'

x = np.arange(-3, 3, 0.01)
y = np.arange(-3, 3, 0.01)
X, Y = np.meshgrid(x, y)
Z = X**2 + 4 * X * Y - 2 * Y**2

w1 = np.array([2, 1]) / np.sqrt(5)
w2 = np.array([1, -2]) / np.sqrt(5)

eps = 0.3

ax = plt.gca()
ax.set_aspect('equal')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

contour = ax.contour(X, Y, Z, levels=[-3, 0, 2],
                     linestyles='solid')
ax.scatter(w1[0], w1[1], color='black', alpha=1.0, zorder=10)
ax.scatter(w2[0], w2[1], color='black', alpha=1.0, zorder=10)
ax.plot([-5 * w1[0], 5 * w1[0]], [-5 * w1[1], 5 * w1[1]], color='blue')
ax.text(w1[0] + eps, w1[1] + eps, s=r"$\mathbf w_1'$", color='black')
ax.plot([-5 * w2[0], 5 * w2[0]], [-5 * w2[1], 5 * w2[1]], color='blue')
ax.text(w2[0] + eps, w2[1] + eps, s=r"$\mathbf w_2'$", color='black')
fmt = {level: int(level) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True, fmt=fmt)

plt.savefig('contour_example.pdf', format='pdf', bbox_inches='tight')

plt.cla()

ax = plt.gca()
ax.set_aspect('equal')
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)

x = np.arange(-3, 3, 0.01)
y = np.arange(-3, 3, 0.01)
X, Y = np.meshgrid(x, y)
Z = 2 * X**2 + 4 * X * Y + 5 * Y**2

w1 = np.array([1, 2]) / np.sqrt(5)
w2 = np.array([-2, 1]) / np.sqrt(5)

contour = ax.contour(X, Y, Z, levels=[6],
                     linestyles='solid')
ax.scatter(w1[0], w1[1], color='black', alpha=1.0, zorder=10)
ax.scatter(np.sqrt(6) * w2[0], np.sqrt(6) * w2[1],
           color='black', alpha=1.0, zorder=10)
ax.plot([-5 * w1[0], 5 * w1[0]], [-5 * w1[1], 5 * w1[1]], color='blue')
ax.text(w1[0] + 0.5, w1[1] + 0.5, s=r"$\mathbf w_1'$", color='black')
ax.plot([-5 * w2[0], 5 * w2[0]], [-5 * w2[1], 5 * w2[1]], color='blue')
ax.text(np.sqrt(6) * w2[0] - 0.5, np.sqrt(6) * w2[1] +
        0.5, s=r"$\sqrt{6}\mathbf w_2'$", color='black')
fmt = {level: int(level) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True, fmt=fmt)

plt.savefig('other_contour_example.pdf', format='pdf', bbox_inches='tight')
