# this is canvas画布
import tkinter as tk

# 创建一个主窗口
window = tk.Tk()
window.title('my window')
window.geometry('200x200')

# 创建一个变量存放图片
image_file = tk.PhotoImage(file='ins.gif')

# 创建一个canvas
canvas = tk.Canvas(window,bg='blue',height=100,width=200)
      # 10,10表示图片放入画布的坐标
      # anchor='nw'是把图片的左上角作为锚定点
image = canvas.create_image(10,10,anchor='nw',image=image_file)
canvas.pack()

# 创建一条直线
x0,y0,x1,y1 = 50,50,80,80
line = canvas.create_line(x0,y0,x1,y1)
# 创建一个圆
oval = canvas.create_oval(x0,y0,x1,y1,fill='red')
#创建一个扇形
arc  = canvas.create_arc(x0+30,y0+30,x1+30,y1+30,start=0,extent=18)#创建一个矩形
rect = canvas.create_rectangle(100,30,100+20,30+20)

# 触发功能
def movedown():
	canvas.move(rect,0,2) #把rect这个对象，横向移动0个单位，纵向移动两个单位

def moveup():
	canvas.move(rect,0,-2) #把rect这个对象，横向移动0个单位，纵向移动两个单位
# 创建一个按键
b1 = tk.Button(window,text='movedown',command=movedown).pack()
b2 = tk.Button(window,text='moveup',command=moveup).pack()

#显示
window.mainloop()
