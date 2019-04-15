import tkinter as tk
import tkinter.messagebox #在导入tkinter时，不会自动导入tk.messagebox
import pickle

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
	usr_name = var_usr_name.get()
	usr_pwd  = var_usr_pwd.get()

	# try/except语句用来检测try语句块中的错误，从而让except语句捕获异常信息并处理
	# 即如果usrs_info.pickle文件不存在，就进入except FileNotFoundError分支
    # 否则，把usr_file中的数据解析为一个python对象usrs_info	
	try:
		# with语句的好处就是在文件打开出错的时候，也会自动关闭文件
		# 'rb'：表示以二进制读模式打开usrs_info.pickle文件
		with open('usrs_info.pickle','rb') as usr_file:
			# 把磁盘中的文件usrs_info.pickle中的信息解析为一个python对象
			usrs_info = pickle.load(usr_file)
	except FileNotFoundError:
		# 'wb'：表示以二进制格式打开usrs_info文件只用于写入，如果该文件不存在就新建
		with open('usrs_info.pickle','wb') as usr_file:
			usrs_info = {'admin': 'admin'}
			# 把一个python对象usrs_info序列化后，存到usr_file文件中
			pickle.dump(usrs_info, usr_file)
	if usr_name in usrs_info:
		if usr_pwd == usrs_info[usr_name]:
			tk.messagebox.showinfo(title='Welcome', message='How are you? '+usr_name)
		else:
			tk.messagebox.showerror(message='Error,your password is wrong, try again.')
	else:
		# 跳出yes/no的窗口，让用户进行选择
#		is_sign_up = tk.messagebox.askyesno('Welcome',
#				'You have not sign up yet. Sign up today?')
		is_sign_up = tk.messagebox.askyesno('Welcome',
				                           'You have not sign up yet. Sign up today?')
		if is_sign_up:
			usr_sign_up()

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
