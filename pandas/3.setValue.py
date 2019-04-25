'''

更改数据里面的值

'''

import pandas as pd
import numpy  as np

# 创建数据
dates = pd.date_range('20190423',periods=6)
df = pd.DataFrame(np.arange(24).reshape(6,4),
				  index = dates, columns = ['A','B','C','D'])
print(df)

# 根据标签设置（loc）
#df['B']['20190424'] = 10
df.loc['20190425','B']  = 111 # '20190425'是行标签,'B'是列标签
print(df)

# 根据位置设置（iloc）
df.iloc[2,1] = 12 # 2是行号，1是列号
print(df)

# 根据条件设置
df.B[df.A > 8] = 0
print(df)

# 加一列空数据
df['F'] = np.nan
print(df)

# 加一列Series序列
df['E'] = pd.Series([1,2,3,4,5,6],
		index=pd.date_range('20190423',periods=6))
print(df)
