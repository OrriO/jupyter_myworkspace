#-*- coding: utf-8 -*-
# @Time    : 2018/12/5 16:21
# @Author  : Z
# @Email   : S
# @File    : 21sklearn.py
from sklearn import linear_model
reg = linear_model.LinearRegression()
x = [[0, 0], [1, 1], [2, 2]]
y = [0, 1, 2]
reg.fit (x, y) #Fit linear model.
# LinearRegression(copy_X=True, fit_intercept=True, n_jobs=None,
#                  normalize=False)
print(reg.coef_) #[0.5 0.5] w1x1+w2x2+w0  w1=0.5,w2=0.5
print(reg.intercept_) #w0=0
import numpy as np
print(np.allclose(0,reg.intercept_))
# array([0.5, 0.5])
print(reg.predict([[0,0],[1,1]]))