import numpy as np
import matplotlib.pyplot as plt

ax = plt.gca()

ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

x = np.arange(-10, 10, 0.01)
y = np.arange(-10, 10, 0.01)

X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2

levels = np.arange(-50, 51, 25)

contour = ax.contour(X, Y, Z, colors='blue',
                     linestyles='solid', levels=levels, alpha=0.7)
plt.savefig('x2-y25contour.pdf', format='pdf')
