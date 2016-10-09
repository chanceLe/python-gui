#!/usr/bin/python
#-*-coding:UTF-8 -*-

from Tkinter import *
root=Tk()

root.wm_title("课程列表")

li=['c','python','php','html','SQL','java']
movie=['css','jQuery','Bootstrap']

listb=Listbox(root)
listb2=Listbox(root)

for item in li:
    listb.insert(0,item)
for item in movie:
     listb2.insert(0,item)

listb.pack()
listb2.pack()

listb.Dimension=(50,20);

root.mainloop()
