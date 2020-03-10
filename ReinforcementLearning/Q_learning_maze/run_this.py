# -*- coding: utf-8 -*-

'''
运行环境：python3

                       让机器学习走迷宫
1. 创建有一个探索者的模拟环境env，和使用Q_Learning算法的大脑brain.
2. 循环：
        env同时提供反馈给人和brain。给人的是图形，给brain的数字。人根据图形理解env传达给brain的信息
		brain根据env的反馈进行决策（决定探索者下一步怎么走）和学习（学到的是一张Q表）

'''

import pandas as pd
import time
import numpy  as np
from   env_Maze import Maze
from   brain_Q_Learning import Q_LearningTable # Q是quality的意思，表示行为的质量

TRY_TIMES = 100
def learn():
	# start of game
	for epsiode in range(TRY_TIMES):
		print('走第' + str(epsiode) + '次迷宫')
		# 1. 模拟环境 - 让探索者回到起点
		state = env.explorer_reset() 

		# 2. 探索者走到出口，或者跌入深渊
		while True:

			# 1. 大脑 - 思考探索者在state态下要走哪一步
			action = brain.choose_action(str(state))

			# 2. 模拟环境 - 让探索者执行action
			state_,reward,done = env.explorer_step(action)

			# 3. 大脑 - 根据模拟环境的反馈，反思学习（更新Q表）
			brain.learning(str(state), action, reward,str(state_))

			# 4. 模拟环境 - 探索者是否到达终点？ 
			if done:
				print('done == True')
				break

			# 5. 暂停0.1s，继续下一步
			time.sleep(0.1) 
			state = state_

	# end of game
	print('game over')
	env.destroy()

LEARNING_RATE=0.6
REWARD_DECAY =0.9
E_GREEDY     =0.9
if __name__ == '__main__':
	# 1. 创建模拟的可视化环境env和一颗Q_Learning强化学习大脑brain
	env   = Maze() 
	brain = Q_LearningTable(env.actions, LEARNING_RATE, REWARD_DECAY, E_GREEDY)

	# 2. brain从env给的数字反馈中进行学习，我从env给的可视化图形反馈中观看学习过程。
	learn()	
	env.mainloop()
						
