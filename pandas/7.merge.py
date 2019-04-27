'''
运行环境：python3

merge：
-- 
'''

import numpy  as np
import pandas as pd

++++++++++++++++++++++++ 列合并 +++++++++++++++++++++++++++++++++
# 定义资料集
left = pd.DataFrame({'key1':['K0','K0','K5','K3'],
					'key2':['K0','K1','K0','K1'],
					'A':['A0','A1','A2','A3'],
					'C':['B0','B1','B2','B3']})
right = pd.DataFrame({'key1':['K0','K0','K2','K3'],
					'key2':['K0','K0','K0','K1'],
					'C':['C0','C1','C2','C3'],
					'D':['D0','D1','D2','D3']})
###### on（合并时的参考依据：on指定的列标识相同的行两两互相合并，不相同的单独归一行，空处用NaN代替）#######
###### how （是否删除合并后含有NaN的行）
###### indicator （是否要把合并的记录放在新的一列）
res = pd.merge(left,right,on='key1',how='outer',indicator=True) # 合并参考依据：'key1'的值
res = pd.merge(left,right,on=['key1','key2'],how='outer',indicator=True) # 合并参考依据：'key1'和'key2'作为一个整体的的值
print(left)
print(right)
print(res)
'''
     A  C_x key1 key2  C_y    D      _merge
0   A0   B0   K0   K0   C0   D0        both
1   A0   B0   K0   K0   C1   D1        both
2   A1   B1   K0   K1  NaN  NaN   left_only
3   A2   B2   K5   K0  NaN  NaN   left_only
4   A3   B3   K3   K1   C3   D3        both
5  NaN  NaN   K2   K0   C2   D2  right_only

'''

+++++++++++++++++++++++++ 行合并 ++++++++++++++++++++++++++++++++

# 定义资料集
df1 = pd.DataFrame({'col1':[0,1],'col_left':['a','b']})
df2 = pd.DataFrame({'col1':[1,2,2],'col_right':[2,2,2]})
res = pd.merge(df1,df2,on='col1',how='outer')
###### indicator ######


left = pd.DataFrame({'key1':['K0','K4','K2','K3'],
					'key2':['K0','K1','K2','K3'],
					'A':['A0','A1','A2','A3'],
					'B':['B0','B1','B2','B3']})
right = pd.DataFrame({'key1':['K0','K1','K2','K3'],
					'key2':['K0','K1','K2','K3'],
					'C':['C0','C1','C2','C3'],
					'D':['D0','D1','D2','D3']})
res = pd.merge(left,right,on=['key1','key2'],how='inner')
