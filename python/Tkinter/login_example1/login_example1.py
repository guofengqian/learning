import tkinter as tk

# ---- window ----
window = tk.Tk()
window.title('welcome to qianguofeng')
window.geometry('450x300')
	
# ---- window -> image ----- 
canvas     = tk.Canvas(window, height=200, width=500)# 画布
image_file = tk.PhotoImage(file='welcome.gif')    # 图片
image      = canvas.create_image(0,0,anchor='nw', image=image_file) #图片
canvas.pack(side='top') 
# ----- window -> user_name -----
# ----- window -> user_pwd  -----
tk.Label(window,text='User name: ').place(x=50,y=150)
tk.Label(window,text='Password: ').place(x=50,y=190)
var_usr_name   = tk.StringVar()
var_usr_name.set('example@python.com')
entry_usr_name = tk.Entry(window, textvariable=var_usr_name)
entry_usr_name.place(x=160,y=150)
var_usr_pwd    = tk.StringVar()
entry_usr_pwd  = tk.Entry(window,textvariable=var_usr_pwd, show='*') 
entry_usr_pwd.place(x=160,y=190)

# 触发功能
def usr_login():
	pass
def usr_sign_up():
	pass

# ----- window -> login   button -----
# ----- window -> sign up button -----
btn_login = tk.Button(window, text='Login', command=usr_login)
btn_login.place(x=170,y=230)
btn_sign_up = tk.Button(window, text='Sign up', command=usr_sign_up)
btn_sign_up.place(x=270,y=230)

# 显示window
window.mainloop()
