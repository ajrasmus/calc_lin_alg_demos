import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['text.usetex'] = True
mpl.rcParams['text.latex.preamble'] = r'\usepackage{{amsmath}}'


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
plt.tight_layout(h_pad=5)

ax1.set_title('The usual grid')
ax1.set_xlim(-3, 3)
ax1.set_ylim(-3, 3)
ax1.set_aspect('equal')

u = np.array([1, 0])
v = np.array([0, 1])

u_mults = [a * u for a in range(-5, 5, 1)]
v_mults = [a * v for a in range(-5, 5, 1)]
linear_combos = [x + y for x in u_mults for y in v_mults]

u_line = [-10 * u, 10 * u]
v_line = [-10 * v, 10 * v]

for a in range(-5, 5, 1):
    u_trans = [a * v + x for x in u_line]
    X = [x[0] for x in u_trans]
    Y = [x[1] for x in u_trans]
    ax1.plot(X, Y, color='blue')

for a in range(-5, 5, 1):
    v_trans = [a * u + x for x in v_line]
    X = [x[0] for x in v_trans]
    Y = [x[1] for x in v_trans]
    ax1.plot(X, Y, color='blue')

X = [x[0] for x in linear_combos]
Y = [x[1] for x in linear_combos]
ax1.scatter(X, Y, color='black', s=20)

ax2.set_title(r'After applying $\begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix}$')
ax2.set_xlim(-3, 3)
ax2.set_ylim(-3, 3)
ax2.set_aspect('equal')

u = np.array([1, 2])
v = np.array([2, 1])

u_mults = [a * u for a in range(-5, 5, 1)]
v_mults = [a * v for a in range(-5, 5, 1)]
linear_combos = [x + y for x in u_mults for y in v_mults]

u_line = [-10 * u, 10 * u]
v_line = [-10 * v, 10 * v]

for a in range(-5, 5, 1):
    u_trans = [a * v + x for x in u_line]
    X = [x[0] for x in u_trans]
    Y = [x[1] for x in u_trans]
    ax2.plot(X, Y, color='blue')

for a in range(-5, 5, 1):
    v_trans = [a * u + x for x in v_line]
    X = [x[0] for x in v_trans]
    Y = [x[1] for x in v_trans]
    ax2.plot(X, Y, color='blue')

X = [x[0] for x in linear_combos]
Y = [x[1] for x in linear_combos]
ax2.scatter(X, Y, color='black', s=20)

#

ax3.set_title(
    r'After applying $\begin{pmatrix} 2 & 1 \\ 1 & 2\end{pmatrix}^{-1}$')
ax3.set_xlim(-3, 3)
ax3.set_ylim(-3, 3)
ax3.set_aspect('equal')

u = -1 / 3 * np.array([1, -2])
v = -1 / 3 * np.array([-2, 1])

u_mults = [a * u for a in range(-10, 10, 1)]
v_mults = [a * v for a in range(-10, 10, 1)]
linear_combos = [x + y for x in u_mults for y in v_mults]

u_line = [-10 * u, 10 * u]
v_line = [-10 * v, 10 * v]

for a in range(-10, 10, 1):
    u_trans = [a * v + x for x in u_line]
    X = [x[0] for x in u_trans]
    Y = [x[1] for x in u_trans]
    ax3.plot(X, Y, color='blue')

for a in range(-10, 10, 1):
    v_trans = [a * u + x for x in v_line]
    X = [x[0] for x in v_trans]
    Y = [x[1] for x in v_trans]
    ax3.plot(X, Y, color='blue')

X = [x[0] for x in linear_combos]
Y = [x[1] for x in linear_combos]
ax3.scatter(X, Y, color='black', s=20)

ax4.set_title('After applying both')
ax4.set_xlim(-3, 3)
ax4.set_ylim(-3, 3)
ax4.set_aspect('equal')

u = np.array([1, 0])
v = np.array([0, 1])

u_mults = [a * u for a in range(-5, 5, 1)]
v_mults = [a * v for a in range(-5, 5, 1)]
linear_combos = [x + y for x in u_mults for y in v_mults]

u_line = [-10 * u, 10 * u]
v_line = [-10 * v, 10 * v]

for a in range(-5, 5, 1):
    u_trans = [a * v + x for x in u_line]
    X = [x[0] for x in u_trans]
    Y = [x[1] for x in u_trans]
    ax4.plot(X, Y, color='blue')

for a in range(-5, 5, 1):
    v_trans = [a * u + x for x in v_line]
    X = [x[0] for x in v_trans]
    Y = [x[1] for x in v_trans]
    ax4.plot(X, Y, color='blue')

X = [x[0] for x in linear_combos]
Y = [x[1] for x in linear_combos]
ax4.scatter(X, Y, color='black', s=20)

plt.savefig('inverse.pdf', format='pdf', bbox_inches='tight')
plt.show()
