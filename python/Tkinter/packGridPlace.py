import tkinter as tk

# 对象声明
window = tk.Tk()
l = tk.Label(window, text=1)

#  ---- window ----
window.title('my window')
window.geometry('200x200')

# ---- window -> label ----

#l.pack(side='top') #上
#l.pack(side='bottom')#下
#l.pack(side='left') #左
#l.pack(side='right') #右

# 坐标位置(row*padx, column*pady)
#l.grid(row=0, column=0, padx=10, pady=10) 
#l.grid(row=0, column=1, padx=10, pady=10) 
#l.grid(row=0, column=2, padx=10, pady=10) 

# 给出精确的坐标来定位
l.place(x=40,y=80,anchor='nw') #'nw'表示坐标的锚定点在西北角

# ---- 显示window -----
window.mainloop()
