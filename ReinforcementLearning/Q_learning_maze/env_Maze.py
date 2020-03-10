'''
         可视化迷宫环境 - 迷宫
'''

import numpy as np
import time
import sys

if sys.version_info.major == 2: # pythone的版本
	import Tkinter as tk
else:
	import tkinter as tk

# GRID_X_NUM * GRID_Y_NUM的迷宫
GRID_SIDE_LENGTH = 40 # 迷宫中每个格子GRID的边长
GRID_X_NUM       = 4  # 迷宫中X轴方向的格子GRID数量
GRID_Y_NUM       = 4  # 迷宫中Y轴方向的格子GRID数量

# 迷宫中各元素的坐标值 X0, Y0, X1, Y1
EXPLORER_INIT_COORDS  = [0,                    0,                  GRID_SIDE_LENGTH,   GRID_SIDE_LENGTH] # 探索者 
TRAP_1_COORDS         = [  GRID_SIDE_LENGTH,   GRID_SIDE_LENGTH, 2*GRID_SIDE_LENGTH, 2*GRID_SIDE_LENGTH] # 陷阱1 
TRAP_2_COORDS         = [2*GRID_SIDE_LENGTH, 2*GRID_SIDE_LENGTH, 3*GRID_SIDE_LENGTH, 3*GRID_SIDE_LENGTH] # 陷阱2
EXIT_COORDS           = [2*GRID_SIDE_LENGTH,   GRID_SIDE_LENGTH, 3*GRID_SIDE_LENGTH, 2*GRID_SIDE_LENGTH] # 出口

# 迷宫中可采取的行为
ACTION_NORTH    = 'north' # 向北走
ACTION_SOUTH    = 'south' # 向南走
ACTION_WEST     = 'west'  # 向西走
ACTION_EAST     = 'east'  # 向东走

# 迷宫
class Maze(tk.Tk, object): # 继承tk.Tk类, object类，
						   # 在python3中object类是自动继承
	# 在创建迷宫这个对象时会被自动调用
	def __init__(self):
		super(Maze, self).__init__() # super会自动递归查找第一个参数指定的类的父类
									 # self是一个要调用__init__方法的实例
		self.title('maze')           # 标题
		self.actions = [ACTION_NORTH, ACTION_SOUTH, ACTION_WEST, ACTION_EAST]        # 在迷宫中可采取的action的种类
		# 迷宫的尺寸 
		self.geometry('{0}x{1}'.format(GRID_X_NUM * GRID_SIDE_LENGTH, GRID_Y_NUM * GRID_SIDE_LENGTH))
		# 画出迷宫 
		self._build_maze()   

	# 画出迷宫
	def _build_maze(self):
		# 画出长为width,宽为height，背景色为blue的画布canvas
		self.canvas = tk.Canvas(self,bg='blue',
								height = GRID_Y_NUM * GRID_SIDE_LENGTH,
								width  = GRID_X_NUM * GRID_SIDE_LENGTH)
		# 在canvas上画GRID_X_NUM条, 间隔为GRID_SIDE_LENGTH的竖线
		for colu in range(0, GRID_X_NUM * GRID_SIDE_LENGTH, GRID_SIDE_LENGTH):  # colu: 0,UNIT - 1, 2*UNIT - 1, ... , MAZE_W*UNIT - 1
			x0,y0,x1,y1 = colu, 0, colu, GRID_X_NUM * GRID_SIDE_LENGTH
			self.canvas.create_line(x0,y0,x1,y1)  # 画竖线
		# 在canvas上画GRID_X_NUM条, 间隔为GRID_SIDE_LENGTH的竖线
		for row  in range(0, GRID_Y_NUM * GRID_SIDE_LENGTH, GRID_SIDE_LENGTH):
			x0,y0,x1,y1 = 0, row, GRID_Y_NUM * GRID_SIDE_LENGTH, row
			self.canvas.create_line(x0,y0,x1,y1)  # 画横线

		# 在canvas上画出一个红色矩形，表示探索者
		self.explorer = self.canvas.create_rectangle( EXPLORER_INIT_COORDS[0], EXPLORER_INIT_COORDS[1], # 左上角的坐标X0,Y0
													  EXPLORER_INIT_COORDS[2], EXPLORER_INIT_COORDS[3], # 右下角的坐标X1,Y1
				                                      fill = 'red')

		# 在canvas上画出一个黑色矩形，表示陷阱1区 
		self.trap_1  = self.canvas.create_rectangle( TRAP_1_COORDS[0], TRAP_1_COORDS[1], # 左上角的坐标X0,Y0
				                                     TRAP_1_COORDS[2], TRAP_1_COORDS[3], # 右下角的坐标X1,Y1
				                                     fill = 'black')
		
		# 在canvas上画出一个黑色矩形，表示陷阱2区 
		self.trap_2  = self.canvas.create_rectangle( TRAP_2_COORDS[0], TRAP_2_COORDS[1], # 左上角的坐标X0,Y0
				                                     TRAP_2_COORDS[2], TRAP_2_COORDS[3], # 右下角的坐标X1,Y1
				                                     fill = 'black')
		# 在canvas上画出一个黄色的椭圆形，表示出口
		self.exit   = self.canvas.create_rectangle( EXIT_COORDS[0], EXIT_COORDS[1], # 左上角的坐标
				                                    EXIT_COORDS[2], EXIT_COORDS[3], # 右下角的坐标
				                                    fill = 'yellow')
		
		# canvas上的部件的布局 
		self.canvas.pack()

	# 让迷宫中的探索者explorer回到起点,并给出环境的反馈（位置坐标）
    # 反馈有两种表现形式，一种是给人看的（图形），一种是给机器的（返回值）
	def explorer_reset(self):
		time.sleep(0.5)
		self.canvas.delete(self.explorer)
		self.explorer = self.canvas.create_rectangle( EXPLORER_INIT_COORDS[0], EXPLORER_INIT_COORDS[1], # 左上角的坐标X0,Y0
													  EXPLORER_INIT_COORDS[2], EXPLORER_INIT_COORDS[3], # 右下角的坐标X1,Y1
				                                      fill = 'red')
		self.update()
		# return observation
		return self.canvas.coords(self.explorer)

	# 让迷宫中的探索者按动作action移动，并给出环境的反馈（位置坐标, 奖励reward,  是否已到达终点）
    # 反馈有两种表现形式，一种是给人看的（图形），一种是给机器的（返回值）
	def explorer_step(self, action):
		# 往action的方向移动一格 
		current_coords = self.canvas.coords(self.explorer) # current_coords[0]是explorer左上角的X坐标,current[1]是explorer左上角的Y坐标
		                                                   # current_coords[2]是explorer右下角的X坐标,current[3]是explorer右下角的Y坐标
		print("current_coords = : ", current_coords)

		if (action == ACTION_NORTH) and  (current_coords[1] > GRID_SIDE_LENGTH):  
			self.canvas.move(self.explorer, 0, -GRID_SIDE_LENGTH)        # 探索者往北移动一格
			print("向北移动一格")
		elif (action == ACTION_SOUTH) and (current_coords[3] < (GRID_Y_NUM - 1) * GRID_SIDE_LENGTH): 
			self.canvas.move(self.explorer, 0, +GRID_SIDE_LENGTH)        # 探索者往南移动一格
			print("向南移动一格")
		elif (action == ACTION_WEST) and (current_coords[0] > GRID_SIDE_LENGTH):
			self.canvas.move(self.explorer, -GRID_SIDE_LENGTH, 0)        # 探索者往西移动一格
			print("向西移动一格")
		elif (action == ACTION_EAST) and (current_coords[2] < (GRID_X_NUM - 1) * GRID_SIDE_LENGTH): 
			self.canvas.move(self.explorer, +GRID_SIDE_LENGTH, 0)        # 探索者往东移动一格
			print("向东移动一格")

		# 计算奖励reward
		next_coords = self.canvas.coords(self.explorer) # 得到移动后的explorer(red rect)的状态(坐标)
		if next_coords in [self.canvas.coords(self.trap_1), self.canvas.coords(self.trap_2)]:
			reward = -1
			next_coords = 'terminal'
			done = True
			print("踩到陷阱1或者2")
		elif next_coords == self.canvas.coords(self.exit):
			reward = 1
			next_coords = 'terminal'
			done = True
			print("来到出口")
		else:
			reward = 0
			done = False 

		self.update()

		return next_coords, reward, done
	
#------------------  以下是测试代码  -------------------

# 让explorer回归原位后，
if __name__ == '__main__':
	env = Maze()                                               # 创建对象env(绘制迷宫)
	env.explorer_reset()                                       # env的探索者回到原点
	time.sleep(1)
	next_coords,reward,done = env.explorer_step(ACTION_EAST)  # env的探索者往东走一步
	print(next_coords,reward,done)
	time.sleep(1)
	next_coords,reward,done = env.explorer_step(ACTION_EAST)  # env的探索者往东走一步
	print(next_coords,reward,done)
	time.sleep(1)
	next_coords,reward,done = env.explorer_step(ACTION_SOUTH)  # env的探索者往南走一步
	print(next_coords,reward,done)
	time.sleep(1)
	next_coords,reward,done = env.explorer_step(ACTION_SOUTH)  # env的探索者往南走一步
	print(next_coords,reward,done)
	time.sleep(1)
	next_coords,reward,done = env.explorer_step(ACTION_WEST)  # env的探索者往西走一步
	print(next_coords,reward,done)
	time.sleep(1)
	
	env.destroy()
	env.mainloop() # 让窗口活动起来


