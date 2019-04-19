'''
Reinfocement learning maze example.

Red rectangle:      explorer.
Black rectangles:   hells       [reward = -1].
Yellow bin circle:  paradise    [reward = +1].
All other status:   ground      [reward = 0].

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
        self.title('maze')                      # 标题
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
        hell2_center = origin + UNIT * 2
        self.hell2 = self.canvas.create_rectangle(
                hell2_center[0] - 15, hell2_center[1] - 15,
                hell2_center[0] + 15, hell2_center[1] + 15,
                fill = 'black')

        # paradise - yellow oval
        paradise_center = origin + UNIT
        self.paradise = self.canvas.create_oval(
                paradise_center[0] - 15, paradise_center[1] - 15,
                parasise_center[0] + 15, paradise_center[1] + 15,
                fill = 'yellow')
        
        # explorer - red rect
        self.explorer = self.canvas.create_rectangle(
                origin[0] - 15, origin[1] - 15,
                origin[0] + 15, origin[1] + 15,
                fill = 'red')

        # pack all
        self.canvas.pack()

    def reset(self):
        self.update()
        time.sleep(0.5)
        self.canvas.delete(self.explorer)
        origin = np.array([20,20])
        self.explorer = self.canvas.create_rectangle(
                origin[0] - 15, origin[1] - 15,
                origin[0] + 15, origin[1] + 15,
                fill = 'red')
        # return observation
        return self.canvas.coords(self.explorer)

   def step(self, action):
        s = self.coords(self.explorer)
        base_action = np.array([0,0])
        if action == 0: # up
            if s[1] > UNIT
                s[1] 
