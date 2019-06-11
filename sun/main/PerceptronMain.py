# -*- coding:utf-8 -*-

"""
  -- 感知机功能实现类 --
@Author: Sun
@time: 2019/2/25 14:03
"""
from PerceptronUtil import *


if __name__ == '__main__':
    list = [(0, 0), (1, 0), (0, 1), (1, 1)]

    print("--------------------- AND ---------------------")
    for xs in list:
        y = AND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    pass

    print("--------------------- NAND ---------------------")
    for xs in list:
        y = NAND(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    pass

    print("--------------------- OR ---------------------")
    for xs in list:
        y = OR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    pass

    print("--------------------- XOR ---------------------")
    for xs in list:
        y = XOR(xs[0], xs[1])
        print(str(xs) + " -> " + str(y))
    pass
pass
