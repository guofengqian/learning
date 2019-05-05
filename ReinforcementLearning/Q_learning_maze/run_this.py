'''
========= 探索者学习走迷宫 ===========
1. 创建探索者要走的迷宫可视化对象 - 迷宫Maze
2. 创建探索者的强化学习大脑       - RL_brain
3. 探索者走try_times次迷宫：
	1) 探索者走到迷宫入口
	for 
	1）思考：大脑RL_brain根据过去经验（Q表），以epsilon的概率选择在当前状态下Q值最大的action,
	                                          以(1-essilon)的概率选择别的action
	2）行动：env_maze中的探索者执行action这个动作，得到相应的反馈（下一状态s_，奖励reward，及是否到达终点）
	3）刷新头脑里的经验（Q(s,a)): 使用过去的经验Qmax(s_) 
		新估计Q(s,a) = 旧估计Q(s,a) + learning_rate * (reward + GAMA * 假想的现实Qmax(s_) - 旧估计Q(s,a))
	2）迷宫Maze中的探索者执行action的动作，返回探索者下一个状态，此次行动
的评分，以及是否走到出口的标志
	3）RL_brain根据迷宫Maze返回的信息，更新内部的信息
'''

import pandas as pd
import time
import numpy  as np
from maze_env import Maze
from RL_brain import Q_LearningTable # Q是quality的意思，表示行为的质量

TRY_TIMES = 100
def update():
	for epsiode in range(TRY_TIMES):
		# 探索者的初始state
		state = env.reset() 

		# 根据过往经验走迷宫，不停走不停更新过往经验，直到到达出口
		while True:

			# 思考：state状态下要采取的动作action
			action = brain.choose_action(str(state))

			# 执行：在state状态下执行动作action，返回（到达的下一状态state_,获得的奖励，是否到达终点的标志）
			state_,reward,done = env.step(action)

			# 学习：使用假想的Qmax(s_)，及获得的奖励reward来更新Q(s,a)
			brain.learning(str(state), action, reward,str(state_))

			# 在当前状态暂留0.1s，方便看清探索者走的每一步
			time.sleep(0.1) 
			state = state_

			print('state=',state)
			print('done=',done)

			if done:
				break

	# end of game
	print('game over')
	env.destroy()

if __name__ == '__main__':
	# 1. 可视化环境（可视化尝试的过程，以及给出反馈reward）
	env   = Maze()

	# 2. 大脑（探索者的大脑决策依据是内部的一张Q表，
	#          探索者在环境中尝试后的反馈用来维护这张Q表）
	brain = Q_LearningTable(list(range(env.n_actions)))

	# 3. 探索者走TY_TIMES次迷宫（从初始state走到出口算一次）
	env.after(TRY_TIMES, update)
	env.mainloop()
						
