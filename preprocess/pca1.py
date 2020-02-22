# pca：将一组N维向量降为K维（K大于0，小于N），目标是选择K个单位正交基，
# 使原始数据变换到这组基上后，各个字段两两间协方差为0，字段的方差则尽可能大
# 协方差矩阵->特征值->对角化->降维

from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_wine
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

wine = load_wine()
X = wine.data
y=wine.target
X_scaled = StandardScaler().fit_transform(X)
# print(X_scaled.shape)
pca = PCA(n_components=2)
pca.fit(X_scaled)
X_pca=pca.transform(X_scaled)
# print(X_pca.shape)
# print(X_pca)
# print(y)
X0 = X_pca[y == 0]
X1 = X_pca[y == 1]
X2 = X_pca[y == 2]

# # 1、绘制散点图
# plt.scatter(X0[:,0],X0[:,1],c='b',s=60,edgecolors='k')
# plt.scatter(X1[:,0],X1[:,1],c='g',s=60,edgecolors='k')
# plt.scatter(X2[:,0],X2[:,1],c='r',s=60,edgecolors='k')
# # 设置图注
# plt.legend(wine.target_names,loc='best')
# plt.xlabel('component 1')
# plt.xlabel('component 2')
# plt.show()

# 2、主成分和原始特征的关系，如果从数学角度来说需要了解内积和投影。
# 使用主成分绘制热度图，正数表示正相关，负数表示负相关。
print(pca.components_)
plt.matshow(pca.components_,cmap='plasma')
# y轴属性
plt.yticks([1,0],['component 1','component 2'])
# colorbar
plt.colorbar()
# x轴属性
plt.xticks(range(len(wine.feature_names)),wine.feature_names,rotation=60,ha='left')
plt.show()