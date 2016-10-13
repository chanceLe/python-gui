#!/user/bin/python
#coding=utf-8

from Tkinter import *
root=Tk()
#gird 布局row 设置第几行（从0开始），column设置一行有几列
#sticky参数（取值N，E，S，W）表示这个组件是从哪个方向开始的。
#grid函数还支持ipadx，ipady，padx，pady，他们表示内边距和外边距，默认是0.
#gird函数还支持rowspan和columnspan表示跨的行数和列数。
Label(root,text="账号：").grid(row=0,sticky=W)
Entry(root).grid(row=0,column=1,sticky=E)

Label(root,text="账号：").grid(row=1,sticky=W)
Entry(root).grid(row=1,column=1,sticky=E)

Button(root,text="登录").grid(row=2,column=1,sticky=E)

root.mainloop()