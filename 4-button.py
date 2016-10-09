#!user/bin/python
#coding=utf-8

from Tkinter import *
import tkMessageBox
root=Tk()
root.Wm_title=("Welcome !")
'''
Label(root,fg="red",bg="blue",width=100,height=5,text="hello Tkinter").pack()
Label(root,fg="red",bg="green",width=100,height=5,text="hello Tkinter").pack()
Label(root,fg="red",bg="yellow",width=100,height=5,text="hello Tkinter").pack()

def helloButton():
    print "I want go to somewhere!"
Button(root,text="1",command=helloButton).pack()
Button(root,text="2",command=helloButton).pack()
Button(root,text="3",command=helloButton).pack()
Button(root,text="4",command=helloButton).pack()
Button(root,text="5",command=helloButton).pack()
Button(root,text="6",command=helloButton).pack()
Button(root,text="7",command=helloButton).pack()
Button(root,text="8",command=helloButton).pack()
Button(root,text="9",command=helloButton).pack()
Button(root,text="0",command=helloButton).pack()
Button(root,text="+",command=helloButton).pack()
Button(root,text="-",command=helloButton).pack()
Button(root,text="×",command=helloButton).pack()
Button(root,text="÷",command=helloButton).pack()
Button(root,text="=",command=helloButton).pack()

print"-"*50
#alertButton=Button(root,text="计算器",command=hello).pack()

Button(root,text="hello Button",relief=FLAT).pack()
Button(root,text="hello Button",relief=GROOVE).pack()
Button(root,text="hello Button",relief=RAISED).pack()
Button(root,text="hello Button",relief=RIDGE).pack()
Button(root,text="hello Button",relief=SOLID).pack()
Button(root,text="hello Button",relief=SUNKEN).pack()
'''
print"-"*50

Button(root,text="hello world",image=PhotoImage(file="./images/1.gif")).pack()
root.mainloop()
