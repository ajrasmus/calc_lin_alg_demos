import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

train_data = pd.read_csv('./breast_cancer_data.csv')
X = train_data.drop(labels=['id', 'Unnamed: 32'], axis=1)
numeric_cols = X.select_dtypes(include=np.number).columns
X_cent = X.iloc[:, :]

for name in numeric_cols:
    X_cent[name] = X_cent[name] - X_cent[name].mean()

X_cent_num = X_cent.drop(labels='diagnosis', axis=1)

X_np = np.array(X_cent_num)

U, sigma, Vt = np.linalg.svd(X_np)

B_indices = X.index[X.diagnosis == 'B']
M_indices = X.index[X.diagnosis == 'M']

W2 = Vt.T[:, :2]
X2D = X_np.dot(W2)

ax = plt.gca()
ax.scatter(X2D[B_indices, 0], X2D[B_indices, 1], alpha=0.5, color='blue', label='Benign')
ax.scatter(X2D[M_indices, 0], X2D[M_indices, 1], alpha=0.5, color='orange', label='Malignant')
ax.set_axis_off()
ax.legend(loc = 'lower right')
plt.title('PCA for breast cancer data set')
plt.savefig('breast_cancer_pca.pdf', format='pdf')
plt.savefig('breast_cancer_pca.png', format='png')
