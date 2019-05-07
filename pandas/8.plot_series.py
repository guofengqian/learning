import numpy  as np
import pandas as pd
import matplotlib.pyplot as plt

######### Series可视化（用线性和点图的方式来显示两个一维数组之间的关系）

# 要显示的数据
x1=[1,2,3,4]
y1=[2,4,5,7]
x2=[11,12,13,14]
y2=[1,2,3,4]

# 添加要显示的数据 -- 方法1
data = pd.Series(y1,index=x1)
data.plot()

# 添加要显示的数据 -- 方法2
plt.plot(x2, y2, 'go--', linewidth=2, markersize=12)

# 进行显示
plt.show()
