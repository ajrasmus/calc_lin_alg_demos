import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from matplotlib.ticker import MaxNLocator

plt.grid(False)

for arr in [[0], [-50, 0, 50], [-50, -25, 0, 25, 50]]:
    ax = plt.figure().add_subplot(projection='3d')
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_aspect('equal')

    for c in arr:
        x = np.arange(-10, 10, 0.001)
        posy = np.sqrt(x**2 - c)
        negy = -posy
        z = c * np.ones(x.shape)
        ax.plot(x, posy, z, color='black')
        ax.plot(x, negy, z, color='black')

        otherx = np.arange(-10, 11, 1)
        othery = np.arange(-10, 11, 1)
        X, Y = np.meshgrid(otherx, othery)
        Z = c * np.ones(X.shape)
        ax.plot_surface(X, Y, Z, alpha=0.3, color='green')

    x = np.arange(-10, 10, 0.01)
    y = np.arange(-10, 10, 0.01)

    X, Y = np.meshgrid(x, y)
    Z = X**2 - Y**2

    ax.plot_surface(X, Y, Z, alpha=0.3, linewidth=0.5, color='blue')
    plt.savefig(f'{len(arr)}_contours.pdf', format='pdf')
    plt.savefig(f'{len(arr)}_contours.png', format='png')
