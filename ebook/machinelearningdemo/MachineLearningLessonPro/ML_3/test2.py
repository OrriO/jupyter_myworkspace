# -*- coding: utf-8 -*- 
# @Time : 2018/12/22 0:22
# @Author : Z
# @Email : S
# @File : test2.py


# 简单插入排序
# l1 = [2, 5, 7, 9, 1, 6]
# print(l1)
# def insert_sort(ary):
#     n = len(ary)
#     for i in range(1,n):
#         if ary[i] < ary[i-1]:
#             temp = ary[i]
#             index = i           #待插入的下标
#             for j in range(i-1,-1,-1):  #从i-1 循环到 0 (包括0)
#                 if ary[j] > temp :
#                     ary[j+1] = ary[j]
#                     index = j   #记录待插入下标
#                 else :
#                     break
#             ary[index] = temp
#     return ary
# l2 = insert_sort(l1)
# print(l1)

# 冒泡排序
# def bubble_sort(ary):
#     count = len(ary)
#     for i in range(0, count):
#         for j in range(i + 1, count):
#             if ary[i] > ary[j]:
#                 ary[i], ary[j] = ary[j], ary[i]
#     return ary
#
#
# ary1 = bubble_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
# print(ary1)


# def quick_sort(qlist):
#     if qlist == []:
#         return []
#     else:
#         qfirst = qlist[0]
#         qless = quick_sort([l for l in qlist[1:] if l < qfirst])
#         qmore = quick_sort([m for m in qlist[1:] if m >= qfirst])
#         return qless + [qfirst] + qmore
#
# qlist1 = quick_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
# print(qlist1)


import copy
def heap_sort(hlist):
    def heap_adjust(parent):
        child = 2 * parent + 1  # left child
        while child < len(heap):
            if child + 1 < len(heap):
                if heap[child + 1] > heap[child]:
                    child += 1  # right child
            if heap[parent] >= heap[child]:
                break
            heap[parent], heap[child] = heap[child], heap[parent]
            parent, child = child, 2 * child + 1

    heap, hlist = copy.copy(hlist), []
    for i in range(len(heap) // 2, -1, -1):
        heap_adjust(i)
    while len(heap) != 0:
        heap[0], heap[-1] = heap[-1], heap[0]
        hlist.insert(0, heap.pop())
        heap_adjust(0)
    return hlist


hlist = heap_sort([4, 5, 6, 7, 3, 2, 6, 9, 8])
print(hlist)