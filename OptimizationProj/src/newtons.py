newtons.py

'''
(1)终止条件 0<e<<1,初始条件x0
(2)计算gk = f'(xk),||gk|| <= e,则停止，输出x* = xk
(3)计算Gk = f''(xk),并求解线性方程组的解dk: Gkd = -gk
(4) 令xk+1 = xk + dk, k = k+ 1,转2
'''

import numpy
import math
import matplotlib.pyplot as pl

def newtons():
