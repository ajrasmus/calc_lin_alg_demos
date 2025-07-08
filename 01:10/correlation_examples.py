import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = np.array([-3, -1, 1, 3])
Y = np.array([4, -4, -4, 4])

Z = np.linspace(-3.5, 3.5, num=500)
W = Z**2 - 5

ax = plt.gca()
ax.scatter(X, Y, s=20)
ax.plot(Z, W, color='black', linewidth=1)
plt.title('Some data along the parabola $y=x^2-5$')
plt.savefig('along_parabola.pdf', format='pdf')

plt.clf()


X = np.array([-3, 1, 2])
Y = np.array([-8, 2, 6])

Z = np.linspace(-3.5, 3.5, num=500)
W = 3 * Z

ax = plt.gca()
ax.scatter(X, Y, s=20)
ax.plot(Z, W, color='black', linewidth=1)
plt.title('Some data near the line $y=3x$')
plt.savefig('near_line.pdf', format='pdf')
