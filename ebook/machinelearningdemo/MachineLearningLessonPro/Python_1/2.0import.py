#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 11:23
# @Author  : Z
# @Email   : S
# @File    : 2.0import.py
import os
print(os.getcwd())
#D:\BigData\Workspace\PycharmProjects\MachineLearningLessonPro\Python_1
os.chdir("D:\\BigData\\Workspace\\PycharmProjects\\MachineLearningLessonPro")
print(os.getcwd())

import requests
text_content=requests.get("https://www.baidu.com")
print(text_content.url)
print(text_content.text)
print(text_content.encoding)
