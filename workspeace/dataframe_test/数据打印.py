#!/usr/bin/python
# -*- coding: utf-8 -*-
# import os
# base_dir = os.path.join(os.path.dirname(__file__), "../")
t = open('A00.txt', 'r')
# print(t)
j = 0
dict = {}
for i in t:
    w = i.strip('\n')
    dict[w] = j
    print(w,':',j)
    j += 1
