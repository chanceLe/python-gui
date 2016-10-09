#!user/bin/python
#coding=utf-8

from Tkinter import *
import tkMessageBox

def printEventInfo(event):
    print "event.time",event.time
    print "event.type",event.type
    print "event.widget",event.widget
    print "event.keysymbol",event.keysym

root = Tk()
b=Button(root,text="Information")
b.bind("<Return>",printEventInfo)
b.pack()
b.focus_set()
root.mainloop()
