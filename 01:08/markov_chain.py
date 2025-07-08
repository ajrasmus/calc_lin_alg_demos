import numpy as np

matrix = np.array([[0.7, 0.1, 0.1], [0.2, 0.8, 0.3], [0.1, 0.1, 0.6]])
pop_vec = np.array([5 * 1e6, 5 * 1e6, 5 * 1e6])

for i in range(50):
    print(np.round(pop_vec))
    pop_vec = np.dot(matrix, pop_vec)
