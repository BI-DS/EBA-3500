import numpy as np

a = np.random.randint(1, 10, 9).reshape(3, 3)
a = a + a.T

tens = np.tensordot(a, a, 0)
tens = tens.transpose(0, 2, 1, 3)
tens = tens + tens.transpose(1, 0, 2, 3)

tens[0, 2, 2, 1]
tens[0, 2, 1, 2]
tens[2, 0, 1, 2]
tens[0, 1, 2, 2]
tens[1, 0, 2, 2]
tens[1, 2, 0, 2]
tens[1, 2, 2, 0]

# The tensor is input-symmetric and output-symmetric. This is correct,
# as we don't need or want general symmetry.
