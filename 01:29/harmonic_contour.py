import numpy as np
import matplotlib.pyplot as plt

ax = plt.gca()

ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])


def f(x, y): return x**2 + x - y**2


x = np.arange(-1.5, 1.5, 0.01)
y = np.arange(-1.5, 1.5, 0.01)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

xs = [-1 / 2, -1 / 4, -1 / 4, 1, -1]
ys = [0, np.sqrt(15) / 4, -np.sqrt(15) / 4, 0, 0]
zs = list(map(f, xs, ys))

levels = np.arange(-5, 5.5, 0.5)
levels = np.append(levels, zs)
levels = np.unique(levels)
levels = np.sort(levels)

curve_x = np.arange(-1, 1, 0.0001)
curve_y_top = np.sqrt(1 - curve_x**2)
curve_y_bottom = -np.sqrt(1 - curve_x**2)

ax.scatter(xs, ys, color='red')

contour = ax.contour(X, Y, Z, colors='blue',
                     linestyles='solid', levels=levels, alpha=0.7)

ax.plot(curve_x, curve_y_top, color='black')
ax.plot(curve_x, curve_y_bottom, color='black')

plt.title('A contour plot for $f(x,y)=x+x^2-y^2$')
plt.savefig('harmonic_contour.pdf', format='pdf')
