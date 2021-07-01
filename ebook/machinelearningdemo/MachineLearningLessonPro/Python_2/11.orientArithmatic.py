#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 20:56
# @Author  : Z
# @Email   : S
# @File    : 11.orientArithmatic.py
class ArithMatic():
    def __init__(self,x,y):
        self.X=x
        self.Y=y
    def add(self):
        return self.X+self.Y
    def sub(self):
        return self.X-self.Y
    def mul(self):
        return self.X*self.Y
    def div(self):
        return self.X/self.Y
if __name__ == '__main__':
    x=int(input("please input number:"))
    y=int(input("please input another number:"))
    aritcal=ArithMatic(x,y)
    print(aritcal.add())
    print(aritcal.sub())
    print(aritcal.mul())
    print(aritcal.div())