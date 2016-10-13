#!/user/bin/python
#coding=utf-8

from Tkinter import *
root=Tk()
Button(root,text="A").pack(side=LEFT,expand=YES,ipadx=5,fill=X)
Button(root,text="B").pack(side=RIGHT,expand=YES,ipadx=5,fill=Y)
Button(root,text="C").pack(side=TOP,expand=YES,ipadx=5,fill=BOTH)
Button(root,text="D").pack(side=BOTTOM,expand=YES,ipadx=5,fill=NONE)
Button(root,text="E").pack(side=LEFT,expand=YES,ipadx=5,fill=X)
root.mainloop()


