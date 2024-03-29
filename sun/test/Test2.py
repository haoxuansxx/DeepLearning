# -*- coding:utf-8 -*-
"""
  -- 测试2 --
@Author: Sun
@time: 2019/2/25 16:39
"""
import numpy as np
from ActivationFunctionUtil import *

if __name__ == '__main__':
    X = np.array([1.0, 0.5])
    W1 = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    B1 = np.array([0.1, 0.2, 0.3])

    print(W1.shape)  # (2, 3)
    print(X.shape)  # (2,)
    print(B1.shape)  # (3,)

    A1 = np.dot(X, W1) + B1
    Z1 = sigmoid(A1)
    print(Z1)

    W2 = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    B2 = np.array([0.1, 0.2])

    print(Z1.shape)  # (2, 3)
    print(W2.shape)  # (2,)
    print(B2.shape)  # (3,)
    A2 = np.dot(Z1, W2) + B2
    Z2 = sigmoid(A2)
    print(Z2)

    W3 = np.array([[0.1, 0.3], [0.2, 0.4]])
    B3 = np.array([0.1, 0.2])

    A3 = np.dot(Z2, W3) + B3
    y = A3
    print(y)

pass
