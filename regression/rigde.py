# 岭回归：一种将L2作为正则化工具的线性最小二乘回归。
# 在岭回归中，模型会保留所有的特征变量，但是会减小特征变量的系数值，让特征变量对预测结果的
# 影响变小， 在岭回归中是通过改变其alpha 参数来控制减小特征变量系数的程度。而这
# 种通过保留全部特征变量，只是降低特征变量的系数值来避免过拟合的方法，我们称之为L2 正则化。

from sklearn.datasets import load_boston
from sklearn.linear_model import Ridge
from sklearn.model_selection import train_test_split
# 岭回归参数调节:可以提高alpha 值来降低过拟合的程度。
X, y = load_boston(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
ridge = Ridge(alpha=1).fit(X_train, y_train)
print('山岭训练集得分：{:.2f}'.format(ridge.score(X_train,y_train)))
print('山岭测试集得分：{:.2f}'.format(ridge.score(X_test,y_test)))

# 这种通过保留全部特征变量，只是降低特征变量的系数值来避免过拟合的方法，我们称之为L2 正则化。
# 波士顿房价数据测试山岭回归（解决线性回归中过度拟合问题）
# X, y = load_boston(return_X_y=True)
# # print(X.shape)
# # print(y.shape)
# X_train, X_test, y_train, y_test = train_test_split(X, y)
# ridge = Ridge().fit(X_train, y_train)
# print('山岭训练集得分：{:.2f}'.format(ridge.score(X_train,y_train)))
# print('山岭测试集得分：{:.2f}'.format(ridge.score(X_test,y_test)))