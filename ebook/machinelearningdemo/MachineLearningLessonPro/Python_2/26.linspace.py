#-*- coding: utf-8 -*-
# @Time    : 2018/12/3 10:29
# @Author  : Z
# @Email   : S
# @File    : 26.linspace.py
import numpy as np
#等差数列
r1=np.linspace(1,10,num=10)
print(r1) #[ 1.  2.  3.  4.  5.  6.  7.  8.  9. 10.]
r2=np.linspace(1,10,num=50)
print(r2)
#等比数列
r3=np.logspace(1,10,10)
print(r3)#[1.e+01 1.e+02 1.e+03 1.e+04 1.e+05 1.e+06 1.e+07 1.e+08 1.e+09 1.e+10]
r4=np.logspace(1,10,100)
print(r4)