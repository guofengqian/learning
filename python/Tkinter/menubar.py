import tkinter as tk

# 对象声明
window   = tk.Tk()                    # window
menubar  = tk.Menu(window)            # window   -> menubar 
editmenu = tk.Menu(menubar)           # menubar  -> editmenu
filemenu = tk.Menu(menubar,tearoff=0) # menubar  -> filemenu
submenu  = tk.Menu(filemenu)          # filemenu -> submenu

l = tk.Label(window, text='', bg='yellow') # label

# 触发功能声明
counter = 0
def do_job():
	global counter
	l.config(text='do '+ str(counter))
	counter += 1

# window 
window.title('my window')
window.geometry('200x200')
window.config(menu=menubar)

# window -> menubar 
menubar.add_cascade(label='File',menu=filemenu)
menubar.add_cascade(label='Edit',menu=editmenu)

# menubar -> filemenu
# 如果点击这些单元，就会触发do_job的功能
filemenu.add_command(label='New',command=do_job)
filemenu.add_command(label='Open',command=do_job)
filemenu.add_command(label='Save',command=do_job)
filemenu.add_separator() #分割线
filemenu.add_command(label='Exit',command=window.quit)
filemenu.add_cascade(label='Import',menu=submenu,underline=0)

# menubar -> editmenu
editmenu.add_command(label='cut',command=do_job)
editmenu.add_command(label='copy',command=do_job)
editmenu.add_command(label='paste',command=do_job)

# filemenu -> submenu
submenu.add_command(label='Submenu1',command=do_job)

# label
l.pack()

# 进行显示
window.mainloop()
