#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 20:36
# @Author  : Z
# @Email   : S
# @File    : 07.for.py
from __future__ import print_function
for i in range(10):
    print(i,end="")

print()
for i in [1,2,3,4]:
    print(i,end="")


print()
for i in (1,2,3,4):
    print(i,end="")

print()
for i in {"apple":1,"pear":2}.values():
    print(i,end="")
print()


for i in range(10):
    print(i,end="")
else:
    print("Finish")