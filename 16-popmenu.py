#!/user/bin/python
#coding=utf-8

from Tkinter import *
'''
def fn():
    global root
    Label(root,text="I love Python").pack()
root=Tk()
menubar=Menu(root)

for i in ["vb","c","java","python"]:
    menubar.add_command(label=i,command=fn)

#menubar.add_command(label="php",command=fn)

def pop(event):
    menubar.post(event.x_root,event.y_root)

root.bind("<Button-3>",pop)
root.mainloop()


Menu类里有一个post方法，接收两个参数x和y，表示弹出菜单的位置。
绑定鼠标右击事件<Button-3>

 用没有参数的add_separator()方法在菜单项之间插入分割线。
'''
def func():
    global root
    Label(root,text="I love python!").pack()
root=Tk()
m=Menu(root)
m2=Menu(m)

for i in ["python","c","oc","php"]:
    m2.add_command(label=i,command=func)
m2.add_separator()

for i in ["rubby","c++","javascript"]:
    m2.add_command(label=i,command=func)

m.add_cascade(label="lan",menu=m2)  #add_cascade()引出级联菜单
root['menu']=m
root.mainloop()
