from itertools import product
import numpy as np
import random


def noise(D):
    return random.choice([-0.4999 / D, 0.4999 / D])


def generate_combinations(n):
    # Create a list with repeated elements -1 and 1 of size n
    elements = [-1, 1]

    # Use itertools.product to generate all combinations
    combinations = list(product(elements, repeat=n))

    return combinations


def relu(x):
    return np.maximum(0, x)


def sign_v(array):
    return np.where(array >= 0, 1, -1)


k = 3
A = -2
B = 1
D = 5

W1 = np.array([[-k] * D, [k] * D])
W2 = np.array([-1, -1])
B1 = np.array([k * A - k / 2, -k * B - k / 2])
B2 = np.array([0])


combinations = generate_combinations(D)
for x_i in combinations:
    x_i_noise = [i + noise(D) for i in x_i]

    y_i = sum(x_i)
    if y_i >= A and y_i <= B:
        y_i = 1
    else:
        y_i = -1

    y_pred = relu(np.dot(W1, x_i) + B1)
    y_pred = sign_v(np.dot(W2, y_pred.T) + B2)[0]

    y_pred_noise = relu(np.dot(W1, x_i_noise) + B1)
    y_pred_noise = sign_v(np.dot(W2, y_pred_noise.T) + B2)[0]

    if y_pred != y_i:
        print("Error")

    if y_pred_noise != y_i:
        print("Not Resistent to Noise")
