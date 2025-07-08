import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

X = np.random.normal(loc=0, scale=10, size=(1000, 1))
offset = np.random.normal(loc=0, scale=5, size=(1000, 1))
Y = -2 * X + offset + 5

lineX = np.linspace(min(X), max(X), num=1000)
lineY = -2 * lineX + 5

Xhat = X - X.mean()
Yhat = Y - Y.mean()
rlin = np.dot(Xhat.T, Yhat) / (np.linalg.norm(Xhat) * np.linalg.norm(Yhat))

ax = plt.gca()
ax.scatter(X, Y, s=5)
ax.plot(lineX, lineY, color='black', linewidth=1)
plt.title('Some data, $r={}$'.format(round(float(rlin), 3)))
plt.savefig('linear_correlation.pdf', format='pdf')

plt.clf()

X = np.random.normal(loc=0, scale=10, size=(1000, 1))
offset = np.random.normal(loc=0, scale=5, size=(1000, 1))
Y = X**2 + offset

parabX = np.linspace(min(X), max(X), num=1000)
parabY = parabX**2

Xhat = X - X.mean()
Yhat = Y - Y.mean()
rparab = np.dot(Xhat.T, Yhat) / (np.linalg.norm(Xhat) * np.linalg.norm(Yhat))

ax = plt.gca()
ax.scatter(X, Y, s=5)
ax.plot(parabX, parabY, color='black', linewidth=1)
plt.title('Some data, $r={}$'.format(round(float(rparab), 3)))
plt.savefig('parabola_correlation.pdf', format='pdf')
