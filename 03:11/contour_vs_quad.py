import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'


def f(x, y): return (3 * x**4 - 8 * x**3 - 6 * x**2 + 24 * x - 6 * y**2) / 5
def g(x, y): return (36 * x**2 - 48 * x - 12) / 5
def h(x, y): return -12 / 5
def A(a, b, x, y): return g(a, b) * x**2 + h(a, b) * y**2


eps = 0.5

x1 = -1 + np.arange(-eps, eps, 0.005)
y1 = 0 + np.arange(-eps, eps, 0.005)
X1, Y1 = np.meshgrid(x1, y1)
Z1 = f(X1, Y1)
x1_ = np.arange(-eps, eps, 0.005)
y1_ = np.arange(-eps, eps, 0.005)
X1_, Y1_ = np.meshgrid(x1_, y1_)
Q1 = A(-1, 0, X1_, Y1_)

x2 = 1 + np.arange(-eps, eps, 0.005)
y2 = 0 + np.arange(-eps, eps, 0.005)
X2, Y2 = np.meshgrid(x2, y2)
Z2 = f(X2, Y2)
x2_ = np.arange(-eps, eps, 0.005)
y2_ = np.arange(-eps, eps, 0.005)
X2_, Y2_ = np.meshgrid(x2_, y2_)
Q2 = A(1, 0, X2_, Y2_)

x3 = 2 + np.arange(-eps, eps, 0.005)
y3 = 0 + np.arange(-eps, eps, 0.005)
X3, Y3 = np.meshgrid(x3, y3)
Z3 = f(X3, Y3)
x3_ = np.arange(-eps, eps, 0.005)
y3_ = np.arange(-eps, eps, 0.005)
X3_, Y3_ = np.meshgrid(x3_, y3_)
Q3 = A(2, 0, X3_, Y3_)

ax = plt.gca()

contour = ax.contour(X1, Y1, Z1, levels=np.arange(-20, 20, 0.2), colors='blue',
                     linestyles='solid')
ax.scatter(-1, 0, color='green', alpha=1.0, zorder=10)
fmt = {level: round(level, 1) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True, fmt=fmt)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
plt.savefig('contour1.pdf', format='pdf', bbox_inches='tight')

plt.clf()

ax = plt.gca()
contour = ax.contour(X1_, Y1_, Q1, levels=np.arange(-20, 20, 0.2), colors='blue',
                     linestyles='solid')
ax.scatter(0, 0, color='black', alpha=1.0, zorder=10)
fmt = {level: round(level, 1) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True, fmt=fmt)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
plt.savefig('quad1.pdf', format='pdf', bbox_inches='tight')

plt.clf()

ax = plt.gca()
contour = ax.contour(X2, Y2, Z2, levels=np.arange(-20, 20, 0.2), colors='blue',
                     linestyles='solid')
ax.scatter(1, 0, color='black', alpha=1.0, zorder=10)
fmt = {level: round(level, 1) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True, fmt=fmt)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
plt.savefig('contour2.pdf', format='pdf', bbox_inches='tight')

plt.clf()

ax = plt.gca()
contour = ax.contour(X2_, Y2_, Q2, levels=np.arange(-20, 20, 0.2), colors='blue',
                     linestyles='solid')
ax.scatter(0, 0, color='black', alpha=1.0, zorder=10)
fmt = {level: round(level, 1) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True, fmt=fmt)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
plt.savefig('quad2.pdf', format='pdf', bbox_inches='tight')

plt.clf()

ax = plt.gca()
contour = ax.contour(X3, Y3, Z3, levels=np.arange(-20, 20, 0.2), colors='blue',
                     linestyles='solid')
ax.scatter(2, 0, color='red', alpha=1.0, zorder=10)
fmt = {level: round(level, 1) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True, fmt=fmt)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
plt.savefig('contour3.pdf', format='pdf', bbox_inches='tight')

plt.clf()

ax = plt.gca()
contour = ax.contour(X3_, Y3_, Q3, levels=np.arange(-20, 20, 0.2), colors='blue',
                     linestyles='solid')
ax.scatter(0, 0, color='black', alpha=1.0, zorder=10)
fmt = {level: round(level, 1) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True, fmt=fmt)
ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')
plt.savefig('quad3.pdf', format='pdf', bbox_inches='tight')
