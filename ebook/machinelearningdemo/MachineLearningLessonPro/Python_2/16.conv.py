#-*- coding: utf-8 -*-
# @Time    : 2018/12/3 9:08
# @Author  : Z
# @Email   : S
# @File    : 16.conv.py
import scipy as sp
result=sp.convolve([1,2,3,4,5,6,7,8,8,9],[4,5,6])
print(result) #[ 4 13 28 43 38 24]

# lst1=[4,5,6] ===》lst1=[6,5,4]==》length1=3 i---》range(1,4)=1,2,3
# 1.  3-1=2 lst1=[4(2)]
# 2.  3-2=1 lst1=[5(1),4(2)]
# 3.  3-3=0 lst1=[6(0),5(1),4(2)]
# lst2=[1,2,3,4]==》length1=4
def conv(lst1,lst2):
    length1=len(lst1)
    length2=len(lst2)
    lst1.reverse()
    result=[]
    for i in range(1,length1+1):
        t=lst1[length1-i:]
        r1=sum([t1*t2 for t1,t2 in zip(t,lst2)])
        result.append(r1)
    #使用lst2进行相对移动----加一个翻转
    # lst2=[1,2,3,4]==》length2=4==>range(1,4)==》1,2,3
    # 1.lst2[1:]   lst2=[2,3,4]
    # 2.lst2[2:]   lst2=[3,4]
    # 2.lst2[3:]   lst2=[4]
    for i in range(1,length2):
        t=lst2[i:]
        r2=sum([t1*t2 for t1,t2 in zip(lst1,t)])
        result.append(r2)
    return result

if __name__ == '__main__':
    result=conv([1,2,3,4,5,6,7,8,8,9],[4,5,6])
    print("convolve 1 result:",result)