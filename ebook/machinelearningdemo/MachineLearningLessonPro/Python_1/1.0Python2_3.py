#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 11:10
# @Author  : Z
# @Email   : S
# @File    : 1.0Python2_3.py
print("hello")
#编码方式
print("传智播客黑马程序员！")
#查看编码方式
import sys
print(sys.getdefaultencoding())
#python2-ascii
#python-utf-8-------unicode transform format 8bytes    Unicode
#案例
str="黑马程序员"
print(str.encode("gbk"))
#b'\xe9\xbb\x91\xe9\xa9\xac\xe7\xa8\x8b\xe5\xba\x8f\xe5\x91\x98'    utf-8
#b'\xba\xda\xc2\xed\xb3\xcc\xd0\xf2\xd4\xb1'                        gbk
print(b'\xe9\xbb\x91\xe9\xa9\xac\xe7\xa8\x8b\xe5\xba\x8f\xe5\x91\x98'.decode()) #黑马程序员
print(b'\xba\xda\xc2\xed\xb3\xcc\xd0\xf2\xd4\xb1'.decode("GBK")) #黑马程序员