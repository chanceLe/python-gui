#! /user/bin/python
#coding=utf-8

from Tkinter import *
root=Tk()

def printState():
    print "state"
#设置button的状态
for i in ["normal","active","disabled"]:
    Button(root,text=i,state=i,width=30,command=printState).pack()

#绑定button与变量，当变量变化时，button控件显示的文本也随之变化
def changeText():
    if b['text']=="text":
        v.set("change")
        print "change"
    else:
        v.set("text")
        print "text"
v=StringVar()
b=Button(root,textvariable=v,command=changeText)
v.set("text")
b.pack()

root.mainloop()
