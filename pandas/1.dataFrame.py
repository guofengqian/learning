# -*- coding: utf-8 -*-
# 上面这行注释是用于Python支持中文

'''
pandas是在numpy的基础上，设置数值标签，以
标签的形式来索引目标值

np.random.randn(6,4): 返回6行4列的数据，这些数据来自于标准正态分布

'''

import pandas as pd
import numpy  as np

# 生成行标签
dates = pd.date_range('20190422',periods=6)
# 同时指定行标签，列标签
df    = pd.DataFrame(np.random.randn(6,4),index=dates,columns=['a','b','c','d'])
print(df)
print(df['b']['20190423'])  # 这是对的，先指定列标签，再指定行标签
#print(df['20190423']['b']) # 这种用法是错的

'''
                   a         b         c         d
2019-04-22 -0.637966 -1.340507  0.074796 -1.223388
2019-04-23 -1.189856  1.450391 -2.036277 -0.272758
2019-04-24 -0.593260 -1.352030 -0.623816  0.408455
2019-04-25 -2.668526 -0.389462 -0.048257  0.446670
2019-04-26 -1.398292 -0.605747 -2.537124 -1.178271
2019-04-27 -1.534806  0.760442  0.783709  1.385117
1.4503911025305591

'''
# 不指定行标签和列标签
df1 = pd.DataFrame(np.random.randn(6,4))
print(df1)

'''
          0         1         2         3
0 -0.395481 -3.518560  0.718602 -0.878966
1  0.568323 -0.504314  0.539808 -0.370900
2  0.883094  0.150048  0.047736 -0.365881
3  0.167951 -0.078083 -0.182291  1.252051
4  0.715788 -0.076156  0.797072 -0.795603
5  0.090387 -1.555868 -0.202506 -0.590977

'''
# 只指定列标签
print('------df2--------')
df2 = pd.DataFrame({'A':1,
        'B':pd.Timestamp(2019,4,22),
        'C':pd.Series(1,index=list(range(4)),dtype='float32'),
        'D':np.array([3]*4,dtype='int32'),
        'E':pd.Categorical(['test','train','test','train'])})
print(df2)
print(df2.columns) # 表的列标签
print(df2.index)   # 表行标签
print(df2.values)  # 表的值
print(df2.describe()) # 对每一列的数值型数据进行统计分析（平均值，最小值...）
print(df2.dtypes)     # 类型
print(df2.T)          # 翻转
print(df2.sort_index(axis=1,ascending=False))
df2['A'][2] = 3.0
print(df2.sort_values(by='A')) # 按'A'列的数值大小进行排序
