#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 14:58
# @Author  : Z
# @Email   : S
# @File    : 6.3listFunction.py
l1=[1,2,3,4,5]
l2=[6,7,8,9,10]
# 列表操作包含以下函数:
# 1、cmp(list1, list2)：比较两个列表的元素
# print(cmp(l1,l2))
# 2、len(list)：列表元素个数
print(len(l1))
# 3、max(list)：返回列表元素最大值
print(max(l1))
# 4、min(list)：返回列表元素最小值
print(min(l1))
# 5、list(seq)：将元组转换为列表
# 列表操作包含以下方法:
# 1、list.append(obj)：在列表末尾添加新的对象
print(l1) #[1, 2, 3, 4, 5]
l1.append(900)
l1.append(1000)
print(l1)
# 2、list.count(obj)：统计某个元素在列表中出现的次数
print(l1.count(1))
# 3、list.extend(seq)：在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
l1.extend([1,2,3,4,5])
print(l1)
# 4、list.index(obj)：从列表中找出某个值第一个匹配项的索引位置
print(l1.index(1))
# 5、list.insert(index, obj)：将对象插入列表
l1.insert(0,"apple")
print(l1)
# 6、list.pop(obj=list[-1])：移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
print(l1.pop())
print(l1.pop())
print(l1.pop())
print(l1.pop())
print(l1.pop())
print(l1.pop())
print(l1.pop())
# 7、list.remove(obj)：移除列表中某个值的第一个匹配项
l1.remove("apple")
print(l1)
# 8、list.reverse()：反向列表中元素
l1.reverse()
print(l1)
# 9、list.sort([func])：对原列表进行排序
