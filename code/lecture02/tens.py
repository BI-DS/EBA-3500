import numpy as np

def circ(a, b, n):
    return(np.tensordot(a, b, n))

rng = np.random.default_rng(seed=313)
a = rng.integers(0, 10, 3**4).reshape(3, 3, 3, 3)
b = rng.integers(0, 10, 3**4).reshape(3, 3, 3, 3)

circ(a, b, 4)
y = circ(a, b, 2)

zum = 0
for i in range(3):
    for j in range(3):
        zum += y[i, j, i, j]
        zum += y[i, i, j, j]
        zum += 2*y[i, j, j, i]

zum/4

a = np.eye(2*3*4)
a.shape = (2*3, 4, 2, 3, 4)
b = np.random.randn(2*3, 4)
x = np.linalg.tensorsolve(a, b)
x.shape
np.allclose(np.tensordot(a, x, axes=3), b)


