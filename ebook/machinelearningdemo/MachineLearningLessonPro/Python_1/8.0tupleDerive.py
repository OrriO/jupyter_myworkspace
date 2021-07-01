#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 16:45
# @Author  : Z
# @Email   : S
# @File    : 8.0tupleDerive.py
#元祖--求解满足条件的元祖
#生成器推导式---惰性求值-----
t1=(x*x for x in range(10))
#通过nect方法进行求解下一个符合条件的元素
print(t1.__next__())
print(t1.__next__())
print(t1.__next__())
print(t1.__next__())
print(t1.__next__())
print(list(t1))
print(list(t1))
print(list(t1))


#python中将多元素赋值叫做序列解包
a,b=1,1
print(a,b)
(x,y,z)=1,2,3
print(x,y,z)