import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches

ax = plt.gca()
ax.set_aspect('equal')
ax.set_xticks([])
ax.set_yticks([])

x = np.array([[2], [1]])
y = np.array([[1], [2]])
e1 = np.array([[1], [0]])
z = x + y
orig = np.array([[0], [0]])
mat = 1 / np.sqrt(5) * np.array([[-2, -1], [1, -2]])

angleA = int(np.arccos(np.dot(y.T, e1)))

ax.arrow(orig[0, 0], orig[1, 0], x[0, 0], x[1, 0], color='blue', width=0.02)
ax.arrow(orig[0, 0], orig[1, 0], y[0, 0], y[1, 0], color='green', width=0.02)
ax.arrow(x[0, 0], x[1, 0], y[0, 0], y[1, 0], color='green', width=0.02)
ax.arrow(y[0, 0], y[1, 0], x[0, 0], x[1, 0], color='blue', width=0.02)
ax.arrow(orig[0, 0], orig[1, 0], z[0, 0], z[1, 0], color='red', width=0.02)

ax.arrow((np.dot(mat, orig))[0, 0], (np.dot(mat, orig))[
         1, 0], (np.dot(mat, x))[0, 0], (np.dot(mat, x))[1, 0], color='blue', width=0.02)
ax.arrow((np.dot(mat, orig))[0, 0], (np.dot(mat, orig))[
         1, 0], (np.dot(mat, y))[0, 0], (np.dot(mat, y))[1, 0], color='green', width=0.02)
ax.arrow((np.dot(mat, x))[0, 0], (np.dot(mat, x))[
         1, 0], (np.dot(mat, y))[0, 0], (np.dot(mat, y))[1, 0], color='green', width=0.02)
ax.arrow((np.dot(mat, y))[0, 0], (np.dot(mat, y))[1, 0], (np.dot(mat, x))[0, 0],
         (np.dot(mat, x))[1, 0], color='blue', width=0.02)
ax.arrow((np.dot(mat, orig))[0, 0], (np.dot(mat, orig))[
         1, 0], (np.dot(mat, z))[0, 0], (np.dot(mat, z))[1, 0], color='red', width=0.02)

arr = patches.FancyArrowPatch(posA=(0.5 * y[0, 0], 0.5 * y[1, 0]),
                              posB=(0.5 * np.dot(mat, x)[0, 0],
                                    0.5 * np.dot(mat, x)[1, 0]),
                              connectionstyle='arc3,rad=.5',
                              arrowstyle='->,head_width=5,head_length=5',
                              linewidth=2)

ax.add_patch(arr)
plt.title('Rotations are linear!')
plt.savefig('rotation.pdf', format='pdf', bbox_inches='tight')
plt.show()
