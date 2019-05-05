'''
Reinfocement learning maze example.

对象：
	Maze -> canvas -> hell1     (black rectangle)  [reward = -1]
                   -> hell2     (black rectangle)  [reward = -1]
                   -> paradise  (yellow oval)      [reward = +1]
                   -> explorer  (red rectangle)   
                   -> all other status  (bakcground rectangle) [reward = 0] 
方法：
	__init__(self):    创建对象
	reset(self):       让探索者explorer回到原点
	step(self,action): 让探索者explorer按action指定的方向移动一步
	render()：         测试用：每过0.1s，往右移动explorer一格

This script is the environment part of this example. The RL is in RL_brain.py.
'''

import numpy as np
import time
import sys

if sys.version_info.major == 2: # pythone的版本
	import Tkinter as tk
else:
	import tkinter as tk


UNIT   = 40 # pixels
MAZE_H = 4  # grid height
MAZE_W = 4  # grid width

class Maze(tk.Tk, object): # 继承tk.Tk类, object类，
						   # 在python3中object类是自动继承
	def __init__(self):
		super(Maze, self).__init__() # super会自动递归查找第一个参数指定的类的父类
									 # self是一个要调用__init__方法的实例
		self.action_space = ['u','d','l','r']   # action
		self.n_actions = len(self.action_space) # action的个数
		self.title('maze')					  # 标题
		# {0}：对应数字MAZE_H * UNIT
		# {1}: 对应数字MAZE_H * UNIT
		# '{0}x{1}' 对应字符串 160x160
		self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_W * UNIT))
		self._build_maze()   # 把迷宫画出来

	def _build_maze(self):
		self.canvas = tk.Canvas(self,bg='white',
								height = MAZE_H * UNIT,
								width  = MAZE_W * UNIT)
		# create grids
		for colu in range(0, MAZE_W * UNIT, UNIT):  # colu: 0,1,2,3,..., MZE_W*UNIT - 1
			x0,y0,x1,y1 = colu, 0, colu, MAZE_H * UNIT
			self.canvas.create_line(x0,y0,x1,y1)  # 竖线
		for row  in range(0, MAZE_H * UNIT, UNIT):
			x0,y0,x1,y1 = 0, row, MAZE_W * UNIT, row
			self.canvas.create_line(x0,y0,x1,y1)  # 横线

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

	# explorer（red rect）销毁后，重新创建回到原点处
	def reset(self):
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

	# 进行动作action，返回explorer(red rect)的新坐标值 
	def step(self, action):
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
		elif action == 3:
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

# 让explorer回归原位后，一直往右移动
def test_moveRight():
	print('update')
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
