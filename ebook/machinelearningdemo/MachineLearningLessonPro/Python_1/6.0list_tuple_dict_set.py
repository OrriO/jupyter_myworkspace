#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 12:23
# @Author  : Z
# @Email   : S
# @File    : 6.0list_tuple_dict_set.py
#1.list----列表---有序、异质、根据下标进行查询、更改、删除
#1.1创建
l1=[1,2,3,4]
#1.2查询---根据下标
print(l1[0])
print(l1[1])
#1.3增加
l1.append(10)
print(l1)
#1.4更改
l1[0]="apple"
print(l1)
#1.4删除
del l1[0]
print(l1)
l1.remove(10)
print(l1)
#2.tuple-----元祖-----有序、异质、根据下标进行查询，不能够进行修改、删除、更新等操作
#2.1创建
l2=(1,"apple",3,4)
print(type(l2)) #<class 'tuple'>
#2.2查询
print(l2[0])
print(l2[1])
#2.3修改----不能修改
# l2[0]="apple"
# print(l2) #TypeError: 'tuple' object does not support item assignment
#2.4删除---TypeError: 'tuple' object doesn't support item deletion
# del l2[0]
#可以直接删除整个元祖
# del l2
# print(l2) #NameError: name 'l2' is not defined
#3.dict-----字典-----无序、能够根据key进行查询、更改、删除等操作
#3.1创建
l3={"apple":10,"pear":20}
#3.2查询
print(l3["apple"])
#3.3更改
l3["apple"]="pear"
print(l3)
#3.4删除
del l3["apple"]
print(l3) #{'pear': 20}
l3.clear()
print(l3)  #{}
#4.set------集合-----无序性、唯一性、确定性
l4={"apple","pear"}
print({"a","b","c","a","b"})
