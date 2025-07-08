from ucimlrepo import fetch_ucirepo
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# fetch dataset
wine = fetch_ucirepo(id=109)

# data (as pandas dataframes)
X = wine.data.features
y = wine.data.targets

X_cent = X.copy()

for col in X_cent.columns:
    X_cent[col] = X_cent[col] - X_cent[col].mean()

X_np = np.array(X_cent)

print(X_np)

U, sigma, Vt = np.linalg.svd(X_np)

W2 = Vt.T[:, :2]
X2D = X_np.dot(W2)

import matplotlib.pyplot as plt

one_indices = y.index[y['class'] == 1]
two_indices = y.index[y['class'] == 2]
three_indices = y.index[y['class'] == 3]

ax = plt.gca()
ax.scatter(X2D[one_indices, 0], X2D[one_indices, 1],
           color='blue', alpha=0.9, label='Cultivar 1')
ax.scatter(X2D[two_indices, 0], X2D[two_indices, 1],
           color='orange', alpha=0.9, label='Cultivar 2')
ax.set_axis_off()
ax.legend(loc='lower right')
plt.title('PCA for wine dataset')
plt.savefig('wine_pca.pdf', format='pdf')
