import np as np
from sklearn.naive_bayes import BernoulliNB

# 朴素贝叶斯：在机器学习中，朴素贝叶斯分类器是一系列以假设特征之间强独立（朴素）下运用贝叶斯定理为基础的简单概率分类器。
## 当特征是离散变量时，使用多项式模型
### 1. 注意：当特征中既有连续变量又有离散变量时，一般将连续变量离散化后使用多项式模型

## 当特征是连续变量时，使用高斯模型

## 伯努利模型和多项式模型是一致的，但要求特征是二值化的（1，0）

X = np.array([
    [0, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 1, 1, 0],
    [0, 0, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 0, 1],
])
# print(X.sum(axis=0))
y = np.array([0, 1, 1, 0, 1, 0, 0])
# print(X[y == 1])
counts = {}
# 统计下雨/不下雨情况下，刮北风、闷热、多云、天气预报有雨的次数
for label in np.unique(y):
    counts[label] = X[y == label].sum(axis=0)

# print(counts)

clf = BernoulliNB().fit(X, y)

next_day = [[1, 0, 1, 0]]
# 预测这一天 0,0,1,0情况下是否会下雨
pre = clf.predict(next_day)
# 预测这一天 0,0,1,0情况下下雨/不下雨的概率
pre_proba = clf.predict_proba(next_day)
print(pre)
print(pre_proba)
