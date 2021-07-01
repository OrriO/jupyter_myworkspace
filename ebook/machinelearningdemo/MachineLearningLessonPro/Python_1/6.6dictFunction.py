#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 15:25
# @Author  : Z
# @Email   : S
# @File    : 6.6dictFunction.py
d1={1:"Apple",2:"pear"}
d2={3:"Apple",4:"pear"}
print(d1)
print(d2)
# Python字典包含了以下内置函数：
# 1、cmp(dict1, dict2)：比较两个字典元素。
# print(cmp(d1,d2))
# 2、len(dict)：计算字典元素个数，即键的总数。
print(len(d1))
# 3、str(dict)：输出字典可打印的字符串表示。
s1=str(d1)
print(s1)
# 4、type(variable)：返回输入的变量类型，如果变量是字典就返回字典类型。
# Python字典包含了以下内置方法：
# 1、radiansdict.clear()：删除字典内所有元素
l2={"pple":1}
l2.clear()
print(l2)
# 2、radiansdict.copy()：返回一个字典的浅复制
# 3、radiansdict.fromkeys()：创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# 如：print "fromkeys",dict_2.fromkeys(dict_2,10)
# 4、radiansdict.get(key, default=None)：返回指定键的值，如果值不在字典中返回default值
print(d1.get(1))
# 5、radiansdict.has_key(key)：如果键在字典dict里返回true，否则返回false
# print(d1.has_key(1))
# 6、radiansdict.items()：以列表返回可遍历的(键, 值) 元组数组
print(d1.items())
# 7、radiansdict.keys()：以列表返回一个字典所有的键
print(d1.keys())
# 8、radiansdict.setdefault(key, default=None)：和get()类似, 但如果键不已经存在于字典中，将会添加键并将值设为default
d1.setdefault(1,100)
print(d1)
# 9、radiansdict.update(dict2)：把字典dict2的键/值对更新到dict里
d1.update({"apple":1000,"banana":2000})
print(d1)
# 10、radiansdict.values()：以列表返回字典中的所有值
print(d1.values())
