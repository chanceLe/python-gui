#!/user/bin/python
#coding=utf-8

from Tkinter import *
#以下代码演示如何绑定按钮与函数，也可用command=fn来实现。
#其中<Button-1>表示鼠标左击事件。
'''
def fn(event):
    global  root;
    s=Label(root,text="I love python")
    s.pack()
root=Tk()
#b=Button(root,text="I love Html!",command=fn)
b=Button(root,text="hello")
b.bind("<Button-1>",fn)
b.pack()
'''
root=Tk()
b1=Button(root,text="你好啊！")
b1['width']=20
b1['height']=5
b1['background']='red'
b1.pack()
root.mainloop()