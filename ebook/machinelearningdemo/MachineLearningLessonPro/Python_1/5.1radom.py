#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 12:16
# @Author  : Z
# @Email   : S
# @File    : 5.1radom.py
import random
print("[0,1):",random.random())
print("[a,b]:",random.randint(1,10)) # range [a, b]
print("start stop:",random.randrange(1,10,2))#Choose a random item from range(start, stop[, step]).
str=[1,2,3,4]#有序
random.shuffle(str)
print(str) #[2, 1, 3, 4]
import numpy as np
print("normal data:\n",np.random.randn(5,5))
print("normal data:\n",np.random.chisquare(10,size=(5,5)))