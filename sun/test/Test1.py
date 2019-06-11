# -*- coding:utf-8 -*-
"""
  -- 测试1 --
@Author: Sun
@time: 2019/2/25 16:21
"""
import numpy as np

if __name__ == '__main__':
    X = np.array([1, 2])
    print(X.shape)

    W = np.array([[1, 3, 5], [2, 4, 6]])
    print(W)
    print(W.shape)

    Y = np.dot(X, W)
    print(Y)

pass
