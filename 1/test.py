import numpy as np

# Example vectors x_i and d
x_i = np.array([1, 2, 3])
d = np.array([4, 5, 6])

# Improved code
outer_product = np.outer(x_i, d)
print(outer_product.shape)
