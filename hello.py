#!user/bin/python
#coding=utf-8

from Tkinter import *
import tkMessageBox

class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    # def createWidgets(self):
    #     self.helloLabel=Label(self,text="hello,world!")
    #     self.helloLabel.pack()
    #     self.quitButton=Button(self,text='Quit',command=self.quit)
    #     self.quitButton.pack()
    def createWidgets(self):
        self.nameInput=Entry(self)
        self.nameInput.pack()
        self.alertButton=Button(self,text='Hello',command=self.hello)
        self.alertButton.pack()
    def hello(self):
        name=self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message','hello, %s'%name)
        

app=Application()
app.master.title('Hello world')
app.mainloop()
