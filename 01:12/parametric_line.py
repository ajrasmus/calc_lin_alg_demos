import numpy as np
import matplotlib.pyplot as plt

pt = np.array([[2], [2]])
parallel = np.array([[3], [-2]])
pts_on_line = [pt + n * parallel for n in range(-3, 3, 1)]
scatter_X = [p[0, 0] for p in pts_on_line]
scatter_Y = [p[1, 0] for p in pts_on_line]

plt_X = np.arange(-8, 8, 0.1)
plt_Y = 10 / 3 - 2 / 3 * plt_X

offset = 0.5

ax = plt.gca()
ax.set_aspect('equal')
ax.set_axisbelow(True)
ax.grid()
ax.scatter(scatter_X, scatter_Y)
ax.plot(plt_X, plt_Y, color='black')
ax.arrow(0, 0, 0.8 * pt[0, 0], 0.8 * pt[1, 0],
         width=0.03, label='$\mathbf{p}$', color='green')
ax.annotate('$\mathbf{p}$',
            (0.4 * pt[0, 0] + offset, 0.4 * pt[1, 0]), color='green')
ax.annotate('$\mathbf{v}$', ((pt + 0.5 * parallel)
                             [0, 0] + offset, (pt + 0.5 * parallel)[1, 0] + 2 * offset), color='red')
for (x, y) in list(zip(scatter_X, scatter_Y))[:-1]:
    ax.arrow(x + offset, y + offset,
             0.9 * parallel[0, 0], 0.9 * parallel[1, 0], width=0.03, label='$\mathbf{v}$', color='red')
plt.title('The line $2x+3y=10$ in $\mathbb{R}^2$')
plt.savefig('line.pdf', format='pdf')
plt.show()
