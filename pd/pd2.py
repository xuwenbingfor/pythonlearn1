import pandas as pd
# import numpy as np

# 读取CSV文件
titanic = pd.read_csv('titanic.csv')
# print(titanic.head())
# print(type(titanic['Age'])) # pandas.core.series.Series

# 分组计算
# print(titanic.pivot_table(index="Pclass", values="Survived", aggfunc=np.mean))

# 丢弃缺失值
# print(titanic.dropna(axis=0,subset=['Age','Sex']))

# 重排index（drop=True原来index不要了）
# sorted_titanic = titanic.sort_values("Age",ascending=False)
# print(sorted_titanic)
# print(sorted_titanic.reset_index(drop=True))

# 应用自定义function
# def row_100(column):
#     return column.loc[100]
# print(titanic.apply(row_100))

# def not_null_count(column):
#     # print(column)
#     column_null = pd.isnull(column)
#     column_column_null =column[column_null]
#     return len(column_column_null)
# titanic.apply(not_null_count)

# Series
# print(titanic["Age"][0:5])
# print(type(titanic["Age"].values)) # numpy.ndarray
