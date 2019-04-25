'''
'''
运行环境：python3
----------------------------
pandas导入导出
-- 要点
	pandas可以读取与存取的资料格式有很多种，像csv,excel,json,html
	和pickle等。详细看：http://pandas.pydata.org/pandas-docs/stable/user_guide/io.html
-- 读取csv
-- 将资料存取成pickle
-- 读取pickle
'''

import pandas as pd

# 读取csv
data = pd.read_csv('student.csv')

print(data)

# 将资料存取成pickle
data.to_pickle('student.pickle')

# 读取pickle
data1 = pd.read_pickle('student.pickle')
print(data1)
