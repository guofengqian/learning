import tkinter as tk

# 创建一个主窗口
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# 创建一个label
l = tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

# 触发功能
def print_selection():
	if (var1.get() == 1) & (var2.get() == 0): 
	#选中第一个选项，未选中第二个选项
		l.config(text='I love only python')
	elif (var1.get() == 0) & (var2.get() == 1):
		l.config(text='I love only C++')
	elif (var1.get() == 0) & (var2.get() == 0):
		l.config(text='I do not love either')
	else:
		l.config(text='I love both')

# 创建两个checkbutton部件
var1 = tk.IntVar()
c1   = tk.Checkbutton(window,text='Python',variable=var1,
		onvalue=1,offvalue=0,command=print_selection)
c1.pack()
var2 = tk.IntVar()
c2   = tk.Checkbutton(window,text='C++',variable=var2,
		onvalue=1,offvalue=0,command=print_selection)
c2.pack()

# 显示
window.mainloop()
