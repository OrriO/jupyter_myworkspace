
#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 20:43
# @Author  : Z
# @Email   : S
# @File    : 08.file_input.py
def writeFile():
    sen = '''\
This is first line!
This is second line!
This is third line!
This is last line!\
'''
    f = open("sentecnce.txt", mode="w")
    f.writelines(sen)
    f.close()
def readLines():
    f = open("sentecnce.txt", mode="r")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end="")

if __name__ == '__main__':
    # writeFile()
    readLines()