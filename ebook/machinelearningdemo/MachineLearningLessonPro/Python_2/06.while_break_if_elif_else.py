#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 20:31
# @Author  : Z
# @Email   : S
# @File    : 04if_elif_else.py
#猜数字游戏
number=100
while  True:
    guessNumber=int(input("Please input your number:"))
    if guessNumber == number:
        print("Wow,you guess number is right!")
        break
    elif guessNumber > number:
        print("Your guess number is larger than before!")
        continue
    else:
        print("Your guess number is smaller than before")
        continue
