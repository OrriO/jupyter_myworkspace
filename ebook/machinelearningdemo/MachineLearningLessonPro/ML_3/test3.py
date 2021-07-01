# -*- coding: utf-8 -*- 
# @Time : 2018/12/26 16:53
# @Author : Z
# @Email : S
# @File : test3.py


a = "1.22b.e.c.d"
l = a.split(".")
print(l)
print(type(l))

import re

print(a[1])


def sort1(lst1):
    first_max = 0
    second_max = 0
    len_lst1 = len(lst1)
    for i in range(0, len_lst1):
        if first_max < lst1[i]:
            second_max = first_max
            first_max = lst1[i]
    return print(first_max, second_max)


lst = [3, 4, 1, 7, 6, 9, 10, 13, 5, 20, 12,66]
sort1(lst)
