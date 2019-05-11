'''
         可视化迷宫环境
'''

import numpy as np
import time
import sys

if sys.version_info.major == 2: # pythone的版本
	import Tkinter as tk
else:
	import tkinter as tk

UNIT   = 40 # 迷宫 - 格子边长包含的像素个数
MAZE_H = 4  # 迷宫 - 纵向的格子的个数
MAZE_W = 4  # 迷宫 - 横向的格子的个数

class Maze(tk.Tk, object): # 继承tk.Tk类, object类，
						   # 在python3中object类是自动继承
	# 在创建迷宫这个对象时会被自动调用
	def __init__(self):
		super(Maze, self).__init__() # super会自动递归查找第一个参数指定的类的父类
									 # self是一个要调用__init__方法的实例
		self.action_space = ['u','d','l','r']   # action
		self.n_actions = len(self.action_space) # action的个数
		self.title('maze')                      # 标题
		# {0}：对应数字MAZE_H * UNIT
		# {1}: 对应数字MAZE_H * UNIT
		# '{0}x{1}' 对应字符串 160x160
		self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_W * UNIT))
		self._build_maze()   # 把迷宫画出来

	# 画出迷宫
	def _build_maze(self):
		self.canvas = tk.Canvas(self,bg='white',
								height = MAZE_H * UNIT,
								width  = MAZE_W * UNIT)
		# create grids
		for colu in range(0, MAZE_W * UNIT, UNIT):  # colu: 0,1,2,3,..., MAZE_W*UNIT - 1
			x0,y0,x1,y1 = colu, 0, colu, MAZE_H * UNIT
			self.canvas.create_line(x0,y0,x1,y1)  # 画竖线
		for row  in range(0, MAZE_H * UNIT, UNIT):
			x0,y0,x1,y1 = 0, row, MAZE_W * UNIT, row
			self.canvas.create_line(x0,y0,x1,y1)  # 画横线

		# create origin
		origin = np.array([20,20]) # origin: 一个一维数组[20,20]

		# hell1 - black rect
		hell1_center = origin + np.array([UNIT * 2, UNIT])
		self.hell1 = self.canvas.create_rectangle(
				hell1_center[0] - 15, hell1_center[1] - 15,
				hell1_center[0] + 15, hell1_center[1] + 15,
				fill = 'black')
		
		# hell2 - black rect
		hell2_center = origin + np.array([UNIT, UNIT * 2]) 
		self.hell2 = self.canvas.create_rectangle(
				hell2_center[0] - 15, hell2_center[1] - 15,
				hell2_center[0] + 15, hell2_center[1] + 15,
				fill = 'black')

		# paradise - yellow oval
		paradise_center = origin + UNIT * 2
		self.paradise = self.canvas.create_oval(
				paradise_center[0] - 15, paradise_center[1] - 15,
				paradise_center[0] + 15, paradise_center[1] + 15,
				fill = 'yellow')
		
		# explorer - red rect
		self.explorer = self.canvas.create_rectangle(
				origin[0] - 15, origin[1] - 15,
				origin[0] + 15, origin[1] + 15,
				fill = 'red')

		# pack all
		self.canvas.pack()

	# 让迷宫中的探索者explorer回到起点,并给出环境的反馈（位置坐标）
    # 反馈有两种表现形式，一种是给人看的（图形），一种是给机器的（返回值）
	def explorer_reset(self):
		time.sleep(0.5)
		self.canvas.delete(self.explorer)
		origin = np.array([20,20])
		self.explorer = self.canvas.create_rectangle(
				origin[0] - 15, origin[1] - 15,
				origin[0] + 15, origin[1] + 15,
				fill = 'red')

		self.update()
		# return observation
		return self.canvas.coords(self.explorer)

	# 让迷宫中的探索者按动作action移动，并给出环境的反馈（位置坐标, 奖励reward,  是否已到达终点）
    # 反馈有两种表现形式，一种是给人看的（图形），一种是给机器的（返回值）
	def explorer_step(self, action):
		s = self.canvas.coords(self.explorer)
		base_action = np.array([0,0])
		if action == 0: # up
			if s[1] > UNIT:
				base_action[1] -= UNIT
		elif action == 1: # down
			if s[1] < (MAZE_H - 1) * UNIT:
				base_action[1] += UNIT
		elif action == 2: # left
			if s[0] > UNIT:
				base_action[0] -= UNIT
		elif action == 3: # right
			if s[0] < (MAZE_W - 1) * UNIT:
				base_action[0] += UNIT
		
		# 把explorer(red rect)在x方向上移动base_action[0]
							 #在y方向上移动base_action[1]
		self.canvas.move(self.explorer, base_action[0], base_action[1])
		
		# 得到移动后的explorer(red rect)的状态(坐标)
		s_ = self.canvas.coords(self.explorer)

		# 计算奖励reward
		if s_ in [self.canvas.coords(self.hell1), self.canvas.coords(self.hell2)]:
			reward = -1
			s_ = 'terminal'
			done = True
		elif s_ == self.canvas.coords(self.paradise):
			reward = 1
			done = True
			s_ = 'terminal'
		else:
			reward = 0
			done = False 

		self.update()

		return s_, reward, done
	
#------------------  以下是测试代码  -------------------

# 让explorer回归原位后，一直往右移动
def test_moveRight():
	for t in range(10):
		s = env.reset() # 
		while True:
			env.render()
			a = 3  # 往下走一步
			s, r, done = env.step(a)
			if done:
				break

if __name__ == '__main__':
	env = Maze() # 1. 创建对象env(绘制迷宫)
	env.reset()  # 2. env的探索者回到原点
	env.after(100, moveRight) # 100ms之后往右移动一步
	env.mainloop()
