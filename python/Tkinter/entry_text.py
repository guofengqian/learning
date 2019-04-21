import tkinter as tk

# 窗口
window = tk.Tk()
window.title('my window')#窗口的标题
window.geometry('200x200')#窗口的尺寸

# 输入框
e = tk.Entry(window,show='*')
e.pack()

# 文本框
t = tk.Text(window,height=2)
t.pack()

# 按钮
def insert_point():
	var = e.get()
	t.insert('insert',var)
b1 = tk.Button(window,text="insert point",width=15,height=2,command=insert_point)
b1.pack() #固定

def insert_end():
	var = e.get()
	t.insert('end',var)
b2 = tk.Button(window,text="insert end",command=insert_end)
b2.pack()

#把窗口显示出来
window.mainloop()
