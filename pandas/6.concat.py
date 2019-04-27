'''
运行环境：python3

合并concat：
-- 要点：合并多组数据
-- axis（横向合并还是纵向合并）
-- ignore_index（合并后，是否要对重复的行/列标识进行重新排列）
-- join（合并后，是否删除含有空数据的行/列）
-- join_axes（合并后，应该保留的行/列）
'''

import pandas as pd
import numpy  as np

# 定义资料集
df1 = pd.DataFrame(np.ones((3,4))*0, index=[1,2,3],columns = ['A','B','C','D'])
df2 = pd.DataFrame(np.ones((3,4))*1, index=[1,2,3],columns = ['A','B','C','D'])
df3 = pd.DataFrame(np.ones((3,4))*2, index=[2,3,4],columns = ['A','K','C','D'])

######## axis（横向合并还是纵向合并）#########
# axis（0：纵向合并）纵向合并（axis=0）
res = pd.concat([df1,df2,df3],axis=0)
# axis（1：横向合并）横向合并（axis=1）
res = pd.concat([df1,df2,df3],axis=1)

####### index_ignore（合并后, 是否要对重复的行/列标识进行重新排列）########
# ignore_index=True（在横向合并时，如果列标识有重复，则把列标识从0递增排序）
res = pd.concat([df1,df2,df3],axis=1,ignore_index=True)
# ignore_index=True（在纵向合并时，如果行标识有重复，则把行标识从0递增排序）
res = pd.concat([df1,df2,df3],axis=1,ignore_index=True)

######## join（合并后，是否删除含有空数据的行/列）###########
# 定义资料集
df1 = pd.DataFrame(np.ones((3,4))*1, index=[1,2,3], columns=['a','b','c','d'])
df2 = pd.DataFrame(np.ones((3,4))*2, index=[2,3,4], columns=['b','c','d','e'])

# join='outer'（ 纵向合并，保留含有NaN的列
res = pd.concat([df1,df2],axis=0,join='outer') # 纵向合并
# join='outer'（ 横向合并，保留含有NaN的行)
res = pd.concat([df1,df2],axis=1,join='outer') # 横向合并
# join='inner'（纵向合并，删除含有有NaN的列)
res = pd.concat([df1,df2],axis=0,ignore_index=True,join='inner')
# join='inner'（横向合并，删除含有NaN的行)
res = pd.concat([df1,df2],axis=1,ignore_index=True,join='inner')


########## join_axes（合并后，应该保留的行/列）############
# join_axes='df1.index'，只保留与df1行标识相同的行
res = pd.concat([df1,df2],axis=1,join_axes=[df1.index])
# join_axes='df2.index'，只保留与df2行标识相同的行
res = pd.concat([df1,df2],axis=1,join_axes=[df2.index])
# join_axes='df1.columns'，只保留与df1列标识相同的行
res = pd.concat([df1,df2],axis=0,join_axes=[df1.columns])
# join_axes='df2.columns'，只保留与df2列标识相同的行
res = pd.concat([df1,df2],axis=0,join_axes=[df2.columns])


