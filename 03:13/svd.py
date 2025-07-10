import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import patches
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator
mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'

U = np.array([[1, 2], [2, -1]]) / np.sqrt(5)
S = np.array([[3, 0], [0, 2]])
V = np.array([[2, 1], [1, -2]]) / np.sqrt(5)
U_angle = np.arccos(U[0, 0])

u1 = np.array([1, 2]) / np.sqrt(5)
u2 = np.array([2, -1]) / np.sqrt(5)

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.tight_layout(h_pad=5)

ax1.set_aspect('equal')
ax2.set_aspect('equal')
ax3.set_aspect('equal')
ax4.set_aspect('equal')
ax1.set_xlim(-3.1, 3.1)
ax1.set_ylim(-3.1, 3.1)
ax2.set_xlim(-3.1, 3.1)
ax2.set_ylim(-3.1, 3.1)
ax3.set_xlim(-3.1, 3.1)
ax3.set_ylim(-3.1, 3.1)
ax4.set_xlim(-3.1, 3.1)
ax4.set_ylim(-3.1, 3.1)

ax1.set_title(
    r'Unit circle with $\mathbf e_1,\mathbf e_2$')
ax1.plot([0, 1], [0, 0], color='blue')
ax1.plot([0, 0], [0, 1], color='green')
e1 = patches.Ellipse((0, 0), 2, 2, angle=0, linewidth=1, fill=False)
ax1.add_patch(e1)

ax3.set_title(
    r"After applying $(Q')^T=\frac{1}{\sqrt{5}}\begin{pmatrix} 2 & 1 \\ 1 & -2\end{pmatrix}$")
ax3.plot([0, V.T[0, 0]], [0, V.T[1, 0]], color='blue')
ax3.plot([0, V.T[0, 1]], [0, V.T[1, 1]], color='green')
e3 = patches.Ellipse((0, 0), 2, 2, angle=0, linewidth=1, fill=False)
ax3.add_patch(e3)

ax4.set_title(
    r"After applying $D=\begin{pmatrix} 3 & 0 \\ 0 & 2 \end{pmatrix}$")
ax4.plot([0, np.dot(S, V.T)[0, 0]], [0, np.dot(S, V.T)[1, 0]], color='blue')
ax4.plot([0, np.dot(S, V.T)[0, 1]], [0, np.dot(S, V.T)[1, 1]], color='green')
e4 = patches.Ellipse((0, 0), 6, 4, angle=0, linewidth=1, fill=False)
ax4.add_patch(e4)

ax2.set_title(
    r"After applying $Q=\frac{1}{\sqrt{5}}\begin{pmatrix} 1 & 2 \\ 2 & -1 \end{pmatrix}$")
ax2.plot([0, np.dot(U, np.dot(S, V.T))[0, 0]],
         [0, np.dot(U, np.dot(S, V.T))[1, 0]], color='blue')
ax2.plot([0, np.dot(U, np.dot(S, V.T))[0, 1]],
         [0, np.dot(U, np.dot(S, V.T))[1, 1]], color='green')
e2 = patches.Ellipse((0, 0), 6, 4, angle=(180 / np.pi)
                     * U_angle, linewidth=1, fill=False)
ax2.add_patch(e2)

plt.savefig('SVD.pdf', format='pdf', bbox_inches='tight')
