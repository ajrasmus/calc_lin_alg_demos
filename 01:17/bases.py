import numpy as np
import matplotlib.pyplot as plt

u = np.array([1, 2])
v = np.array([2, 1])

u_mults = [a * u for a in range(-5, 5, 1)]
v_mults = [a * v for a in range(-5, 5, 1)]
linear_combos = [x + y for x in u_mults for y in v_mults]

u_line = [-10 * u, 10 * u]
v_line = [-10 * v, 10 * v]

for a in range(-5, 5, 1):
    u_trans = [a * v + x for x in u_line]
    X = [x[0] for x in u_trans]
    Y = [x[1] for x in u_trans]
    plt.plot(X, Y, color='blue')

for a in range(-5, 5, 1):
    v_trans = [a * u + x for x in v_line]
    X = [x[0] for x in v_trans]
    Y = [x[1] for x in v_trans]
    plt.plot(X, Y, color='blue')

X = [x[0] for x in linear_combos]
Y = [x[1] for x in linear_combos]
plt.scatter(X, Y, color='black')

plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.title('The grid defined by a basis for $\mathbb{R}^2$')
plt.savefig('basis.pdf', format='pdf')
