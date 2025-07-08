import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = np.array([0, 1, -1])
Y = np.array([2, 2, -1])
one = np.array([1, 1, 1])

x_bar = np.dot(X, one) / np.dot(one, one)
y_bar = np.dot(Y, one) / np.dot(one, one)

X_hat = X - x_bar * one

m = np.dot(Y, X_hat) / np.dot(X_hat, X_hat)
b = y_bar - x_bar * (np.dot(Y, X_hat) / np.dot(X_hat, X_hat))

X_for_line = np.array([-2, 2])
Y_for_line = m * X_for_line + b

plt.scatter(X, Y, color='blue')
plt.plot(X_for_line, Y_for_line, color='black')
plt.title('Line of best fit for $(-1,-1), (0,2), (1,2)$')
plt.savefig('best_fit_1.pdf', format='pdf')

plt.clf()

X = np.array([2, 3, 3, 4])
Y = np.array([3, 3, 0, -2])
one = np.array([1, 1, 1, 1])

x_bar = np.dot(X, one) / np.dot(one, one)
y_bar = np.dot(Y, one) / np.dot(one, one)

X_hat = X - x_bar * one

m = np.dot(Y, X_hat) / np.dot(X_hat, X_hat)
b = y_bar - x_bar * (np.dot(Y, X_hat) / np.dot(X_hat, X_hat))

X_for_line = np.array([0, 5])
Y_for_line = m * X_for_line + b

plt.scatter(X, Y, color='blue')
plt.plot(X_for_line, Y_for_line, color='black')
plt.title('Line of best fit for $(2,3), (3,3), (3,0), (4,-2)$')
plt.savefig('best_fit_2.pdf', format='pdf')

plt.show()
