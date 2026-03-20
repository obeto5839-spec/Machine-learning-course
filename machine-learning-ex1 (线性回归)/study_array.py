import numpy as np
x_train = np.array([[1.0, 2.0], [3.0, 4.0]])
y_train = np.array([300.0, 500.0])
print(f"x_train: {x_train}")
print(f"y_train: {y_train}")

m = x_train.shape[0]
print(f"m: {m}")

i = 0

x_i = x_train[i][i]
y_i = y_train[i]
print(f"x_i: {x_i}")
print(f"y_i: {y_i}")