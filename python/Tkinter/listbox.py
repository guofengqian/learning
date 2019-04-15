import tkinter as tk

# 创建主窗口
window = tk.Tk()
window.title('my window')
window.geometry('400x400')

# 创建一个label
var1 = tk.StringVar()
l = tk.Label(window,bg='yellow',width=4,textvariable=var1)
l.pack()

# 创建一个listbox
var2 = tk.StringVar()
var2.set((11,22,33,44))
lb = tk.Listbox(window,listvariable=var2)
list_items = [1,2,3,4]
for item in list_items:
	lb.insert('end',item) #从底部开始插入
lb.insert(0,'zero')
lb.insert(1,'first')
lb.insert(2,'second')
lb.delete(2)
lb.pack()

# 按钮
def print_selection():
	value = lb.get(lb.curselection())
	var1.set(value)
b1 = tk.Button(window,text='print selection',width=15,
		height=2,command = print_selection)
b1.pack()

# 进行显示
window.mainloop()
