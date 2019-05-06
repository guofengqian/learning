'''

状态          epsilon的概率选Q值最大的动作         动作
*****        (1-epsion)的概率随即选择动作         ******     在环境中执行这个动作a
* s *  ---- --------------------------------->    * a  *   --------------------------
*****                                             ******                            -
  ^                                                                                 -
  -         s=s_             ************      反思         ******************      - 
  ---------------------      * 新Q(s,a) *   <---------      * s_,reward,done  * <----
                             ************                   * ****************         
                      
当dong = True时，单轮探索结束

========= 探索者学习走迷宫 ===========
1. 创建可视化环境env
2. 创建一颗大脑brain
3. 让大脑brain在可视化环境env中学习
'''

import pandas as pd
import time
import numpy  as np
from   maze_env import Maze
from   brain_Q_Learning import Q_LearningTable # Q是quality的意思，表示行为的质量

TRY_TIMES = 100
def learn():
	# start of game
	for epsiode in range(TRY_TIMES):
		# 1. 探索者回到迷宫入口
		state = env.reset() 

		# 2. 探索者走到出口，或者跌入深渊
		while True:

			# 1. 思考当前状态下要走哪一步
			action = brain.choose_action(str(state))
			print('state=',state)

			# 2. 执行action
			state_,reward,done = env.step(action)
			print('reward=',reward)

			# 3. 反思学习
			brain.learning(str(state), action, reward,str(state_))

			# 4. 如果已经到达出口，则推出当前循环 
			print('done=',done)	
			if done:
				break

			# 5. 暂停0.1s，继续下一步
			time.sleep(0.1) 
			state = state_

	# end of game
	print('game over')
	env.destroy()

if __name__ == '__main__':
	# 1. 创建可视化环境
	env   = Maze()

	# 2. 创建大脑
	brain = Q_LearningTable(list(range(env.n_actions)))

	# 3. 大脑在可视化环境中学习
	learn() 

	env.mainloop()
						
