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

p1 = np.array([1, 0])
vec1 = np.array([1, 0])
vec1 = vec1 / (3 * np.linalg.norm(vec1))

p2 = np.array([-1, 0])
vec2 = np.array([-1, 0])
vec2 = vec2 / (3 * np.linalg.norm(vec2))

p3 = np.array([-1 / 4, np.sqrt(15) / 4])
vec3 = np.array([0.5, -2 * np.sqrt(15) / 4])
vec3 = vec3 / (3 * np.linalg.norm(vec3))

p4 = np.array([-1 / 4, - np.sqrt(15) / 4])
vec4 = np.array([0.5, 2 * np.sqrt(15) / 4])
vec4 = vec4 / (3 * np.linalg.norm(vec4))

for pt, vec in zip([p1, p2, p3, p4], [vec1, vec2, vec3, vec4]):
    ax.arrow(pt[0], pt[1], vec[0], vec[1], color='black', width=0.01)

contour = ax.contour(X, Y, Z, colors='blue',
                     linestyles='solid', levels=levels, alpha=0.7)
fmt = {level: level.round(2) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True, fmt=fmt, colors='red')

ax.plot(curve_x, curve_y_top, color='black')
ax.plot(curve_x, curve_y_bottom, color='black')

plt.title('A contour plot for $f(x,y)=x+x^2-y^2$')
plt.savefig('harmonic_contour.pdf', format='pdf', bbox_inches='tight')
plt.savefig('harmonic_contour.png', format='png', bbox_inches='tight')
