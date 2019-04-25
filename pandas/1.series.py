'''
pandas是基于numpy构建。
numpy是列表形式，没有数值标签
pandas是字典形式。

输出：
0     1.0
1     3.0
2     6.0
3     NaN
4    44.0
5     1.0
dtype: float64


索引在左边，值在右边。由于我们没有为数据创建
指定索引，它会自动创建一个0~N-1（N为长度）的
整数型索引

'''
import numpy  as np
import pandas as pd

s = pd.Series([1,3,6,np.nan, 44, 1])

print(s)
