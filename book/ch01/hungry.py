import numpy as np

print("I'm hungry!")

X = np.array([[51, 55], [11, 34], [23, 54], [234, 5342]])
print(X.dtype)
print(X.shape)
x = X.flatten()
print(x.dtype)
print(x.shape)

x[x > 15]
print(x > 15)
print(x)

pass
