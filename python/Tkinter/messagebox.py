import tkinter as tk
import tkinter.messagebox as tms

# 函数声明
def hit_me():
	tms.showinfo(title='Hi', message='hahahha')

# 对象声明
window = tk.Tk()
b      = tk.Button(window,text='hit me', command=hit_me)

# window
window.title('my window')
window.geometry('200x200')

# window -> b
b.pack()

# 显示window
window.mainloop()

