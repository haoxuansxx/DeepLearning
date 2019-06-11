# -*- coding:utf-8 -*-
"""
  -- 激活函数功能工具类 --
@Author: Sun
@time: 2019/2/25 15:45
"""
import numpy as np

"""
  -- 阶跃函数  PS：非线性函数 --
  -- 输入参数x
"""
def step_function(x):
    y = x > 0
    return y.astype(np.int)
pass

"""
  -- sigmoid函数  PS：非线性函数 --
  -- 输入参数x
"""
def sigmoid(x):
    return 1 / (1 + np.exp(-x))
pass

"""
  -- ReLU函数 --
  -- 输入参数x
"""
def relu(x):
    return np.maximum(0, x)
pass

"""
  -- 恒等函数  PS：输入跟输出一致，一般而言，回归问题用恒等函数 --
  -- 输入参数x
"""
def identity_function(x):
    return x
pass

"""
  -- softmax函数  PS：一般而言，分类问题用softmax函数 --
  -- 公式： 
  -- 输入参数x
"""
def softmax(a):
    c = np.max(a)
    exp_a = np.exp(a - c)  # -c 为溢出对策
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a
    return y
pass