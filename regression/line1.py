# 线性回归：图像上看是一条直线。使用普通最小二乘法的线性回归。
# 梯度下降：在合适的方向走一个合适的步伐（学习率）更新参数，找到最优解。
## 批量梯度下降：容易得到最优解，但是由于每次考虑所有样本，速度慢
## 随机梯度下降：每次找一个样本，迭代速度快，但不一定每次都朝着收敛的方向
## 小批量梯度下降：每次更新选择一小部分数据来算，实用。

import mat.pyplot as plt
import np as np
from sklearn.linear_model import LinearRegression
# 4、批量数据训练线性回归模型，并使用


# 3、批量数据训练线性回归模型，并使用
from sklearn.datasets import make_regression
# 参数含义
# X, y = make_regression(n_samples=50, n_features=1, n_informative=1
#                        , noise=50, random_state=1)
# reg = LinearRegression().fit(X, y)
# z = np.linspace(-3, 3, 200)
# print(z)
# # np reshape -1表示具体不知道多少行/列
# z = z.reshape(-1, 1)
# print(z)
#
# # s表示点的大小
# plt.scatter(X, y, c='b', s=100)
# plt.plot(z, reg.predict(z), c='k')
# plt.title('Straight Line')
# plt.show()
#
# print('直线系数：{:.2f}'.format(reg.coef_[0]))
# print('直线截距：{:.2f}'.format(reg.intercept_))

# 2、两个点训练线性回归模型，并使用
# X = [[1], [2]]
# y = [3, 5]
# regression = LinearRegression().fit(X, y)
# print('直线方程是：y={:.3f}'.format(regression.coef_[0]), 'x'
#       , '+{:.3f}'.format(regression.intercept_))
#
# z = np.linspace(0, 5, 20)
# # plt.scatter(X, y, s=[20, 100])
# plt.scatter(X, y, s=100)
# plt.plot(z, regression.predict(z.reshape(-1, 1)), c='k')
# plt.title('Straight Line')
# plt.show()


# 1、直线方程
# x = np.linspace(-5, 5, 100)
# y = 0.5 * x + 3
# # print(x)
# # print(y)
# plt.plot(x, y, c='orange')
# plt.title('Straight Line')
# plt.show()
