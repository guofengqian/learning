'''
运行环境：python3

合并concat：
-- 要点：合并多组数据
-- axis（合并方向）
'''

import pandas as pd
import numpy  as np

# 定义资料集
df1 = pd.DataFrame(np.ones((3,4))*0, columns = ['A','B','C','D'])
df2 = pd.DataFrame(np.ones((3,4))*1, columns = ['A','B','C','D'])
df3 = pd.DataFrame(np.ones((3,4))*2, columns = ['A','K','C','D'])

# 纵向合并（axis=0）
df4 = pd.concat([df1,df2,df3],axis=0)

# 将index_ignore设定为True(行标识重新从0递增排序)
df5 = pd.concat([df1,df2,df3],axis=0,ignore_index=True)
print(df5)

######## join（合并方式）###########
# 定义资料集
df1 = pd.DataFrame(np.ones((3,4))*1, index=[1,2,3], columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*2, index=[2,3,4], columns=['b','c','d','e'])

# 纵向（默认join='outer'）：有相同的column上下合并在一起，其他独自的columns单独一列
res = pd.concat([df1,df2],axis=0,join='outer')

# 纵向(join='inner')：只有相同的column合并在一起，其他的会被抛弃
res = pd.concat([df1,df2],axis=0,ignore_index=True,join='inner')
print(res)
