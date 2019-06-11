# -*- coding:utf-8 -*-
"""
  -- 测试3 --
@Author: Sun
@time: 2019/2/25 17:14
"""
import numpy as np
from ActivationFunctionUtil import *

if __name__ == '__main__':
    a = np.array([0.3, 2.9, 4.0])
    y = softmax(a)

    print(y)
    print(np.sum(y))
pass
