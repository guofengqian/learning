'''
====== Q_Learning强化学习者的大脑 =======

Q_LearningTable:
           action[0]   action[1]   ...  action[j] ...   action[n]
state_0       Q00          Q01             Q0j            Q0n
state_1       Q10          Q11             Q1j            Q1n
...
state_i       Qi0          Qi1             Qij            Qin
...
state_m       Qm0          Qm1             Qmj            Qmn

在state下选择一个动作action的策略：
	以epsilon的概率选择Q值最大的action，
    以（1-epsilon)的概率随机选择Q值
新的Q值 = 旧Q值 + 
		  奖励值reward（采取当前action获得的） + 
		  在状态state_下最大的Q值（采取当前action后到达的新状态下的最大Q值）
最佳action[j] ： 
	Q值最大
'''


import pandas as pd
import numpy  as np

class Q_LearningTable:
	def __init__(self, actions, learning_rate=0.1, reward_decay=0.9, e_greedy=0.9):
		self.actions = actions # a list	
		self.lr      = learning_rate
		self.gamma   = reward_decay
		self.epsilon = e_greedy
		self.q_table = pd.DataFrame(columns=actions, dtype=np.float64)

	def choose_action(self,state):
		self.check_state_exist(state)	
		if np.random.uniform() < self.epsilon:
			state_action = self.q_table.loc[state, :]
			action = np.random.choice(state_action[state_action == np.max(state_action)].index)
		else:
			action = np.random.choice(self.actions)
		return action

	def learning(self, state, action, reward, state_):
		self.check_state_exist(state_)
		q_predict = self.q_table.loc[state, action]
		if state_ != 'terminal':
			q_target = reward + self.gamma * self.q_table.loc[state_,:].max()
		else:
			q_target = reward 
		self.q_table.loc[state, action] += self.lr * (q_target - q_predict)
		print(self.q_table)

	def check_state_exist(self, state):
		if state not in self.q_table.index:
			# append new state to q table
			self.q_table = self.q_table.append(
				pd.Series(
					[0]*len(self.actions),
					index = self.q_table.columns,
					name  = state,
				)
			)

