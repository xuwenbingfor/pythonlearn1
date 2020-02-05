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