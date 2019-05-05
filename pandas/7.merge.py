'''
运行环境：python3

pandas.merge(left, right, how='inner', on=None, left_on=None, right_on=None, left_index=False, right_index=False, sort=False, suffixes=('_x', '_y'), copy=True, indicator=False, validate=None)

工作流程：
		  1. 指定合并依据（列号：用on指定，或者用left_on和right_on共同指定, 或者都不指定（默认使用左右数据集相同的列号）
		                   或者
						   行号：用left_index和right_index共同指定）
		  3. 创建一个新的 merged DataFrame，下面一步是他的创建过程
		  4. 
		  	情况一：left DataFrame的某行ll和right DataFrame中某行lr的合并依据部分相同
				添加新行（ll的非合并依据部分 + lr的非合并依据部分 + 1分合并依据）至merged DataFrame
		  	情况二：left DataFrame的某行ll和right DataFrame中所有行的合并依据部分都不相同
				添加新行（ll + right DataFrame的空行NaN（除掉合并依据部分））至merged DataFrame
		  	情况三：right DataFrame的某行lr和left DataFrame中所有行的合并依据部分都不相同
				添加新行（lr + left DataFrame的空行NaN（除掉合并依据部分））至merged DataFrame
		  5. 	
			switch(how)
				'left':  删除merged DataFrame中含有left DataFrame空行NaN的行
				'right': 删除merged DataFrame中含有right DataFrame空行NaN的行
				'inner': 删除含有空行NaN的行
				'outer': 保留含有空行NaN的行
参数说明：
left ：二维数据, left DataFrame
right：二维数据, right DataFrame
how: {'left',right','outer','inner'},default 'inner'}, default inner
	left:  合并后，删除左半部分含有NaN的行
	right: 合并后，删除右半部分含有NaN的行
    inner: 合并后删除含有NaN的行
	outer: 合并后不删除含有NaN的行

on: label or list
	合并时的依据，它不能和left_on和right_on一起使用
	是列标识或列标识集合，它必须是left DataFrame和right DataFrame共有的

left_on：  label or list
	位于left DataFrame中的合并依据, 它是列标识中或者列标识集合，不与on并用

right_on： label or list 
	位于right DataFrame中的合并依据, 它是列标识中或者列标识集合，不与on并用

left_index: boolean, default False
	合并时的依据，来自left DataFrame的index
right_index: boolean, default False
	合并的依据，来自right DataFrame的index

indicator： boolean, default False
	是否新建一列存放合并记录
'''

import numpy  as np
import pandas as pd

left = pd.DataFrame({'key1':['K0','K1','K2','K3'],
					'key2':['K0','K0','K2','K3'],
					'key3':['K0','K3','K4','K5'],
					'A':['A0','A1','A2','A3'],
					'C':['C0','C1','C2','C3'],
					'E':['E0','E1','E2','E3']},
					index = ['L0','L1','L2','L3'])
right = pd.DataFrame({'key1':['K0','K0','K2','K3'],
					'key2':['K0','K1','K2','K3'],
					'key3':['K0','K0','K2','K4'],
					'C':['C0','C1','C2','C3'],
					'D':['D0','D1','D2','D3'],
					'E':['E0','E1','E2','E3']},
					index = ['L0','L2','L3','L4'])

#++++++++++++++++++++++++ 使用列号所在的值作为合并依据 +++++++++++++++++++++++++++++++++
res = pd.merge(left,right,how='outer',on=['key1','key2'],indicator=False) # 合并参考依据：'key1','key2'的值
res = left.merge(right,how='outer',left_on='key1',right_on='key2',indicator=True) 


#++++++++++++++++++++++++ 使用行号作为合并依据 +++++++++++++++++++++++++++++++++
res = pd.merge(left, right, how = 'outer', left_index = True, right_index=True) 
