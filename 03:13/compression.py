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

ax = plt.gca()
ax.set_xticks([])
ax.set_yticks([])
ax.imshow(post_process(output, means), cmap='gray')
plt.savefig('compressed.pdf', format='pdf', bbox_inches='tight')

plt.cla()
ax.imshow(output[0].reshape(10, 10), cmap='gray')
plt.savefig('pattern.pdf', format='pdf', bbox_inches='tight')
plt.show()
