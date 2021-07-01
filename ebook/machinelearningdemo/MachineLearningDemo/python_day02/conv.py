#-*- coding: utf-8 -*- 
# @Time : 2018/12/3 9:08
# @Author : Z
# @Email : S
# @File : conv.py

import scipy as sp
#求卷积
result= sp.convolve([1, 2, 3, 4], [4, 5, 6])
print(result)

#方法二:手动实现
def conv(lst1,lst2):
    length1=len(lst1)
    length2=len(lst2)
    lst1.reverse()
    result=[]




