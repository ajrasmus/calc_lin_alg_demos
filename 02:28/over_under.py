import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'

eps = 0.5

fig = plt.figure(figsize=plt.figaspect(1))

plt.subplots_adjust(hspace=0.5, wspace=0.5)

ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.set_aspect('auto')

x1 = np.arange(-5, 5, 1)
y1 = np.arange(-5, 5, 1)
X1, Y1 = np.meshgrid(x1, y1)
Z1 = 1 - 2 * X1 - 3 * Y1
ax1.plot_surface(X1, Y1, Z1, alpha=0.5, color='blue')
ax1.text(-4, -4, 30, r'$2x+3y+z=1$', color='blue')

x2 = np.arange(-5, 5, 1)
y2 = np.arange(-5, 5, 1)
X2, Y2 = np.meshgrid(x2, y2)
Z2 = 1 / 5 * (2 - 4 * X2 - Y2)
ax1.plot_surface(X2, Y2, Z2, alpha=0.5, color='green')
ax1.text(-4, -2.5, -35, r'$4x+y+5z=2$', color='green')

x3 = np.arange(-5, 5, 1)
y3 = 3 / 14 - 3 * x3 / 7
z3 = 5 / 14 - 5 * x3 / 7
ax1.plot(x3, y3, z3, color='black')

ax1.set_title(
    r'$\begin{pmatrix} 2&3&1\\4&1&5\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}1\\2\end{pmatrix}$')
ax1.axes.xaxis.set_ticklabels([])
ax1.axes.yaxis.set_ticklabels([])
ax1.axes.zaxis.set_ticklabels([])
ax1.grid(False)

ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.set_aspect('auto')

x1 = np.arange(-5, 5, 1)
y1 = np.arange(-5, 5, 1)
X1, Y1 = np.meshgrid(x1, y1)
Z1 = -10 - 2 * X1 - 3 * Y1
ax2.plot_surface(X1, Y1, Z1, alpha=0.5, color='blue')

x2 = np.arange(-5, 5, 1)
y2 = np.arange(-5, 5, 1)
X2, Y2 = np.meshgrid(x2, y2)
Z2 = 10 - 2 * X2 - 3 * Y2
ax2.plot_surface(X2, Y2, Z2, alpha=0.5, color='green')

ax2.set_title(
    r'$\begin{pmatrix} 2&3&1\\2&3&1\end{pmatrix}\begin{pmatrix}x\\y\\z\end{pmatrix}=\begin{pmatrix}-10\\10\end{pmatrix}$')
ax2.axes.xaxis.set_ticklabels([])
ax2.axes.yaxis.set_ticklabels([])
ax2.axes.zaxis.set_ticklabels([])
ax2.grid(False)

ax3 = fig.add_subplot(2, 2, 3)
ax3.set_aspect('auto')


x1 = np.arange(-5, 5, 1)
y1 = 1 / 2 * (1 - x1)
ax3.plot(x1, y1, alpha=0.7, color='blue')
ax3.text(-4, -0.5, r'$x+2y=1$', color='blue')

x2 = np.arange(-5, 5, 1)
y2 = 1 / 4 * (3 - 3 * x2)
ax3.plot(x2, y2, alpha=0.7, color='green')
ax3.text(-3, 3.5, r'$3x+4y=3$', color='green')


x3 = np.arange(-5, 5, 1)
y3 = (10 + x3) / 5
ax3.plot(x3, y3, alpha=0.7, color='red')
ax3.text(0, 1.5, r'$-x+5y=10$', color='red')

ax3.set_title(
    r'$\begin{pmatrix} 1&2\\3&4\\-1&5\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}1\\3\\10\end{pmatrix}$')
ax3.axes.xaxis.set_ticklabels([])
ax3.axes.yaxis.set_ticklabels([])
ax3.grid(False)

ax4 = fig.add_subplot(2, 2, 4)
ax4.set_aspect('auto')

x1 = np.arange(-5, 5, 1)
y1 = 1 / 2 * (1 - x1)
ax4.plot(x1, y1, alpha=0.7, color='blue')

x2 = np.arange(-5, 5, 1)
y2 = 1 / 4 * (3 - 3 * x2)
ax4.plot(x2, y2, alpha=0.7, color='green')

x3 = np.arange(-5, 5, 1)
y3 = x3 - 1
ax4.plot(x3, y3, alpha=0.7, color='red')

ax4.scatter(1, 0, color='black')

ax4.set_title(
    r'$\begin{pmatrix} 1&2\\3&4\\1&-1\end{pmatrix}\begin{pmatrix}x\\y\end{pmatrix}=\begin{pmatrix}1\\3\\1\end{pmatrix}$')
ax4.axes.xaxis.set_ticklabels([])
ax4.axes.yaxis.set_ticklabels([])
ax4.grid(False)

plt.savefig('over_under.pdf', format='pdf', bbox_inches='tight')
plt.savefig('over_under.png', format='png', bbox_inches='tight')
