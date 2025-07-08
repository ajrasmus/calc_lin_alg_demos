import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2, 2, 0.001)
y = np.arange(-2, 2, 0.001)

X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

levels = np.arange(-1, 1.1, 0.2)

ax = plt.gca()

ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

contour = ax.contour(X, Y, Z, colors='blue',
                     linestyles='solid', levels=levels, alpha=0.5)
plt.savefig('sinx2+y2contour.pdf', format='pdf')

ax.cla()
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)

X, Y = np.meshgrid(x, y)
Z = np.sin(X) * np.sin(Y)

levels = np.arange(-1, 1.1, 0.1)

contour = ax.contour(X, Y, Z, colors='blue',
                     linestyles='solid', levels=levels, alpha=0.5)
plt.savefig('sinxsinycontour.pdf', format='pdf')

ax.cla()
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

x = np.arange(-10, 10, 0.01)
y = np.arange(-10, 10, 0.01)

X, Y = np.meshgrid(x, y)
Z = X**2 - Y**2

levels = np.arange(-100, 110, 20)

contour = ax.contour(X, Y, Z, colors='blue',
                     linestyles='solid', levels=levels, alpha=0.5)
plt.savefig('x2-y2contour.pdf', format='pdf')


ax.cla()
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

x = np.arange(-2, 2, 0.01)
y = np.arange(-2, 2, 0.01)

X, Y = np.meshgrid(x, y)
Z = X * np.exp(-Y)

levels = np.arange(-2.5, 2.6, 0.1)

contour = ax.contour(X, Y, Z, colors='blue',
                     linestyles='solid', levels=levels, alpha=0.5)
plt.savefig('xexp-ycontour.pdf', format='pdf')


ax.cla()
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

x = np.arange(-5, 5, 0.01)
y = np.arange(-5, 5, 0.01)

X, Y = np.meshgrid(x, y)
Z = np.sin(X + Y)
levels = np.arange(-1, 1.1, 0.2)

contour = ax.contour(X, Y, Z, colors='blue',
                     linestyles='solid', levels=levels, alpha=0.5)

plt.savefig('sinx+ycontour.pdf', format='pdf')
