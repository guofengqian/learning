# -*- coding: utf-8 -*-  # 编码转换成ut-8，必须放在第一行
'''
python3 xxx.py

处理丢失数据NaN：
-- 创建含NaN的表格
-- pd.dropna()   取掉含有NaN的行或列
-- pd.fillna()   替换NaN
-- pd.isnull()   为NaNaN表示为True，否则表示为False

'''
import numpy as  np
import pandas as pd

# 创建含NaN的矩阵
dates = pd.date_range('20130101', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6,4)), index = dates, 
					columns = ['A','B','C','D'])
df.iloc[0,1] = np.nan
df.loc['20130102','C'] = np.nan
print(df)

# 直接去掉NaN的行或列，使用dropna,
df1 = df.dropna( # 改变后的值不会覆盖df，而是放在返回值中 
		axis=0,    # 0:对行进行操作；1：对列进行操作
		how='any' # 'any'：只要存在NaN就drop掉；
		             # 'all'：必须全部是NaN才可以drop
		)
print(df1)

# 将NaN的值用其他值代替
df2 = df.fillna(value=0)
print(df2)

# 判断是否有缺失数据NaN,为True表示缺失数据：
df3 = df.isnull()
print(df3)

