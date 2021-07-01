#-*- coding: utf-8 -*-
# @Time    : 2018/12/2 21:06
# @Author  : Z
# @Email   : S
# @File    : 12.GUI.py
import tkinter.messagebox as mb
import tkinter.simpledialog as dl

mb.showinfo(title="Weclome",message="GuessNumberGame!")
number=100
while True:
    guessNumber=dl.askinteger("Ask integer:","Please input your age:")
    if guessNumber ==number:
        mb.showinfo("Wow","Your will win the whole world!")
        break
    elif guessNumber >number:
        mb.showinfo("error","You guess wrong!larger than before one!")
        continue
    else:
        mb.showinfo("error","You guess wrong!smaller than before one!")
        continue
