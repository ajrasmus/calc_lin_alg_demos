import numpy as np
import matplotlib.pyplot as plt

ax = plt.gca()

ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])


def f(x, y): return x**2 + y**2
def g(x, y): return x**2 + y**2 + xy


x = np.arange(-1.5, 1.5, 0.01)
y = np.arange(-1.5, 1.5, 0.01)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

levels = np.arange(-2, 2.5, 1 / 3)

curve_x = np.arange(-2 / np.sqrt(3), 2 / np.sqrt(3), 0.0001)
curve_y_top = 0.5 * (-1 * curve_x + np.sqrt(curve_x**2 - 4 * (curve_x**2 - 1)))
curve_y_bottom = 0.5 * \
    (-1 * curve_x - np.sqrt(curve_x**2 - 4 * (curve_x**2 - 1)))

p1 = np.array([1 / np.sqrt(3), 1 / np.sqrt(3)])
vec1 = np.array([1, 1])
vec1 = vec1 / (3 * np.linalg.norm(vec1))

p2 = -np.array([1 / np.sqrt(3), 1 / np.sqrt(3)])
vec2 = -np.array([1, 1])
vec2 = vec2 / (3 * np.linalg.norm(vec2))

p3 = np.array([1, -1])
vec3 = np.array([1, -1])
vec3 = vec3 / (3 * np.linalg.norm(vec3))

p4 = -np.array([1, -1])
vec4 = -np.array([1, -1])
vec4 = vec4 / (3 * np.linalg.norm(vec4))

for pt, vec in zip([p1, p2, p3, p4], [vec1, vec2, vec3, vec4]):
    ax.arrow(pt[0], pt[1], vec[0], vec[1], color='black', width=0.01)
    ax.scatter(pt[0], pt[1], color='red')

contour = ax.contour(X, Y, Z, colors='blue',
                     linestyles='solid', levels=levels, alpha=0.7)

fmt = {level: level.round(2) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True, fmt=fmt, colors='red')

ax.plot(curve_x, curve_y_top, color='black')
ax.plot(curve_x, curve_y_bottom, color='black')

plt.title('A contour plot for $f(x,y)=x^2+y^2$')
plt.savefig('ellipse_contour.pdf', format='pdf', bbox_inches='tight')

plt.show()
