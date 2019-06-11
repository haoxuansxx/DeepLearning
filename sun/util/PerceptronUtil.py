# -*- coding:utf-8 -*-
"""
  -- 感知机功能工具类 --
@Author: Sun
@time: 2019/2/25 14:04
"""
import numpy as np


"""
  -- AND函数（与门） --
  -- 输入参数x1、x2
"""
def AND(x1, x2):
    x = np.array((x1, x2))  # 输入参数
    w = np.array((0.5, 0.5))  # 输入参数对应的权重
    b = -0.7  # 偏置（阈值）PS：神经元被激活的容易程度（输出信号为1的程度）
    tmp = np.sum(w*x) + b

    '''当输入的加权总和超过阈值时返回1'''
    if tmp <= 0:
        return 0
    else:
        return 1
    pass
pass


"""
  -- NAND函数（与非门） --
  -- 输入参数x1、x2
"""
def NAND(x1, x2):
    x = np.array((x1, x2))  # 输入参数
    w = np.array((-0.5, -0.5))  # 输入参数对应的权重
    b = 0.7  # 偏置（阈值）PS：神经元被激活的容易程度（输出信号为1的程度）
    tmp = np.sum(w*x) + b

    '''当输入的加权总和超过阈值时返回1'''
    if tmp <= 0:
        return 0
    else:
        return 1
    pass
pass


"""
  -- OR函数（或门） --
  -- 输入参数x1、x2
"""
def OR(x1, x2):
    x = np.array((x1, x2))  # 输入参数
    w = np.array((0.5, 0.5))  # 输入参数对应的权重
    b = -0.2  # 偏置（阈值）PS：神经元被激活的容易程度（输出信号为1的程度）
    tmp = np.sum(w*x) + b

    '''当输入的加权总和超过阈值时返回1'''
    if tmp <= 0:
        return 0
    else:
        return 1
    pass
pass


"""
  -- XOR函数（异或门） --
  -- 输入参数x1、x2
"""
def XOR(x1, x2):
    s1 = NAND(x1, x2)
    s2 = OR(x1, x2)
    y = AND(s1, s2)
    return y
pass

