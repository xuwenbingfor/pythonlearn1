import numpy as np
from sklearn.naive_bayes import BernoulliNB

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
# 预测这一天 0,0,1,0情况下是否会下雨
next_day = [[1, 0, 1, 0]]
pre = clf.predict(next_day)
print(pre)
