import tkinter as tk

# 创建主窗口
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# 创建label
l = tk.Label(window,bg='yellow',width=20,text='exmpty')
l.pack()

def print_selection(v):
	l.config(text='you have selected ' + v)

# 创建scale
s = tk.Scale(window,
		label  = 'try me',
		from_  = 5, # 滚动条最小值为5
		to     = 11,# 最大值为11
		orient = tk.HORIZONTAL, # 滚动的方向
		length = 200, # 滚动条的长度，以像素为单位
		showvalue = 1, # 0:表示在滚动条上方不显示值 
		tickinterval = 2,# 坐标上的数字之间的间隔值
		resolution   = 0.01, # 滚动距离精度到小数点后两位
		command = print_selection
		)
s.pack()
# 进行显示
window.mainloop()
