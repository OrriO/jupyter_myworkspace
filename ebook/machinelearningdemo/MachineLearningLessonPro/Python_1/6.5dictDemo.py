#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 15:15
# @Author  : Z
# @Email   : S
# @File    : 6.5dictDemo.py
#字典的创建形式
c1={"Apple":10,"pear":20}
print(c1)
print(type(c1))
c2=dict(name="zhangsan",age=13)
print(c2)
print(type(c2))
c3=dict(zip(["apple",'pear'],[10,20]))
print(c3)
#字典的查询
phone_book={"Azhangsan":100,"lisi":200,"wangwu":300}
print(phone_book["Azhangsan"])
phone_book["Azhangsan"]=178
print(phone_book)
del phone_book["Azhangsan"]
print(phone_book)
#一个键如果重复两次怎么办？----会覆盖
phone_book={"zhangsan":100,"lis":100,"zhangsan":900}
print(phone_book)
#如果一个键没有hash值或可改变的类型都不可以作为键
# print(hash(["zhangsan"])) #TypeError: unhashable type: 'list'
# phone_book={["zhangsan"]:100,"lis":100,"zhangsan":900} #TypeError: unhashable type: 'list'
phone_book={("zhangsan"):100,"lis":100,"zhangsan":900} #TypeError: unhashable type: 'list'
