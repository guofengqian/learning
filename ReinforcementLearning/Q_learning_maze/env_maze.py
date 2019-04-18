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
        super(Maze, self).__init__() # super是自动递归查找第一个参数指定的类的父类
                                     # self是一个要调用__init__方法的实例

    

