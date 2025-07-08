import functools
import numpy as np


def sq_dist(v, w):
    return np.sum((v - w)**2)


def clusters(vecs, c1, c2):
    cluster1 = [v for v in vecs if sq_dist(v, c1) < sq_dist(v, c2)]
    cluster2 = [v for v in vecs if sq_dist(v, c1) >= sq_dist(v, v2)]

    d1 = functools.reduce(lambda a, b: a + b, cluster1) / len(cluster1)
    d2 = functools.reduce(lambda a, b: a + b, cluster2) / len(cluster2)

    return cluster1, cluster2, d1, d2


v1 = np.array([1, 1])
v2 = np.array([1, 5])
v3 = np.array([2, 4])
v4 = np.array([3, 1])
v5 = np.array([3, 2])
v6 = np.array([4, 1])
vecs = [v1, v2, v3, v4, v5, v6]
c1 = v2
c2 = v3

for i in range(10):
    cluster1, cluster2, d1, d2 = clusters(vecs, c1, c2)
    print(cluster1, cluster2, c1, c2)
    c1, c2 = d1, d2
