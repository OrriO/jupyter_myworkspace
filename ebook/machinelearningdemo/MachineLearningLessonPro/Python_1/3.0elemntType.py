#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 11:29
# @Author  : Z
# @Email   : S
# @File    : 3.0elemntType.py
a=199.0
b=199.0
print(id(199.0))
print(id(a))
print(id(b))
print(hash("staring"))
print(type(a)) #<class 'float'>
#补充复数类型
c1=complex(1,2)   #1+2j    j**2=-1
print(c1)  #(1+2j)(1+2j)=1-4+4j=-3+4j
print(c1**2) #(-3+4j)
#单目运算符+ - *乘法 /除法  //整除 **幂 %取模
a=3
b=5
print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a%b)
print(a//b)
#双目运算符---+= -=  *= /= %=  **= //=
print("before value is：",a)
a*=b
a**=b
a+=b
a-=b
a//=b
print("change value is：",a)
# & 按位与 | 按位或 ^按位异或 <<左移 >> 右移
a=3   #0011
b=5   #0101
#&     0001---------1
#|     0111---------7
#^     0110---------6
#a>1  除以2   a<乘以2
#8421  2**3   2**2  2**1 2**0
print(a&b)
print(a|b)
print(a^b)
print(a<<1) #6
print(a<<2) #12
