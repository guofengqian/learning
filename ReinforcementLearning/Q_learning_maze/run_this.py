'''

状态          epsilon的概率选Q值最大的动作         动作
*****        (1-epsion)的概率随即选择动作         ******     在环境中执行这个动作a
* s *  ---- --------------------------------->    * a  *   --------------------------
*****                                             ******                            -
  ^                                                                                 -
  -         s=s_             ************      反思         ******************      - 
  ---------------------      * 新Q(s,a) *   <---------      * s_,reward,done  * <----
                             ************                   * ****************         

s: 探索者在迷宫中的当前位置
a: 探索者在在s位置处选择的行为action
s_：探索者在s位置处执行了行为action后到达的新位置
reward：到达新位置s_，环境给予的反馈奖励
done: 表示迷宫单轮探索是否结束

--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------
--------------------------------------------------------------------------------------


========= 探索者学习走迷宫（实测需要走29次，才能学会） ===========
1. 创建模拟可视化环境env
2. 创建一颗大脑brain
3. 大脑根据env给予的反馈进行学习，习得在env环境下的利益最大化
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
		print('走第' + str(epsiode) + '次迷宫')
		# 1. 探索者回到迷宫入口
		state = env.reset() 

		# 2. 探索者走到出口，或者跌入深渊
		while True:

			# 1. 思考当前状态下要走哪一步
			action = brain.choose_action(str(state))

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
						
