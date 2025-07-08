import numpy as np
import matplotlib.pyplot as plt

ax = plt.gca()
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)

X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2

levels = np.arange(-25, 25, 5)

contour = ax.contour(X, Y, Z, colors='blue',
                     linestyles='solid', levels=levels, alpha=0.5)
fmt = {level: int(level) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True,
          fmt=fmt, manual=[(5, 0), (4, 0), (3, 0),
                           (-5, 0), (-4, 0), (-3, 0), (-2, 0),
                           (0, -5), (0, -4), (0, -3), (0, -2),
                           (0, 5), (0, 4), (0, 3), (0, 2), (0, 1)])
plt.savefig('saddle_contour.pdf', format='pdf')
