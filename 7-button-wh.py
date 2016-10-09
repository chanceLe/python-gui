#!/user/bin/python
#coding=utf-8

from Tkinter import *
root =Tk()

#三种设置Button宽高，同样适用其他控件
b1=Button(root,text="30x1",width=30,height=3).pack()

b2=Button(root,text="30x2")
b2['width']=30
b2["height"]=3
b2.pack()

b3=Button(root,text="30x3")
b3.configure(width=30,height=3)
b3.pack()

#使用anchor设置文本在控件上的显示内容

for i in ["n","s","e","w","ne","nw","se","sw"]:
    Button(root,text="anchor",anchor=i,width=30,height=4).pack()

#通过fg和bg设置来改变button的前景和背景色

#button边框设置bd（bordwidth）：缺省为1或2个像素。
for i in [0,1,2,3,4]:
    Button(root,text=str(i),bd=i).pack()

#设置button风格
for i in ["raised","sunken","groove","ridge","flat"]:
    Button(root,text=i,relief=i,width=30).pack()    

root.mainloop()
