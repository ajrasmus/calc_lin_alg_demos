import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
eps = 1
num_pts = 1000
X = 5 * np.random.rand(num_pts)
Y = 2 * np.sin(3 * X + 2) + (2 * np.random.rand(num_pts) - 1) * eps


def err(A, B, C):
    return np.linalg.norm(Y - A * np.sin(B * X + C))


def grad_A(A, B, C):
    return 2 * np.dot(-np.sin(B * X + C), Y - A * np.sin(B * X + C))


def grad_B(A, B, C):
    return 2 * np.dot(-A * X * np.cos(B * X + C), Y - A * np.sin(B * X + C))


def grad_C(A, B, C):
    return 2 * np.dot(-A * np.cos(B * X + C), Y - A * np.sin(B * X + C))


def grad(A, B, C):
    x, y, z = grad_A(A, B, C), grad_B(A, B, C), grad_C(A, B, C)
    return np.array([x, y, z])


offset = 2
A_init = 2 + (-2 * np.random.rand() + 1) * offset
B_init = 3 + (-2 * np.random.rand() + 1) * offset
C_init = 2 + (-2 * np.random.rand() + 1) * offset

A_cur = A_init
B_cur = B_init
C_cur = C_init

num_steps = 10000
step_size = 0.00001

xs = np.arange(0, 5, 0.01)

for step in range(num_steps):
    if step % 50 == 0:
        error = err(A_cur, B_cur, C_cur)
        print('\nStep: {}'.format(step))
        print('A:{}, B:{}, C:{} | Error:{}\n'.format(
            np.round(A_cur, 3), np.round(B_cur, 3),
            np.round(C_cur, 3), np.round(error, 3)))
        if step in [0, 10, 50, 100, 500, 1000, 5000]:
            alpha = 0.4 * (step / num_steps + 1)
            plt.plot(xs, A_cur * np.sin(B_cur * xs + C_cur), alpha=0.5,
                     label='Step {}'.format(step))

    g = grad(A_cur, B_cur, C_cur)

    norm = np.linalg.norm(g)

    gA, gB, gC = g

    A_cur -= gA * step_size
    B_cur -= gB * step_size
    C_cur -= gC * step_size

xs = np.arange(0, 5, 0.01)
plt.title('Fitting a sine curve using gradient descent')
plt.plot(xs, A_cur * np.sin(B_cur * xs + C_cur), color='black')
plt.legend(loc='upper left')
plt.savefig('intermediate_curves.pdf', format='pdf', bbox_inches='tight')
plt.show()
