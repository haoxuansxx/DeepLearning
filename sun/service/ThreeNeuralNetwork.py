# -*- coding:utf-8 -*-
"""
  -- 三层神经网络实现 --
@Author: Sun
@time: 2019/2/25 16:53
"""
import numpy as np
from ActivationFunctionUtil import *

"""
  -- 权重和偏置的数据初始化工作 
"""
def init_network():
    netWork = {}
    netWork['W1'] = np.array([[0.1, 0.3, 0.5], [0.2, 0.4, 0.6]])
    netWork['b1'] = np.array([0.1, 0.2, 0.3])
    netWork['W2'] = np.array([[0.1, 0.4], [0.2, 0.5], [0.3, 0.6]])
    netWork['b2'] = np.array([0.1, 0.2])
    netWork['W3'] = np.array([[0.1, 0.3], [0.2, 0.4]])
    netWork['b3'] = np.array([0.1, 0.2])
    return netWork
pass

""" 
  -- 三层神经网络处理过程 
"""
def forward(network, x):
    W1, W2, W3 = network['W1'], network['W2'], network['W3']
    b1, b2, b3 = network['b1'], network['b2'], network['b3']

    a1 = np.dot(x, W1) + b1
    z1 = sigmoid(a1)
    a2 = np.dot(z1, W2) + b2
    z2 = sigmoid(a2)
    a3 = np.dot(z2, W3) + b3
    y = identity_function(a3)

    return y
pass

"""
  -- 三层神经网络试运行
"""
network = init_network()
x = np.array([1.0, 0.5])
y = forward(network, x)
print(y)
