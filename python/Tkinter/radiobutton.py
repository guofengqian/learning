import tkinter as tk

# 创建主窗口
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# 创建一个label
var = tk.StringVar()
l   = tk.Label(window,bg='yellow',width=20,text='empty')
l.pack()

# 触发功能
def print_selection():
	l.config(text='you have selected '+var.get())

# 创建一个radiobutton部件
r1 = tk.Radiobutton(window,text='Option A',
		variable = var, value = 'A',# 当鼠标选中了其中一个选项，把
		                            # value的值A放到变量var中
		command = print_selection)
r1.pack()

r2 = tk.Radiobutton(window,text='Option B',
		variable = var, value = 'B',# 当鼠标选中了其中一个选项，把
		                            # value的值B放到变量var中
		command = print_selection)
r2.pack()

r3 = tk.Radiobutton(window,text='Option C',
		variable = var, value = 'C',# 当鼠标选中了其中一个选项，把
		                            # value的值C放到变量var中
		command = print_selection)
r3.pack()


# 进行显示
window.mainloop()


