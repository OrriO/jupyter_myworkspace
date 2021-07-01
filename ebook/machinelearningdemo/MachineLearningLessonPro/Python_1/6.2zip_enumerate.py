#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 14:51
# @Author  : Z
# @Email   : S
# @File    : 6.2zip_enumerate.py\
#zip函数作用就是将不同组的各个对应元素进行组合
l1=[1,2,3,4]
l2=[1,2,3,4,5,6]
print(list(zip(l1,l2))) #<zip object at 0x0000017EF1A4D448>
# [(1, 1), (2, 2), (3, 3), (4, 4)]
print(list(zip([9,10,11],[1,2,3]))) #<zip object at 0x0000017EF1A4D448>
print(list(zip([9,10,11],[1,2,3],[4,5,6]))) #<zip object at 0x0000017EF1A4D448>
#enumerate函数------枚举
print(list(enumerate(range(10),start=10)))