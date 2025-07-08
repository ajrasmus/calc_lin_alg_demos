import numpy as np
import pandas as pd

data = pd.read_csv('housing.csv')

X = data['population']

Y = data['total_bedrooms']

import matplotlib.pyplot as plt

ax = plt.gca()
ax.set_xlabel('Population')
ax.set_ylabel('Total number of bedrooms')
ax.set_title('Total number of bedrooms vs population')
plt.scatter(X, Y, s=5)
plt.savefig('bedrooms_vs_pop.pdf', format='pdf')

X = X.loc[~Y.isna()]
Y = Y.loc[~Y.isna()]

X_cent = np.array(X - X.mean())

Y_cent = np.array(Y - Y.mean())

pop_vs_bedrooms = np.dot(X_cent, Y_cent.T) / \
    (np.linalg.norm(X_cent) * np.linalg.norm(Y_cent))

Z = data['latitude']
W = data['median_income']
Z = Z.loc[W <= 15]
W = W.loc[W <= 15]
Z_cent = np.array(Z - Z.mean())
W_cent = np.array(W - W.mean())

income_vs_latitude = np.dot(Z_cent, W_cent.T) / \
    (np.linalg.norm(Z_cent) * np.linalg.norm(W_cent))

plt.clf()
ax = plt.gca()
ax.set_xlabel('Latitude (degrees)')
ax.set_ylabel('Median income ($10k)')
ax.set_title('Median income vs latitude')
plt.scatter(Z, W, s=5)
plt.savefig('income_vs_latitude.pdf', format='pdf')
