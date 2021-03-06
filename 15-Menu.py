#!/user/bin/python
#coding=utf-8
'''
from Tkinter import *

1.使用Menu类来新建一个菜单，Menu和其他的组件一样，第一个是parent，这里通常可以为窗口.
2.然后用add_command来添加菜单项，如果是顶层菜单，菜单项依次向右添加。
    如果是顶层菜单的菜单项，则添加的是下拉菜单的菜单项。
3.add_command参数：label指菜单的名字，command属性指定被点击时调用的方法。
	acceletor指定的是快捷键。underline属性表示是否拥有下划线。
4.用窗口的menu属性指定哪一个作为顶层菜单。
5.当有子菜单的时候，要用add_cascade(级联的意思)，它的作用只是为了引出后面的子菜单。
6.add_cascade的一个重要属性就是menu，它指明了要把哪个菜单级联到该菜单项，还有label属性，指定菜单名称。

root=Tk()
menubar=Menu(root)
for item in ["文件","视图","编辑","关于"]:
	menubar.add_command(label=item)

root["menu"]=menubar
root.mainloop()
'''
from Tkinter import *
root=Tk()

menubar=Menu(root)

#for item in ["文件","视图","编辑","关于"]:
#	menubar.add_command(label=item)

fmenu=Menu(menubar)
for item in ["新建","打开","保存","另存为","退出"]:
	fmenu.add_command(label=item)

emenu=Menu(menubar)
for item in ["复制","粘贴","剪切"]:
	emenu.add_command(label=item)

vmenu=Menu(menubar)
for	 item in ["默认视图","新视图"]:
	vmenu.add_command(label=item)

amenu=Menu(menubar)
for item in ["版权信息","其他说明"]:
	amenu.add_command(label=item)

menubar.add_cascade(label="文件",menu=fmenu)
menubar.add_cascade(label="视图",menu=vmenu)
menubar.add_cascade(label="编辑",menu=emenu)
menubar.add_cascade(label="关于",menu=amenu)

root["menu"]=menubar
root.mainloop()
	

