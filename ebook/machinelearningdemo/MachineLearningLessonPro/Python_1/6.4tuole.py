#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 15:06
# @Author  : Z
# @Email   : S
# @File    : 6.4tuole.py
#1.定义只有一个元素的tuple
t0=(1)
print(t0)
print(type(t0))  #<class 'int'>
t00=(1,)
print(type(t00))
#2.如果在tuple中定义一个list，那么list是否可以改变呢？
t01=(1,2,3,["Apple","pear"])
print(t01)
print(t01[0])
print(t01[1])
print(t01[2])
print(t01[3])
print(t01[3][0])
print(t01[3][1])
t01[3][0]="banana"
#(1, 2, 3, ['banana', 'pear'])
print(t01)
#3.tuple与各个数据结构类型的转换
t1=(1,2,3,4)
t2=tuple(range(10))
t3=tuple([1,2,3,4])
t4=tuple({1,2,3,4})
t5=tuple({1:"apple",2:"banana",3:"orange"})
print(t1)
print(t2)
print(t3)
print(t4)
print(t5)
#4.切片操作
print(t2[::])
print(t2[::-1])
print(t2[1:5:])
print(t2[1:5])
print(t2[:8])