import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-2.7, 2.7, 0.01)
y = np.arange(-2.7, 2.7, 0.01)

X, Y = np.meshgrid(x, y)

Z = (np.sin(X**2 / 2) * np.sin(Y**2 / 3) + X**2 + Y**2)
ax = plt.gca()
ax.set_axis_off()

curx = 2.5
cury = 1.9
Delta = 0.1

levels = []

for _ in range(12):
    gradx = curx * np.cos(curx**2 / 2) * np.sin(cury**2 / 3) + 2 * curx
    grady = 2 * cury / 3 * np.sin(curx**2 / 2) * np.cos(cury**2 / 3) + 2 * cury
    curlevel = np.sin(curx**2 / 2) * np.sin(cury**2 / 3) + curx**2 + cury**2
    plt.scatter(curx, cury, color='black', s=10)
    plt.arrow(curx, cury, -0.7 * gradx * Delta,
              -0.7 * grady * Delta, width=0.02, color='black')
    curx += -gradx * Delta
    cury += -grady * Delta
    levels.append(curlevel)

levels.extend([12, 14, 16])
levels = sorted(levels)

contour = ax.contour(X, Y, Z, colors='black',
                     linestyles='solid', levels=levels, alpha=0.5)

fmt = {level: level.round(2) for level in contour.levels}
ax.clabel(contour, contour.levels, inline=True, fmt=fmt)


plt.savefig('grad_descent.pdf', format='pdf')
plt.savefig('grad_descent.png', format='png')
