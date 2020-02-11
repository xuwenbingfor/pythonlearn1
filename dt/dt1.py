# 决策树模型：树枝条件判断，树叶为决策结果。
# 熵：表示随机变量的不确定性。
# 信息增益：表示特征x使得类y的不确定性减少的程度。
# 信息增益率：使用信息增益算法时若使用id作为特征则熵为0，解决信息增益算法算法问题，考虑自身熵问题。
# GINI系数：类似熵的衡量标准。
# 连续值处理：贪婪算法
# 剪枝优化： 预剪枝：限制深度、叶子结点个数、叶子结点样本数、信息增益
#           后剪枝：通过一定的衡量标准，叶子结点越多损失越大

import matplotlib.pyplot as plt
import pandas as pd
from sklearn.datasets.california_housing import fetch_california_housing
from sklearn import tree
from sklearn.model_selection import train_test_split

# 1 加载数据
housing = fetch_california_housing()
X_train,X_test,y_train,y_test = train_test_split(housing.data,housing.target,test_size=0.1,random_state=42)
# print(housing)

# 2 构造决策树模型
dt = tree.DecisionTreeRegressor(random_state=42)
# print(help(tree.DecisionTreeRegressor))
dt.fit(X_train,y_train)
print('训练集得分：',dt.score(X_train,y_train))
print('测试集得分：',dt.score(X_test,y_test))


