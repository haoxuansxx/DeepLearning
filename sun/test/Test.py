# -*- coding:utf-8 -*-
"""
  -- 测试 --
@Author: Sun
@time: 2019/2/25 16:21
"""
import numpy as np

if __name__ == '__main__':
    A = np.array([[1, 2], [3, 4], [5, 6]])
    print(A.shape)

    B = np.array([[7, 8, 9], [10, 11, 12]])
    print(B.shape)

    print(np.dot(A, B))

pass
