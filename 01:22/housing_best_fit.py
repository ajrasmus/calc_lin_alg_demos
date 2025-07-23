import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('./housing.csv')

X = data['population']
Y = data['total_bedrooms']

X = X.loc[~Y.isna()]
Y = Y.loc[~Y.isna()]

X = np.array(X)
Y = np.array(Y)

one = np.ones(X.shape)

x_bar = np.dot(X, one) / np.dot(one, one)
y_bar = np.dot(Y, one) / np.dot(one, one)

X_hat = X - x_bar * one

m = np.dot(Y, X_hat) / np.dot(X_hat, X_hat)
b = y_bar - x_bar * (np.dot(Y, X_hat) / np.dot(X_hat, X_hat))

X_for_line = np.array([-1000, 20000])
Y_for_line = m * X_for_line + b

print(X)
print(Y)
print(x_bar)
print(y_bar)
print(X_hat)
print(m)
print(b)

ax = plt.gca()
ax.set_xlabel('Population')
ax.set_ylabel('Total number of bedrooms')
ax.set_title('Total number of bedrooms vs population')
plt.scatter(X, Y, s=5, color='blue')
plt.plot(X_for_line, Y_for_line, color='black')
plt.savefig('bedrooms_vs_pop.pdf', format='pdf')
plt.savefig('bedrooms_vs_pop.png', format='png')
