import pandas as pd

# 读取CSV文件
famliy = pd.read_csv('data.csv')
# print(famliy)
# print(type(famliy))

# DataFrame 数据类型
# print(famliy.dtypes)
# print(famliy.columns)
# print(famliy.shape)
# for o in famliy.columns:
#     print(o)

#  取前若干条数据，默认5
# print(famliy.head(2))

#  取后若干条数据
# print(famliy.tail(2))

# 索引
# print(famliy.loc[0])
# print(famliy.loc[0:1])
# print(famliy['name'])
# print(famliy.loc[0:1]['name'])
# print(famliy.loc[0:1][['name', 'age']])

# 计算
# print(famliy['age'] * 10)
# print(famliy['age'] * famliy['index'])
# famliy['score'] = famliy['age'] * 10
# print(famliy)
# print(famliy['age'].max())

# 排序(inplace是否用排序后数据替换原有数据)
# famliy.sort_values('age', inplace=True, ascending=False)
# print(famliy)
# famliy.sort_index(inplace=True)
# print(famliy)
