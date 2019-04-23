'''

从带数值标签的表中提取相应数据

'''

import numpy  as np
import pandas as pd

# 建立一张6x4的矩阵数据
dates = pd.date_range('20190423',periods=6)
df    = pd.DataFrame(np.arange(24).reshape(6,4),
					 index = dates, columns = ['A','B','C', 'D'])

# 选择指定列（两种方法）
print(df['A'])
print(df.A)

# 单独指定行，没有这样的写法
#print(df['20190423']) 这是错的

# 选择连续的多行（两种方法）
print(df[0:2])
print(df['20190423':'20190424'])

# 根据标签loc选择单行，这里就弥补了之前不能单独指定行的缺陷
print(df.loc['20190423'])

# 根据标签loc选择全部行，某些列
print(df.loc[:,'A':'B'])

# 根据标签loc选择指定行，某些列
print(df.loc['20190423','A':'B'])

# 根据标签loc选择某些行，某些列
print(df.loc['20190423':'20190424','A':'B'])

# 根据序列iloc，选择指定行指定列的数据
print(df.iloc[3,1])

# 根据序列号iloc，选择全部行，指定列
print(df.iloc[:,1])

# 根据序列号iloc，选择多行，指定列
print(df.iloc[[1,2],1])


