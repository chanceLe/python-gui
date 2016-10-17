#!/user/bin/python
#coding=utf-8

'''
checkbutton 原指复选按钮，用add_checkbutton添加复选菜单
radiobutton 原指单选按钮，用add_radiobutton添加单选菜单
 这两种菜单一旦被选定，那么前边会有一个对号标记出现。
'''
from Tkinter import *
root=Tk()
m=Menu(root)
m2=Menu(m)

for i in ["python","java","php"]:
    m2.add_checkbutton(label=i)
m2.add_separator()

for i in ["c","c++","swift"]:
    m2.add_radiobutton(label=i)

m.add_cascade(label="lan",menu=m2)
root['menu']=m
root.mainloop()
