#user/bin/python
#coding=utf-8

from Tkinter import *

root=Tk()

Label(root,text="red",bg="red").pack()
Label(root,text="blue",bg="blue").pack()
Label(root,text="yellow",bg="yellow").pack()

Label(root,bg="red",width=10,height=3).pack()
Label(root,bg="blue",width=10,height=3).pack()
Label(root,bg="yellow",width=10,height=3).pack()

Label(root,text="botton",compound="bottom",bitmap="error").pack()
Label(root,text="top",compound="top",bitmap="error").pack()
Label(root,text="right",compound="right",bitmap="error").pack()
Label(root,text="left",compound="left",bitmap="error").pack()
Label(root,text="center",compound="center",bitmap="error").pack()


Label(root,text="Welcome to my blog",bg="yellow",width=10,height=2,wraplength=80,justify="center",anchor="ne").pack()

root.mainloop()
