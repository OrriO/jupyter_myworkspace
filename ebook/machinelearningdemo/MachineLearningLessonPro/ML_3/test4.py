# -*- coding: utf-8 -*- 
# @Time : 2018/12/26 17:45
# @Author : Z
# @Email : S
# @File : test4.py

def find_data(lst):
    ntime = 0
    result = 0
    for i in range(0, len(lst)):
        if ntime == 0:
            result = lst[i]
            ntime = 1
        elif result == lst[i]:
            ntime += 1
        else:
            ntime -= 1
    return print(result)


#
# w=dict()
# w[1][2]=0.5

A = ['c', 'd', 'e', 'a', 'b']
A = 'cdaeb'
B = 'ac'
C = len(A & B)
print(C)


