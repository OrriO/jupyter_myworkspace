# -*- coding: utf-8 -*-
# @Time    : 2018/12/2 14:34
# @Author  : Z
# @Email   : S
# @File    : 6.1listDemo.py
# 1.list创建[]及各个数据结构的转换
# list\set\dict\tuple
print(range(10))  # range(0, 10)
print(type(range(10)))  # range(0, 10) <class 'range'>
# 在python2中情况
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# <type 'list'>
print(list(range(10)))  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# tuple----->list
t1 = (1, 2, 3, 4)
l1 = list(t1)
print(l1)
print(type(l1))
# set----->list
print(list({1, 3, 4}))  # [1, 3, 4]
# dict----->list
print(list({"apple": 1, "pear": 2}))  # ['apple', 'pear']
print(list({"apple": 1, "pear": 2}.keys()))  # ['apple', 'pear']
print(list({"apple": 1, "pear": 2}.values()))  # [1, 2]
print(list({"apple": 1, "pear": 2}.items()))  # [('apple', 1), ('pear', 2)]

# 2.list的重要的操作---切片操作
l1 = list(range(10))  # l1[start:stop:step]
print(l1[::])  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(l1[::-1])  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
print(l1[-2])
print(l1[2:5:])  # [2, 3, 4]
print(l1[2:5])  # [2, 3, 4]
print(l1[2:])  # [2, 3, 4, 5, 6, 7, 8, 9]
print(l1[::2])  # [0, 2, 4, 6, 8]
print(l1[1::2])  # [1, 3, 5, 7, 9]

# 3.其他补充
print(len(l1))
print([1, 2, 3] + ["one", "A", 'B'])
print(1 in [1, 2, 3])
print(1 not in [1, 2, 3])

# 补充
l1 = list(range(10))
print(l1)  # 0-9 不包含10数值
print(list(range(0, 10, 1)))
