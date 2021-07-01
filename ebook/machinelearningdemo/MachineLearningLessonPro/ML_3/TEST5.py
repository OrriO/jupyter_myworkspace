# -*- coding: utf-8 -*- 
# @Time : 2019/1/6 14:54
# @Author : Z
# @Email : S
# @File : TEST5.py

# 快速排序

def partition(lyst, left, right):
    x = lyst[right]
    i = left - 1
    for j in range(left, right):
        if lyst[j] <= x:
            i += 1
            lyst[i], lyst[j] = lyst[j], lyst[i]
    lyst[i + 1], lyst[right] = lyst[right], lyst[i + 1]
    return i + 1


def quick_sort(lyst, left, right):
    if left < right:
        q = partition(lyst, left, right)
        quick_sort(lyst, left, q - 1)
        quick_sort(lyst, q + 1, right)


a = [2, 4, 1, 5, 3, 9, 18, 40, 6, 22, 15, 11]
quick_sort(a, 0, len(a) - 1)
print(a)

import tensorflow as tf
