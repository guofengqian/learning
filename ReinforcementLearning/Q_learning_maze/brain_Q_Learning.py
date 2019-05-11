# -*- coding: utf-8 -*-
'''
               Q_Learning强化学习者的大脑 
'''

import pandas as pd
import numpy  as np

class Q_LearningTable:
	def __init__(self, actions, learning_rate=0.6, reward_decay=0.9, e_greedy=0.9):
		self.actions = actions   	 # Q表的列号
		self.lr      = learning_rate # 对现实与估计值之间差距的学习率
		self.gamma   = reward_decay  # 对过去得到过的奖励的衰减率
		self.epsilon = e_greedy      # 选取Q值最大的动作的概率
		self.q_table = pd.DataFrame(columns=actions, dtype=np.float64) # Q表

	#                决策区
	# 以self.epsilon的概率选择maxQ(s,:)对于的a
    # 以(1-self.epsilon)的概率随机选a
	def choose_action(self,s):   # 决策区
		self.check_s_exist(s)	
		if np.random.uniform() < self.epsilon:
			s_a = self.q_table.loc[s, :]
			a = np.random.choice(s_a[s_a == np.max(s_a)].index)
		else:
			a = np.random.choice(self.actions)
		return a

	#               学习区
    # 新Q(s,a) = 估计 + self.lr * (现实 - 估计) = self.lr * 现实 + (1-self.lr) * 估计
    # 现实 = reward + self.gama * Qmax(s_,:)
    # 估计 = 旧Q(s,a)
	def learning(self, s, a, reward, s_):  # 学习区

		self.check_s_exist(s_)
		q_predict = self.q_table.loc[s, a] # 估计
		if s_ != 'terminal':
			q_target = reward + self.gamma * self.q_table.loc[s_,:].max() # 现实
		else:
			q_target = reward 
		self.q_table.loc[s, a] = self.lr * q_target + (1-self.lr) * q_predict # 新Q(s,a)

	def check_s_exist(self, s):
		if s not in self.q_table.index:
			# append new s to q table
			self.q_table = self.q_table.append(
				pd.Series(
					[0]*len(self.actions),
					index = self.q_table.columns,
					name  = s,
				)
			)

