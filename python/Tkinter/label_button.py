#!/usr/bin/python
#coding:utf-8
#上面两行代码是为了保证python可以处理中文
#使用python3运行，它自带tkinter 
import tkinter as tk

window = tk.Tk()
window.title('my window')
window.geometry('200x100')
#按钮
on_hit = False
def hit_me():
	global on_hit
	if on_hit == False:
		on_hit = True
		var.set('you hit me') #设置标签的文字为'you hit me'
	else:
		on_hit = False
		var.set('') # 设置文字为空

b = tk.Button(window,
	text    = 'hit me', #显示在按钮上的文字
	width   = 15, height =2, 
	command = hit_me #点击按钮时执行的命令
	)	
b.pack() #按钮位置

#标签
var = tk.StringVar()  #文字变量存储器
l = tk.Label(window,
		text = 'OMG! this is TK!',
		textvariable = var,  #使用textvaribale替换text，因为这个可以变化
		bg   = 'green',     #背景颜色
		font = ('Arial',12),#标签的字体
		width= 15, height=2 #标签的长宽
		)
l.pack() #固定窗口位置

#这里是窗口的内容 
window.mainloop()
