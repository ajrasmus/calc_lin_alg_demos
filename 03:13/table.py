import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageOps
image = Image.open('dog.jpg')
image_data = np.asarray(image)
image_data = image_data[:, :, 0]


def shape(data):
    return np.array([data[10 * i:10 * (i + 1), 10 * j:10 * (j + 1)].reshape(100)
                     for i in range(30) for j in range(30)])


def shape_back(data):
    new_data = np.zeros((300, 300))
    for i in range(30):
        for j in range(30):
            new_data[10 * i:10 * (i + 1), 10 * j:10 * (j + 1)
                     ] = data[30 * i + j, :].reshape(10, 10)
    return new_data


def pre_process(data):
    new_data = shape(data)
    means = np.mean(new_data, axis=1).reshape(900, 1)
    return new_data - means, means


def post_process(data, means):
    return shape_back(data + means)


processed, means = pre_process(image_data)
U, sigma, Vt = np.linalg.svd(processed)
Sigma = np.diag(sigma)
output = np.dot(np.dot(U[:, :1], Sigma[:1, :1]), Vt[:1, :])

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)
ax1.set_xticks([])
ax1.set_yticks([])
ax2.set_xticks([])
ax2.set_yticks([])
ax3.set_xticks([])
ax3.set_yticks([])
ax4.set_xticks([])
ax4.set_yticks([])

output = np.dot(np.dot(U[:, :2], Sigma[:2, :2]), Vt[:2, :])
ax1.imshow(post_process(output, means), cmap='gray')
ax1.set_title('Principal components: 2')

output = np.dot(np.dot(U[:, :3], Sigma[:3, :3]), Vt[:3, :])
ax2.imshow(post_process(output, means), cmap='gray')
ax2.set_title('Principal components: 3')

output = np.dot(np.dot(U[:, :5], Sigma[:5, :5]), Vt[:5, :])
ax3.imshow(post_process(output, means), cmap='gray')
ax3.set_title('Principal components: 5')

output = np.dot(np.dot(U[:, :10], Sigma[:10, :10]), Vt[:10, :])
ax4.imshow(post_process(output, means), cmap='gray')
ax4.set_title('Principal components: 10')

plt.savefig('compression_table.pdf', format='pdf', bbox_inches='tight')
