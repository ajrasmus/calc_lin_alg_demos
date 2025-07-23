import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows=2, ncols=2)

axes = [ax1, ax2, ax3, ax4]

def f(x): return np.sin(x)
def df(x): return np.cos(x)


for n in range(1, 5):
      ax = axes[n - 1]

      X = np.arange(-2, 2, 0.05)
      Y = f(X)

      x = 1.14
      y = f(x)
      ax.scatter(x, y, color='red')
      eps = 0.1

      ax.plot([-2, 2], [0, 0], color='black')
      ax.plot(X, Y, color='blue')

      for i in range(n - 1):
            newx = x - f(x) / df(x)
            newy = f(newx)

            ax.scatter(newx, newy, color='red')

            x = newx
            y = newy

      newx = x - f(x) / df(x)
      newy = f(newx)

      if n < 3:
            ax.annotate('$(x_{}, y_{})$'.format(
                n, n), (x + eps, y + eps), color='red')

      ax.scatter(newx, newy, color='red')
      ax.annotate('$(x_{}, y_{})$'.format(
          n + 1, n + 1), (newx + eps, newy + eps), color='red')
      ax.scatter(newx, 0, color='red')
      if n < 3:
            ax.annotate('$(x_{}, 0)$'.format(
                n + 1, n + 1), (newx + eps, eps), color='red')
      ax.plot([x, newx], [y, 0], color='green')
      ax.plot([newx, newx], [0, newy], color='green', linestyle='--')

fig.suptitle("Newton's method")
plt.savefig('newton.pdf', format='pdf', bbox_inches='tight')
plt.savefig('newton.png', format='png', bbox_inches='tight')
