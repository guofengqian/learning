import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt

####### DataFrame可视化（用点状图或柱状图的方来来显示两个DataFrame中两个一位数组之间的关系）
# 要显示的数据
ys = [[1,1,2,1],
	 [2,4,4,4],
	 [3,6,6,5],
	 [4,8,8,6]]
# 添加要显示的数据 -- 方法1
data1 = pd.DataFrame(
	 ys,
	 index=[0,1,2,3],
	 columns=['A','B','C','D'])
data1.plot.scatter(x='A',y='C',label='scatter') # 点状图
data1.plot.bar(x='A',y='C',label='bar') # 柱状图


# 进行显示
plt.show()
