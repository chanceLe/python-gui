#!/user/bin/python
#coding=utf-8

#event事件，bind函数调用规则  窗体对象.bind(事件类型，回调函数)
#所谓回调函数是不用去调用它， 当事件发生的时候，自动调用。
#事件<Button-1>:鼠标左键单击，<Button-3>鼠标右键单击，2是鼠标中键
#<KeyPress-A>表示A键被按下，A可以换成其他键位。
#<Control-V>表示Ctrl和V组合键   <F1>表示按下F1键。
from Tkinter import *

