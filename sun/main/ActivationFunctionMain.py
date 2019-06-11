# -*- coding:utf-8 -*-
"""
  -- 激活函数测试输出类 --
@Author: Sun
@time: 2019/2/25 15:57
"""
import numpy as np
import matplotlib.pylab as plt
from ActivationFunctionUtil import *


"""
  -- 阶跃函数输出 --
"""
def step_main():
    x = np.arange(-5.0, 5.0, 0.1)  # 在-5.0到5.0的范围内，以0.1为单位，生成NumPy数组([-5.0, -4.9, ..., 4.9])
    y = step_function(x)  # 阶跃函数
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # 指定y轴的范围
    plt.show()


""" 
  -- sigmoid函数输出 -- 
"""
def sigmoid_main():
    x = np.arange(-5.0, 5.0, 0.1)  # 在-5.0到5.0的范围内，以0.1为单位，生成NumPy数组([-5.0, -4.9, ..., 4.9])
    y = sigmoid(x)  # sigmoid激活函数
    plt.plot(x, y)
    plt.ylim(-0.1, 1.1)  # 指定y轴的范围
    plt.show()
pass


"""
  -- ReLU函数输出 --
"""
def relu_main():
    x = np.arange(-5.0, 5.0, 0.1)  # 在-5.0到5.0的范围内，以0.1为单位，生成NumPy数组([-5.0, -4.9, ..., 4.9])
    y = relu(x)  # sigmoid激活函数
    plt.plot(x, y)
    plt.ylim(-0.1, 9.9)  # 指定y轴的范围
    plt.show()
pass

if __name__ == '__main__':
    step_main()
    sigmoid_main()
    relu_main()
pass