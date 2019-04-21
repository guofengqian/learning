import tkinter as tk

# 对象声明
window = tk.Tk()
l      = tk.Label(window, text='on the window')
frm    = tk.Frame(window)
frm_l  = tk.Frame(frm)
l1_frm_l = tk.Label(frm_l, text='on the frm_l1')
l2_frm_l = tk.Label(frm_l, text='on the frm_l2')
frm_r  = tk.Frame(frm)
r1_frm_r = tk.Label(frm_r, text='on the frm_r1')

# window
window.title('my window')
window.geometry('200x200')

# window -> l
l.pack()

# window -> frm
frm.pack()

# frm -> frm_l, frm -> frm_r
frm_l.pack(side='left')
frm_r.pack(side='right')

# frm_l -> frm_l1, frm_l -> frm_l2
l1_frm_l.pack()
l2_frm_l.pack()
r1_frm_r.pack()

# 显示window
window.mainloop()
