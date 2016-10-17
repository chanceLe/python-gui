#!/user/bin/python
#coding=utf-8

'''
tkinter中的对话框，要注意python版本。不同体现在引用格式import上。
'''
#下面是python3的引入方式
# from tkinter.dialog import *
# from tkinter import *

#下面是python2的引入方式
from Tkinter import *
import tkSimpleDialog as dl

def fn():
    #这是python3 的对话框创建
    # d=Dialog(None,title="此处是标题",text="你对本页面满意码？",bitmap=DIALOG_ICON,default=1,strings=("不满意","还可以","满意"))
    # print d.num

    #python2的对话框创建,这里的例子askinteger表示输入数字的对话框。还可以是askstring。
    d=dl.askinteger("hello","world")
    print d


t=Button(None,text="页面调查",command=fn)
t.pack()
b=Button(None,text="关闭",command=t.quit)
b.pack()

t.mainloop()
