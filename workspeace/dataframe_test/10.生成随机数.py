#!/usr/bin/python
#-*- coding: utf-8 -*-
import random
j=[]
for i in range(1,20):
    w=round(random.uniform(0.12,0.22),3)
    j.append(w)
    i=i+1
# j.sort( reverse=True)
for q in j:
    print(q)
