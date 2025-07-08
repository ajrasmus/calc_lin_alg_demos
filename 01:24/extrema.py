import numpy as np
import matplotlib.pyplot as plt

ax = plt.gca()
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

x = np.arange(-2, 2, 0.001)
y = np.arange(-2, 2, 0.001)

X, Y = np.meshgrid(x, y)
Z = 5 * np.exp(-X**2 - 2 * Y**2) * np.sin(2 * X) * np.sin(Y)

levels = np.arange(-5, 5.1, 0.19)

contour = ax.contour(X, Y, Z, colors='blue',
                     linestyles='solid', levels=levels, alpha=0.5)

fmt = {level: level.round(2) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True, fmt=fmt)

plt.savefig('extrema.pdf', format='pdf')

plt.show()
