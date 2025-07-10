import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'

plt.grid(False)

fig = plt.figure()

ax = fig.add_subplot(projection='3d')
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

x = np.arange(-1.5, -0.5, 0.005)
y = np.arange(-0.5, 0.5, 0.005)

X, Y = np.meshgrid(x, y)
Z = (3 * X**4 - 8 * X**3 - 6 * X**2 + 24 * X - 6 * Y**2) / 5
x3 = -1
y3 = 0
z3 = (3 * x3**4 - 8 * x3**3 - 6 * x3**2 + 24 * x3 - 6 * y3**2) / 5

liney1 = np.arange(-0.5, 0.5, 0.005)
linex1 = -1 * np.ones(liney1.shape)
linez1 = (3 * linex1**4 - 8 * linex1**3 - 6 *
          linex1**2 + 24 * linex1 - 6 * liney1**2) / 5

linex2 = np.arange(-1.5, -0.5, 0.005)
liney2 = np.zeros(linex2.shape)
linez2 = (3 * linex2**4 - 8 * linex2**3 - 6 *
          linex2**2 + 24 * linex2 - 6 * liney2**2) / 5

linex3 = np.array([x3]) + np.arange(-0.2, 0.2, 0.005)
liney3 = np.array([y3]) + np.sqrt(6) * np.arange(-0.2, 0.2, 0.005)
linez3 = (3 * linex3**4 - 8 * linex3**3 - 6 *
          linex3**2 + 24 * linex3 - 6 * liney3**2) / 5

ax.set_aspect('equal')
ax.view_init(azim=70)
ax.plot_surface(X, Y, Z, linewidth=0, color='blue', alpha=0.5)
ax.scatter([x3], [y3], [z3], color='black', zorder=30,
           alpha=1.0)
ax.plot(linex1, liney1, linez1, color='red', zorder=20, alpha=1.0)
ax.plot(linex2, liney2, linez2, color='green', zorder=20, alpha=1.0)
ax.plot(linex3, liney3, linez3, color='orange', zorder=20, alpha=1.0)
plt.savefig('zoomed.pdf', format='pdf', bbox_inches='tight')

plt.clf()

new_ax = fig.add_subplot()
new_ax.scatter([x3], [y3], color='black', zorder=10)
contour = new_ax.contour(X, Y, Z, levels=np.arange(-20, 20, 0.1), colors='blue',
                         linestyles='solid')
fmt = {level: round(level, 1) for level in contour.levels}
new_ax.clabel(contour, contour.levels, inline=True, fmt=fmt)
new_ax.set_xticks([])
new_ax.set_yticks([])
new_ax.set_aspect('equal')
new_ax.plot(linex1, liney1, color='red', linewidth=3)
new_ax.plot(linex2, liney2, color='green', linewidth=3)
new_ax.plot(linex3, liney3, color='orange', linewidth=3)
new_ax.set_title(r'Three lines through $\mathbf a$')
plt.savefig('contour_zoomed.pdf', format='pdf', bbox_inches='tight')

plt.clf()

new_new_ax = fig.add_subplot()
new_new_ax.plot(liney1, linez1, color='red')
new_new_ax.scatter(y3, z3, color='black', zorder=10)
new_new_ax.set_title(r'$f$ has a local max restricted to the line $L$')
plt.savefig('graph1.pdf', format='pdf', bbox_inches='tight')

plt.clf()

new_new_new_ax = fig.add_subplot()
new_new_new_ax.plot(linex2, linez2, color='green')
new_new_new_ax.scatter(x3, z3, color='black', zorder=10)
new_new_new_ax.set_title(r"$f$ has a local min restricted to the line $L'$")
plt.savefig('graph2.pdf', format='pdf', bbox_inches='tight')

plt.clf()

new_new_new_new_ax = fig.add_subplot()
new_new_new_new_ax.plot(linex3, linez3, color='orange')
new_new_new_new_ax.scatter(x3, z3, color='black', zorder=10)
new_new_new_new_ax.set_title(
    r"$f$ has neither a local max nor min on the third line")
plt.savefig('graph3.pdf', format='pdf', bbox_inches='tight')
