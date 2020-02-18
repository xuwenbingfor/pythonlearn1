import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_blobs
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import Normalizer

# https://www.cnblogs.com/peixu/p/8011656.html
X,y=make_blobs(n_samples=40,centers=2,random_state=50,cluster_std=2)
# print(X)
# print(y)
# plt.scatter(X[:,0],X[:,1],c=y)

# 1、StandardScaler原理：将所有数据的特征值转换为均值为0 ，而方差为l 的状态， 这样就可以确保数据的“大小”都是一致的，这样更利于模型的训练。
# X_1 = StandardScaler().fit_transform(X)


# 2、MinMaxScaler将特征值都被转换到0 到l 之
# X_1 = MinMaxScaler().fit_transform(X)


# 3、RobustScaler还有一种数据转换的方法，和StandardScaler 比较近似，但是它并不是用均值和方差来进行转换，而是使用中位数和四分位数。是一种粗暴的缩放方式。
# X_1 = RobustScaler().fit_transform(X)


# 4、Normalizer这种方法将所有样本的特征向量转化为欧几里得距离为l。也就是说，它把数据的分布变成一个半径为1 的圆，或者是一个球。
# X_1 = Normalizer().fit_transform(X)
# plt.scatter(X_1[:,0],X_1[:,1],c=y)
# plt.show()

# 验证数据预处理是否能够提高模型准确率
