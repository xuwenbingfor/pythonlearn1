# 数据源读写
# DataFrame
## 常见属性values、index、columns、dtypes
## 查：loc[行索引名称(未指定index时是行索引位置)或条件,列索引名称]\iloc[行索引位置,列索引位置]
## at:https://blog.csdn.net/sinat_29675423/article/details/87975489
## 改：原理
## 增/删
## 统计：https://www.jianshu.com/p/360c69f0083e
#Series
## get
import pandas as pd
import numpy as np

frame = pd.DataFrame(np.random.rand(4, 3), columns = list('abc'), index = ['Utah', 'Ohio', 'Texas', 'Oregon'])
print(frame.index)
print(frame)