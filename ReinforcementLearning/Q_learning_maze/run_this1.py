'''
========= 探索者学习走迷宫 ===========
1. 创建探索者要走的迷宫可视化对象 - 迷宫Maze
2. 创建探索者的强化学习大脑       - RL_brain
3. 探索者走try_times次迷宫：
	1) 探索者走到迷宫入口

	for 
	1）RL_brain根据当前迷宫的探索者的状态，决定要采取的动作action
	2）迷宫Maze中的探索者执行action的动作，返回探索者下一个状态，此次行动
的评分，以及是否走到出口的标志
	3）RL_brain根据迷宫Maze返回的信息，更新内部的信息
'''


from env_maze1 import Maze
from RL_brain1 import Q_LearingTable # Q是quality的意思，表示行为的质量

TRY_TIMES = 100

def run_maze():
	env_maze = Maze()	
	state = env_maze.reset()
	brain   = Q_Learning()
	for episode in TRY_TIMES:
		action = brain.choose_action(state) 
		state_,reward,done = env_maze.step(action)
		brain.update(state,reward)
		state = state_
def update():
		


if __name__ == '__main__':
	# 1. 可视化环境（可视化尝试的过程，以及给出反馈reward）
	env   = Maze()

	# 2. 大脑（探索者的大脑决策依据是内部的一张Q表，
	#          探索者在环境中尝试后的反馈用来维护这张Q表）
	brain = Q_learning(np.array[0,1,2,3])

	# 3. 探索者走TY_TIMES次迷宫（从初始state走到出口算一次）
	for epsiode in range(TRY_TIMES):
		# 探索者的初始state
		state = env.reset() 

		# 根据过往经验走迷宫，不停走不停更新过往经验，直到到达出口
		while True:
			# 大脑基于探索者当前state选择最佳动作action
			action = brain.choose_action(state)

			# 去环境中执行动作action，
			# 返回探索者在环境中的下一状态state_，
			# 返回探索者此次动作的奖励reward，
			# 返回探索者是否已经到达重点的标志done
			state_,reward,done = env.step(action)

			# 大脑根据环境的反馈，更新探索者在状态state下采取动作action的Q值（quality）
			brain.update(state,reward,state_)

			# 更新探索者的state
			state = state_
			if done:
				break

						
