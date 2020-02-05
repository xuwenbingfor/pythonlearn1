from sklearn.datasets import make_regression
from sklearn.datasets import load_boston
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
# 波士顿房价数据测试山岭回归（出现过度拟合问题）
X, y = load_boston(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
reg = LinearRegression().fit(X_train, y_train)
print('训练集得分：{:.2f}'.format(reg.score(X_train,y_train)))
print('测试集得分：{:.2f}'.format(reg.score(X_test,y_test)))


# 无噪声数据线性回归
# X, y = make_regression(n_samples=100, n_features=2
#                        , n_informative=2, random_state=1)
# X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)
# lr = LinearRegression().fit(X_train, y_train)
# # 一般线性回归得分
# print('X_train:', X_train.shape)
# print('X_test:', X_test.shape)
# print('训练集得分：{:.2f}'.format(lr.score(X_train, y_train)))
# print('测试集得分：{:.2f}'.format(lr.score(X_test, y_test)))
